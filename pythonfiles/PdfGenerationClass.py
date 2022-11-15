from fpdf import FPDF
import numpy as np


class PdfGenerationClass:
    '''
    @description
    Method to transfer the Bingo cards generated into the pdf
    @parameter
    cardsArray- Holds the cards to be added to pdf.
    '''

    def CreatePdf(self, cardsArray):
        pdf = FPDF()
        pdf.set_left_margin(70)
        pdf.set_top_margin(50)
        line_height = 10
        col_width = pdf.epw / 8
        start = 1
        for index in cardsArray:
            pdf.add_page()
            pdf.set_font("Courier", "BI", size=25)
            pdf.set_fill_color(r=138, g=43, b=226)
            pdf.set_text_color(r=252, g=252, b=252)
            pdf.cell(82, 10, 'Bingo Card '+str(start), 0, 1, 'C', fill=1)
            pdf.set_font("Times", "B", size=15)
            pdf.set_text_color(r=0, g=0, b=0)
            col_width = pdf.epw / 8
            start += 1
            for row in index:
                textArray = np.array2string(
                    row, precision=1, separator=',', suppress_small=True)
                textArray = textArray[1:-1]
                for numberString in textArray.split(','):
                    pdf.set_fill_color(r=252, g=100, b=150)
                    if numberString == '-1.':
                        pdf.multi_cell(col_width, line_height, "FREE", border=1, align='C',
                                       ln=3, max_line_height=pdf.font_size, fill=True)
                    else:
                        pdf.multi_cell(col_width, line_height, numberString[:-1], border=1, align='C',
                                       ln=3, max_line_height=pdf.font_size, fill=True)
                pdf.ln(line_height)
        pdf = pdf.output("Bingo Cards.pdf")
