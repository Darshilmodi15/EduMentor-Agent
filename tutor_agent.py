class TutorAgent:
    def __init__(self, memory):
        self.memory = memory

    def explain(self, summary, level="beginner"):
        # Placeholder: Generate LLM-based explanation
        explanation = f"[{level}] Explanation of: {summary[:50]}..."
        self.memory.save("last_explanation", explanation)
        return explanation
