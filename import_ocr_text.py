# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:58:54 2018

@author: JJD8300
"""

import os
from pathlib import Path
import django
from django.db import transaction, connection

os.environ['DJANGO_SETTINGS_MODULE'] = 'courrier.settings'
django.setup()

from ocr.models import OcrDocument, OcrPage

path = Path('C:/Data/Courrier/_Courrier')
os.chdir(path)

print('Searching files')
files = ((root, file) for root, dirs, files
	 in os.walk('.') 
	 for file in files 
	 if file.lower().endswith('-ocr.txt') or file.lower().endswith('-pdftotext.txt'))

cursor = connection.cursor()
cursor.execute('TRUNCATE TABLE ocr_ocrdocument RESTART IDENTITY CASCADE')

for index, file in enumerate(files):
    root, filename = file
    print(f"({index}) Processing file {filename} in {root}")
    with open(os.path.join(root, filename), 'r', encoding='utf8') as f:
        pages = f.read()
        with transaction.atomic():
            doc = OcrDocument()
            doc.dirname = root.replace('.\\', '').replace('\\', '/')
            if filename.lower().endswith('-ocr.txt'):
                doc.filename = filename.replace('-ocr.txt', '-ocr.pdf')
                doc.text_extract_type = 'ocr'
            elif filename.lower().endswith('-pdftotext.txt'):
                doc.filename = filename.replace('-pdftotext.txt', '.pdf')
                doc.text_extract_type = 'pdftotext'
            doc.save()
            OcrPage.objects.bulk_create(OcrPage(page_num=i+1, text=text, ocr_document=doc) for i, text in enumerate(pages.split('\f')))
    