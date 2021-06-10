from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import random


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(),random(),random())
        with self.canvas:
            Color(*color)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clear = Button(text =" clear")
        clear.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clear)
        return parent

    def clear_canvas(self):
        return self.painter.canvas.clear()



if __name__ == '__main__':
    MyPaintApp().run()