import fitz  # PyMuPDF
import os

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    text_content = ""
    images = []

    for page_num, page in enumerate(doc):
        text_content += page.get_text()
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            img_filename = f"outputs/figures/page{page_num+1}_img{img_index+1}.png"
            pix.save(img_filename)
            images.append(img_filename)
    
    return text_content, images
