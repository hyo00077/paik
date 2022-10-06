from urllib import response
from .models import ReportInput, ReportInputString, SharedText, Paragraph
from .serializers import ReportSerializer, ReportTextSerializer, ShareTextSerializer, ParagraphSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .imageGenerate import ImageGenerate
from .snsShare import snsShare
from rest_framework.response import Response
import os
import time
import qrcode


class ReportList(generics.ListCreateAPIView):
    queryset = ReportInput.objects.all()
    serializer_class = ReportSerializer


@api_view(["GET"])
def ReportStringList(request, report):
    try:
        print(report)
        reportEach = ReportInput.objects.get(pk=report)

    except ReportInputString.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ReportSerializer(reportEach)

        return Response(serializer.data)


@api_view(['GET'])
def getSentence(request, report, pk):
    try:
        print(request, report, pk)
        paragraph = Paragraph.objects.get(report=report, pk=pk)
        sentence = ReportInputString.objects.get(report=report, pk=pk)
    except ReportInputString.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ParagraphSerializer(paragraph)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def shareSentence(request, sentence):
    try:
        sentence = ReportInputString.objects.get(pk=sentence)
        serializer = ShareTextSerializer(data=request.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST" and serializer.is_valid(raise_exception=True):
        serializer.save(sentence=sentence)
        img = ImageGenerate(sentence.text, serializer.data.get("created_at"))
        img.imageComp()
        sns = snsShare(serializer.data.get("snsChoices"),
                       serializer.data.get("snsID"), img.imageDir(), sentence.text)
        sns_work = sns.snsDetect()

        os.remove(img.imageDir())

        if sns_work == False:
            newdict = {"status": status.HTTP_400_BAD_REQUEST}
            newdict.update(serializer.data)
            return Response(newdict)
        elif sns_work == 9:
            newdict = {"status": status.HTTP_501_NOT_IMPLEMENTED}
            newdict.update(serializer.data)
            return Response(serializer.data)
        elif "https:" in str(sns_work):
            newdict = {"url": sns_work, "status": status.HTTP_201_CREATED}
            qr_img = generateQR(sns_work)
            newdict.update({"qr": qr_img})
            newdict.update(serializer.data)
            return Response(newdict)
        elif sns_work == True:
            newdict = {"status": status.HTTP_201_CREATED}
            newdict.update(serializer.data)
            return Response(newdict)
    if request.method == "GET":
        return Response(ReportTextSerializer(sentence).data)


def generateQR(url):
    img = qrcode.make(url)
    savePath = os.path.join("./static/image/qr",
                            "{}.jpg".format(url.split("/")[-1]))
    exportPath = os.path.join("/static/image/qr",
                              "{}.jpg".format(url.split("/")[-1]))
    img.save(savePath)

    return exportPath
