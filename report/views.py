from django.shortcuts import render


def indexReport(request):
    return render(request, "report/index.html")


def firstView(request):
    return render(request, "report/R01.html")


def secondView(request):
    return render(request, "report/R02.html")


def thirdView(request):
    return render(request, "report/R03.html")
