# ==============================
# Configuration File
# ==============================

# ------------------------------
# Model & Pipeline Settings
# ------------------------------
# You can switch models if needed; these are from HuggingFace
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
TEXT_CLASSIFICATION_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
NER_MODEL = "dslim/bert-base-NER"

# Device preference ("cuda" for GPU, "cpu" for CPU)
DEVICE = "cpu"  # change to "cuda" if you have GPU support

# ------------------------------
# PDF Parsing Settings
# ------------------------------
MAX_PAGES = None  # None means parse all pages
EXTRACT_IMAGES = True

# ------------------------------
# NLP Processing
# ------------------------------
MIN_SUMMARY_LENGTH = 50
MAX_SUMMARY_LENGTH = 300

# ------------------------------
# Output Settings
# ------------------------------
OUTPUT_DIR = "outputs"
SUMMARY_FILENAME = "summary.txt"
REPORT_FILENAME = "report.pdf"

# ------------------------------
# Knowledge Graph Settings
# ------------------------------
GRAPH_IMAGE_FILENAME = "knowledge_graph.png"

# ------------------------------
# API / External Requests
# ------------------------------
# For example, if you want to fetch definitions or related data
WIKIPEDIA_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

# ------------------------------
# Logging
# ------------------------------

LOG_LEVEL = "INFO"
