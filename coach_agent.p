class CoachAgent:
    def __init__(self, memory):
        self.memory = memory

    def motivate(self, topic):
        message = f"Keep going! You're doing great learning about {topic}!"
        self.memory.save("last_motivation", message)
        return message
