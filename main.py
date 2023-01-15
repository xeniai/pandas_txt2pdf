import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("txt/*.txt")

def read_file(filep):
    file = open(filep)
    for fi in file:
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=50, h=8, txt=fi, ln=2, align="L")
    file.close()

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)
    read_file(filepath)
    pdf.output(f"{name}.pdf")
    