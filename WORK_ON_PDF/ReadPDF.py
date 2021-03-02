import pyttsx3
import PyPDF2
book = open('sentimental.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Total pages = ",pages)

speaker = pyttsx3.init()
for num in range(4,pages):
    print("Reading page no:",num)
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
