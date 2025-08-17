import os
from modules import pdf_parser, text_processing, summarizer, term_definitions, image_processing, knowledge_graph, report_generator

PDF_FILE = "CN UNIT - 1.pdf"

# Step 1: Extract content
text, images = pdf_parser.extract_pdf_content(PDF_FILE)

# Step 2: Clean text & split
cleaned_text = text_processing.clean_text(text)
sections = text_processing.split_sections(cleaned_text)

# Step 3: Summarize abstract
abstract = sections.get("Abstract", cleaned_text[:2000])
summary = summarizer.summarize_text(abstract)

# Step 4: Find technical terms & definitions
terms = ["neural network", "transformer", "backpropagation"]
glossary = {term: term_definitions.get_definition(term) for term in terms}

# Step 5: Enhance images
enhanced_images = [image_processing.enhance_image(img) for img in images]

# Step 6: Build knowledge graph
concepts = ["AI", "Machine Learning", "Deep Learning", "NLP"]
relationships = [("AI", "Machine Learning"), ("Machine Learning", "Deep Learning"), ("Deep Learning", "NLP")]
knowledge_graph.build_knowledge_graph(concepts, relationships)

# Step 7: Generate PDF report
report_generator.create_pdf_report(summary, glossary, enhanced_images, "outputs/graphs/knowledge_graph.png", "outputs/reports/final_report.pdf")

print("✅ Process completed. Report saved in outputs/reports/")
