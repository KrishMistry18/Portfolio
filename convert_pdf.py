import fitz
import glob
import os

pdfs = glob.glob("Devtown — Machine Learning Mastery*.pdf")
for pdf in pdfs:
    doc = fitz.open(pdf)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    
    # generate jpg name
    out_name = pdf.replace(".png.pdf", ".jpg").replace(".pdf", ".jpg")
    pix.save(out_name)
