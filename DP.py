from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.config import Config
from random import randint
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("my.kv")

class MyGrid(Widget):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.question()


    Window.clearcolor = (0.94, 0.94, 0.94, 0.94)    
    sum_q = ObjectProperty(None)
    sub_q = ObjectProperty(None)
    mul_q = ObjectProperty(None)
    div_q = ObjectProperty(None)

    sum_ans = ObjectProperty(None)
    sub_ans = ObjectProperty(None)
    mul_ans = ObjectProperty(None)
    div_ans = ObjectProperty(None)

    sum_check = ObjectProperty(None)
    sub_check = ObjectProperty(None)
    mul_check = ObjectProperty(None)
    div_check = ObjectProperty(None)


    def question(self):
        self.sum_ans.text = ""
        self.sum_check.text = ""
        self.sub_ans.text = ""
        self.sub_check.text = ""
        self.mul_ans.text = ""
        self.mul_check.text = ""
        self.div_ans.text = ""
        self.div_check.text = ""
        # Sum
        n1 = randint(1,100)
        n2 = randint(1,100)
        self.sum = n1 + n2
        self.sum_q.text = f"{n1} + {n2}"
        
        # Subtart
        n1 = randint(1,100)
        n2 = randint(1,n1)
        self.sub = n1 - n2
        self.sub_q.text = f"{n1} - {n2}"
        
        # Multiplication
        n1 = randint(1,100)
        n2 = randint(1,100)
        self.mul = n1 * n2
        self.mul_q.text = f"{n1} x {n2}"

        # Division
        n2 = randint(1,100)
        self.div = randint(1,20)
        n1 = n2 * self.div
        self.div_q.text = f"{n1} / {n2}"


    def check(self):
        try:
            if self.sum == int(self.sum_ans.text):
                self.sum_check.text = "Well done"
            else:
                self.sum_check.text = "Please try again"
        except:
            self.sum_check.text = "Please try again"
        
        try:
            if self.sub == int(self.sub_ans.text):
                self.sub_check.text = "Well done"
            else:
                self.sub_check.text = "Please try again"
        except:
            self.sub_check.text = "Please try again"
        
        try:
            if self.mul == int(self.mul_ans.text):
                self.mul_check.text = "Well done"
            else:
                self.mul_check.text = "Please try again"
        except:
            self.mul_check.text = "Please try again"
        
        try:
            if self.div == int(self.div_ans.text):
                self.div_check.text = "Well done"
            else:
                self.div_check.text = "Please try again"
        except:
            self.div_check.text = "Please try again"


class MyApp(App):  
    def build(self):
        self.title = "Daily Practice"
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
