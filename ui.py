from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")

class QuizInterface:

    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.questionText = self.canvas.create_text(150, 125, text="TEST TEXT", font=FONT, width=290)

        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)
        # Score label
        self.scoreLabel = Label(text=f"Score: {self.quiz.score}", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(column=1, row=0, padx=20, pady=20)

        # True button
        trueButtonImg = PhotoImage(file="./images/true.png")
        self.trueButton = Button(image=trueButtonImg, highlightthickness=0, command=self.trueButtonClick,
                                 bd=0, activebackground=THEME_COLOR)
        self.trueButton.grid(column=0, row=2, padx=20, pady=20)

        # False button
        falseButtonImg = PhotoImage(file="./images/false.png")
        self.falseButton = Button(image=falseButtonImg, highlightthickness=0, command=self.falseButtonClick,
                                  bd=0, activebackground=THEME_COLOR)
        self.falseButton.grid(column=1, row=2, padx=20, pady=20)

        self.getNextQuestion()

        self.window.update()
        self.window.minsize(self.window.winfo_width(), self.window.winfo_height())
        self.window.maxsize(self.window.winfo_width(), self.window.winfo_height())

        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg="white")
        self.scoreLabel.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            rawQuestionText = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=rawQuestionText)
            self.trueButton.config(state="normal")
            self.falseButton.config(state="normal")
        else:
            self.canvas.itemconfig(self.questionText, fill="green", text=f"You've reached the end!\n"
                                                           f"Your final score: "
                                                           f"{self.quiz.score}/{self.quiz.question_number}")

    def trueButtonClick(self):
        self.feedback(self.quiz.check_answer("True"))

    def falseButtonClick(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, correct):
        self.trueButton.config(state="disabled")
        self.falseButton.config(state="disabled")
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getNextQuestion)
