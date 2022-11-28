from fpdf import FPDF
import numpy as np
import BingoConstantsClass

'''
@description
PdfGenerationClass - Class which contains the pdf creation logic for the cards.
'''


class PdfGenerationClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self):
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()

    '''
    @description
    Method to transfer the Bingo cards generated into the pdf
    Picture specified by user is added in the FREE cells.
    @parameter
    cardsArray- Holds the cards to be added to pdf.
    inputToValueDict - Dictionary with the user input values.
    '''

    def CreatePdf(self, cardsArray, inputToValueDict):
        pdf = FPDF()

        #Setting the cell size of the BINGO cards
        lineHeight = 10
        columnWidth = pdf.w / \
            (inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL] * 1.2)

        #Setting the PDF margin to adapt to the changes of the size of BINGO cards
        pdf.set_left_margin(
            (pdf.w - inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL] * columnWidth) / 2)
        pdf.set_top_margin(
            (pdf.h - (inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW] * lineHeight + 10)) / 2)
        start = 1

        #Setting the BINGO cards header font,size & color in PDF to be dynamic and change to the size of BINGO cards
        for index in cardsArray:
            pdf.add_page()
            pdf.set_font("Courier", "BI", size=25)
            pdf.set_fill_color(r=59, g=113, b=245)
            pdf.set_text_color(r=252, g=252, b=252)
            pdf.cell((inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL] * columnWidth), 10,
                     'Bingo Card '+str(start), 0, 1, 'C', fill=1)
            pdf.set_font("Times", "B", size=15)
            pdf.set_text_color(r=0, g=0, b=0)
            start += 1

            #Input the number arrays in cells to output to PDF and replace the FREE cells with image input from user
            for row in index:
                textArray = np.array2string(
                    row, precision=1, separator=',', suppress_small=True)
                textArray = textArray[1:-1]
                for numberString in textArray.split(','):
                    pdf.set_fill_color(r=122, g=169, b=240)
                    numberString = numberString.strip()
                    if numberString == "-1.":
                        xPos = pdf.get_x()
                        yPos = pdf.get_y()
                    pdf.cell(columnWidth, lineHeight,
                             numberString[:-1], border=1, align='C',
                             ln=0, fill=True)
                    if numberString == "-1.":
                        pdf.image(inputToValueDict[self.bingoConstantsClassInstance.IMAGE_REQUESTED], x=xPos, y=yPos,
                                  w=columnWidth, h=lineHeight)
                pdf.ln(lineHeight)
        pdf = pdf.output("Bingo Cards.pdf")
