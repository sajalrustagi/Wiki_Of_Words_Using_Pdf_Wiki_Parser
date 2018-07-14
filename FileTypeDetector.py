# This file contains all the functions that help in detecting the type of file(pdf/wiki) given name of file
import enum


# declares different types of file that our system support
class FileType(enum.Enum):
    pdf = 1
    wiki = 2
    unknown = 3


# computes if file provided is pdf/wiki/unknown
def get_file_type(name):
    file_type = FileType.unknown
    if is_pdf_file(name):
        file_type = FileType.pdf
    elif is_wiki_link(name):
        file_type = FileType.wiki
    return file_type


# returns true if file if of type pdf
def is_pdf_file(name):
    return ".pdf" in name


# returns true if file is of type wiki
def is_wiki_link(name):
    return ("http" or "www") in name

