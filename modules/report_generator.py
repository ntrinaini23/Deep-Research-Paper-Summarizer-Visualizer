from fpdf import FPDF

def create_pdf_report(summary, glossary, enhanced_images, graph_path, output_path):
    pdf = FPDF()
    pdf.add_page()

    # Path where you placed the font
    font_path_regular = r"C:\Users\leela\OneDrive\Desktop\Deep Research Paper Summarizer + Visualizer\dejavu-fonts-ttf-2.37\ttf\DejaVuSans.ttf"
    font_path_bold = r"C:\Users\leela\OneDrive\Desktop\Deep Research Paper Summarizer + Visualizer\dejavu-fonts-ttf-2.37\ttf\DejaVuSans-Bold.ttf"

    pdf.add_font("DejaVu", "", font_path_regular, uni=True)
    pdf.add_font("DejaVu", "B", font_path_bold, uni=True)

    pdf.set_font("DejaVu", "", 12)

    pdf.multi_cell(0, 10, summary)

    pdf.add_page()
    pdf.set_font("DejaVu", "B", 14)
    pdf.cell(0, 10, "Glossary", ln=True)

    pdf.set_font("DejaVu", "", 12)
    for term, definition in glossary.items():
        pdf.multi_cell(0, 10, f"{term}: {definition}")

    pdf.output(output_path)
