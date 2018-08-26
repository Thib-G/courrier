from django.db import models

# Create your models here.

class OcrDocument(models.Model):
    filename = models.CharField(max_length=255)

    def __str__(self):
        return self.filename

class OcrPage(models.Model):
    page_num = models.IntegerField()
    text = models.TextField()

    ocr_document = models.ForeignKey(OcrDocument, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ocr_document} page {self.page_num}"
