# courrier app: convert PDF to text

- copy `courrier/settings.py-dist` to `courrier/settings.py` and edit your database settings
- run `python manage.py makemigrations` and `python manage.py migrate`
- copy pdf files in `./pdf/` folder and use OCR.ipynb notebook in Jupyter to generate text from pdf to database
