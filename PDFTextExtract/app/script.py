import PyPDF2


# STEP 1: open PDF and convert to text
def extract_text_from_pdf(pdf_filename: str) -> str:
    text_output = ''
    with open(pdf_filename, 'rb') as pdf_object:
        pdf_reader = PyPDF2.PdfFileReader(pdf_object)
        for i in range(0, pdf_reader.numPages):
            page_obj = pdf_reader.getPage(i)
            text_output += page_obj.extractText()
    return text_output


# STEP 2: Save Text to File
def save_converted_text(text_file: str, filename: str) -> None:
    with open(filename, 'w+', encoding='utf8') as file_obj:
        file_obj.write(text_file)
    print(f'{text_file} has been successfully saved.')


if __name__ == '__main__':
    # extract text from PDF
    text_from_pdf = extract_text_from_pdf('the_raven.pdf')
    # save extracted text
    save_converted_text(text_from_pdf, 'the_raven.txt')
