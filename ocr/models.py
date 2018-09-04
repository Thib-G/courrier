import os
import re
from django.db import models
import datetime

# Create your models here.

class OcrDocument(models.Model):
    OCR = 'ocr'
    PDFTOTEXT = 'pdftotext'

    TEXT_EXTRACT_TYPE_CHOICES = (
        (OCR, 'OCR with ocrmypdf (tesseract)'),
        (PDFTOTEXT, 'Text extracted from existing PDF with pdftotext'),
    )

    dirname = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)

    text_extract_type = models.CharField(
        max_length=9,
        choices=TEXT_EXTRACT_TYPE_CHOICES,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_path(self):
        return os.path.join(self.dirname, self.filename)

    def __str__(self):
        return f"{self.dirname}/{self.filename}"

    class Meta:
        ordering = ['-pk']


class OcrPage(models.Model):

    page_num = models.IntegerField()
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ocr_document = models.ForeignKey(OcrDocument, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ocr_document} page {self.page_num}"

    def get_page_by_line(self):
        return [line for line in str(self.text).split('\n') if not line.strip() == '']

    class Meta:
        ordering = ['page_num']
