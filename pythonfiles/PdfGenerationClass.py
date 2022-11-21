from fpdf import FPDF
import numpy as np
from PIL import Image
import requests
from io import BytesIO

class PdfGenerationClass:
    '''
    @description
    Method to transfer the Bingo cards generated into the pdf
    Include picture input from user to obtain URL source to insert picture in the FREE cells.
    @parameter
    cardsArray- Holds the cards to be added to pdf.
    sizeofCard - User input on size of cards to be generated and printed to pdf. 
    '''

    def CreatePdf(self, cardsArray, sizeOfCardRow, sizeOfCardCol, imageURL):
        pdf = FPDF()
        lineHeight = 10
        columnWidth = pdf.w / (sizeOfCard * 1.2)
        pdf.set_left_margin((pdf.w - sizeOfCardCol * columnWidth) / 2)
        pdf.set_top_margin((pdf.h - (sizeOfCardRow * lineHeight + 10)) / 2)
        start = 1
        response = requests.get(imageURL)
        image = Image.open(BytesIO(response.content))
        for index in cardsArray:
            pdf.add_page()
            pdf.set_font("Courier", "BI", size=25)
            pdf.set_fill_color(r=138, g=43, b=226)
            pdf.set_text_color(r=252, g=252, b=252)
            pdf.cell((sizeOfCardCol * columnWidth), 10, 'Bingo Card '+str(start), 0, 1, 'C', fill=1)
            pdf.set_font("Times", "B", size=15)
            pdf.set_text_color(r=0, g=0, b=0)
            start += 1
            for row in index:
                textArray = np.array2string(
                    row, precision=1, separator=',', suppress_small=True)
                textArray = textArray[1:-1]
                for numberString in textArray.split(','):
                    pdf.set_fill_color(r=252, g=100, b=150)
                    if numberString =="-1." or numberString == " -1.":
                        xPos = pdf.get_x()
                        yPos = pdf.get_y()
                    pdf.multi_cell(columnWidth, lineHeight,
                                   numberString[:-1], border=1, align='C',
                                   ln=3, max_line_height=pdf.font_size, fill=True)
                    if numberString =="-1." or numberString == " -1.":
                        pdf.image(image, x=xPos, y=yPos,
                                  w=columnWidth, h=lineHeight)
                pdf.ln(lineHeight)
        pdf = pdf.output("Bingo Cards.pdf")
