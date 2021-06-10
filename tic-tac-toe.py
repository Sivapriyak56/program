from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from win32gui import Rectangle
from kivy.metrics import dp


class CanvasExample(Widget):
    pass
    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    #     with self.canvas:
    #         Color(1,0,0)
    #         self.rect=Line(rectangle=(self.x,self.y,100,100))

class Gridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def btn_click_first(self):
        print("first")
        with self.canvas:
            Color(1,0,0,3)
            Line(rectangle=(50, 450, 100, 100))

            Color(1, 1, 0,3)
            Line(rectangle=(350, 450, 100, 100))

    def btn_click_second(self):
        print("second")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(200,450,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(200, 150, 100, 100))

    def btn_click_third(self):
        print("third")
        with self.canvas:
            Color(1,0,0,3)
            Line(rectangle=(350,450,100,100))
            Color(1, 1, 0,3)
            Line(rectangle=(50, 450, 100, 100))

    def btn_click_four(self):
        print("four")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(50,300,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(350, 300, 100, 100))

    def btn_click_five(self):
        print("five")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(200,300,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(200, 450, 100, 100))
    def btn_click_six(self):
        print("six")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(350,300,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(350, 150, 100, 100))

    def btn_click_seven(self):
        print("seven")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(50,150,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(50, 300, 100, 100))


    def btn_click_eight(self):
        print("eigth")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(200,150,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(200, 300, 100, 100))
    def btn_click_nine(self):
        print("nine")
        with self.canvas:
            Color(1,0,0)
            Line(rectangle=(350,150,100,100))
            Color(1, 1, 0, 3)
            Line(rectangle=(50, 150, 100, 100))











class TictactoeApp(App):
    def build(self):
        pass

TictactoeApp().run()