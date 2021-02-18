import PyPDF2
import textract
from gtts import gTTS
import playsound

pdf_url = "TEST PDF DOCUMENT.pdf"

with open(pdf_url, "rb") as pdf_file:
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdfReader.numPages
    page_count = 0
    output_text = ""
    # Loop through each page in pdf | Non-Scanned Files - Store Text
    for page in range(num_pages):
        pageObj = pdfReader.getPage(page)
        output_text += pageObj.extractText()
    if output_text != 0:
        pass
    else:
        # Scanned Files - Store Text
        output_text = textract.process(pdf_url, method="tesseract", language="eng")

print(output_text)
# Use google
output_file = gTTS(text=output_text, lang="en")
output_file.save("TEST SPEECH.mp3")

# Play that funky music white boy...
playsound.playsound("TEST SPEECH.mp3")
