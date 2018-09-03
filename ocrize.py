#
# Move at the root of your directory containing the PDF documents
#

import os
import subprocess
from pathlib import Path

os.chdir('./_Courrier')
cwd = Path.cwd()

print('Searching files')
files = ((root, file) for root, dirs, files
	 in os.walk('.') 
	 for file in files 
	 if file.lower().endswith('.pdf') and (not file.lower().endswith('-ocr.pdf')) and 'wiard -pierret' not in file)

limit = 100000


for index, file in enumerate(files):
	dir, filename = file
	
	os.chdir(dir)

	# Skip if file hase already been ocr'ed
	filename_noext = os.path.splitext(filename)[0]
	if Path.is_file(Path(f"{filename_noext}-ocr.txt")) or Path.is_file(Path(f"{filename_noext}-pdftotext.txt")):
		print(f"Skipping file ({index}) {filename} in {dir}: already processed")
		
	else:
		print(f"Processing file ({index}) {filename} in {dir}")
		args = [
			'ocrmypdf',
			'-l', 'fra',
			#'--output-type', 'pdf',
			'--deskew',
			'--rotate-pages',
			#'--skip-text',
			'--sidecar', f"{filename_noext}-ocr.txt",
			filename,
			f"{filename_noext}-ocr.pdf"
		]
		print(' '.join(args))
		subprocess.run(args)
	
		# Recheck and apply pdftotext if ocr was not generated
		if not Path.is_file(Path(f"{filename_noext}-ocr.txt")):
			print(f"File ({index}) {filename} in {dir} was not OCR'ed. Extracting text instead")
			args = [
				'pdftotext',
				filename,
				f"{filename_noext}-pdftotext.txt"
			]
			print(' '.join(args))
			subprocess.run(args)

	os.chdir(cwd)

	if index == limit:
		break

