from numpy import source
from rest_framework import serializers
from .models import ReportInput, ReportInputString, SharedText, Paragraph
import time
from typing import Dict, Any


class ShareTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedText
        fields = '__all__'
        read_only_fields = ('sentence',)


class ReportTextSerializer(serializers.ModelSerializer):
    # text_shared = ShareTextSerializer(many=True, read_only=True)
    shared_count = serializers.IntegerField(
        source='text_shared.count',
        read_only=True
    )

    class Meta:
        model = ReportInputString
        fields = '__all__'


class ParagraphSerializer(serializers.ModelSerializer):
    report_text = ReportTextSerializer(many=True, read_only=True)

    class Meta:
        model = Paragraph
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    report = ParagraphSerializer(many=True, read_only=True, )

    class Meta:
        model = ReportInput
        fields = '__all__'
