from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


# This class is responsible for creating the user interface for the quiz game using tkinter
class QuizInterface:
    # Creates the layout of the app
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text='Question goes here',
                                                     font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.change = self.canvas.config(bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.check_right)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.check_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    # Taps into the quiz_brain and calls the next_question method
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz!\nYour final score is"
                                        f" {self.quiz.score}/{self.quiz.question_number}")

#  Picks Right or Wrong and gives feedback
    def check_right(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def check_wrong(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

