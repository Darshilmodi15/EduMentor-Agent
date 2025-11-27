from tools.pdf_reader import PDFReader
from tools.url_loader import URLLoader

class ContentAgent:
    def __init__(self, memory):
        self.memory = memory
        self.pdf_reader = PDFReader()
        self.url_loader = URLLoader()

    def summarize(self, docs):
        summaries = []
        for doc in docs:
            # Placeholder: Summarize using LLM (pseudo)
            summary = f"Summary of {doc[:50]}..."
            summaries.append(summary)
        combined_summary = "\n".join(summaries)
        self.memory.save("last_summary", combined_summary)
        return combined_summary
