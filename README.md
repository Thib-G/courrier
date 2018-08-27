# courrier app: convert PDF to text

Requirement: [tesseract](https://github.com/tesseract-ocr/tesseract), [imagemagick](https://www.imagemagick.org/) and [ghostscript](https://www.ghostscript.com/)

- copy `courrier/settings.py-dist` to `courrier/settings.py` and edit your database settings
- run `python manage.py makemigrations` and `python manage.py migrate`
- copy pdf files in `./pdf/` folder and use OCR.ipynb notebook in Jupyter to generate text from pdf to database
- run `python manage.py runserver` and go tp http://localhost:8000 to show the text version of the files.
