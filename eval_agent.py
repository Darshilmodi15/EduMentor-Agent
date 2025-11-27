from tools.quiz_maker import QuizMaker

class EvaluationAgent:
    def __init__(self, memory):
        self.memory = memory
        self.quiz_maker = QuizMaker()

    def generate_quiz(self, content, num_questions=5):
        quiz = self.quiz_maker.create_quiz(content, num_questions)
        self.memory.save("last_quiz", quiz)
        return quiz
