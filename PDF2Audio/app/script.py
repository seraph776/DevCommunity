#!/usr/bin/env python3
"""
created: 2022-07-24 19:27:01
@author: seraph★776
contact: seraph776@gmail.com
project: Python Crash Course
license: MIT
metadoc: 
"""

import pyttsx3
import pdfplumber
import PyPDF2


def convert_pdf_to_audio(pdf_file):
    with open(pdf_file, 'rb') as pdfFileObj:
        pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)

        pages = pdf_reader.numPages
        with pdfplumber.open(pdf_file) as pdf:
            for i in range(0, pages):
                page = pdf.pages[i]
                text = page.extract_text()
                print(text)
                # initialize pyttsx3
                speaker = pyttsx3.init()

                # save audio file to mp3:
                speaker.save_to_file(text, 'the_raven.mp3')

                # read the text
                speaker.say(text)
                speaker.runAndWait()
