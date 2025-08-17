import re

def clean_text(text):
    # Remove references, extra spaces, and headers/footers
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_sections(text):
    sections = {}
    patterns = ["Abstract", "Introduction", "Methods", "Results", "Conclusion"]
    for section in patterns:
        match = re.search(section, text, re.IGNORECASE)
        if match:
            sections[section] = text[match.start():]
    return sections
