# This class declares classes/function that can be used parse different type of files and
# return the text present in the file
# if file is of type pdf, it uses PdfContentParser to parse the content of pdf
# if file is of type wiki, it uses WikiContentParser to parse the content of wikipedia page

import PyPDF2
import textract
import wikipedia
import FileTypeDetector


def parse(filename):
    file_type = FileTypeDetector.get_file_type(filename)
    text = ""
    try:
        if file_type == FileTypeDetector.FileType.pdf:
            text = PdfContentParser.parse(filename)
        elif file_type == FileTypeDetector.FileType.wiki:
            text = WikiContentParser.parse(filename)
    except:
        print('An exception occured while parsing the file : ', filename)
    return text


class PdfContentParser:

    def __init__(self):
        return

    @staticmethod
    def parse(filename):
        # open allows you to read the file
        pdf_file_obj = open(filename, 'rb')
        # The pdfReader variable is a readable object that will be parsed
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj, strict=False)
        # discerning the number of pages will allow us to parse through all # the pages
        num_pages = pdf_reader.numPages
        count = 0
        text = ""
        # The while loop will read each page
        while count < num_pages:
            page_obj = pdf_reader.getPage(count)
            count += 1
            text += page_obj.extractText()
        # This if statement exists to check if the above library returned
        # words. It's done because PyPDF2 cannot read scanned files.
        if text != "":
            text = text

        # If the above returns as False, we run the OCR library textract to
        # convert scanned/image based PDF files into text
        else:
            text = textract.process(filename, method='tesseract', language='eng')
        return text


class WikiContentParser:

    def __init__(self):
        return

    @staticmethod
    def parse(filename):
        # fetches the last part of url
        wiki_name = filename.rsplit('/', 1)[-1]
        # uses wikipedia module to fetch information regarding the last part
        wiki_page = wikipedia.page(wiki_name)
        text = ""
        # if url is same as provided then get the page contents
        if wiki_page.url == filename:
            text = wiki_page.content
        return text
