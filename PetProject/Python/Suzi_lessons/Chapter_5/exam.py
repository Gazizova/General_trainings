from random import choice

class Student:
    def __init__(self):
        self.name = input("What is your name?")
    def listen(self, message):
        print(self.name + " " + message)
    def answer_question(self, question):
        print(question)
        answer = input("Your variant is:  ")
        return answer

class Exam:
    def __init__(self, test):
        self._test = test
    def test_skills(self, student):
        student.listen("answer in the question")
        sum = 0
        total = 0
        for question in self._test:
            total = total+1
            if question.check_answer(student.answer_question(question)):
                sum = sum+1
        return Mark(sum,  total)

class Test:
    def __init__(self, questions, number = 0):
        self._number = number or len(questions)
        self.Pick(questions)
    def __len__(self):
        return len(self.questions)
    def __getitem__(self, n):
        return self._questions[n]
    def Pick(self, questions):

        self._questions = []
        for i in range(self._number):
            picked = choice(questions)
            self._questions.append(picked)
            questions.remove(picked)

class Question:
    def __init__(self, text, answers, right_answer):
        self._text = text
        self._answers = answers
        self._right_answer = right_answer
    def __str__(self):
        text = str(self._text)
        num = 0
        for a in self._answers:
            num = num+1
            text = """%(text)s\n%(num)s. %(a)s""" % vars()
        return text
    def check_answer(self, given_answer):
        return self._right_answer == given_answer

class Mark:
    mark_names = {2: "not good", 3: "not bad", 4:"very good", 5: "perfect"}
    def __init__(self, answered, total):
        self._mark = max(2, answered *5/total)
    def __str__(self):
        return (self.mark_names[self._mark])

def module_test():
    test = Test([
        Question("2*2 = ", ["2", "22", "4", "5"], "3"),
        Question("7*7 = ", ["77", "49", "14", "23"], "2")
    ])
    student = Student()
    exam = Exam(test)
    mark = exam.test_skills(student)
    print(mark)

if __name__=="__main__":
    module_test()