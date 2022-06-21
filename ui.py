from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_word = self.canvas.create_text(150, 125, text="Amazon acquired whole foods in 2019",
                                                   fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # false button
        self.wrong_button_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0, command=self.check_false)
        self.wrong_button.grid(row=2, column=0)

        # true button
        self.right_button_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_image, highlightthickness=0, command=self.check_true)
        self.right_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_word, text=q_text)
        else:
            if self.quiz.score < 10:
                self.canvas.itemconfig(self.canvas_word, text=f"You lost. Your total Score is {self.quiz.score}")
            else:
                self.canvas.itemconfig(self.canvas_word, text=f"You Won. Your total Score is {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
