import pyttsx3
import PyPDF2

pdf = open("Preface.pdf", "rb")         # read file in binary mode
reader = PyPDF2.PdfFileReader(pdf)
pages = reader.numPages                 # It gives you the number of pages in your file.
print('Number of Pages -  ', pages)

speaker = pyttsx3.init()                # Initialize text-to-speech

for num in range(pages):
    page = reader.getPage(0)            # The page number you want to listen.
    text = page.extractText()           # extract the text from page
    speaker.say(text)
    speaker.setProperty('rate', 150)    # set the speed of speech
    speaker.runAndWait()
