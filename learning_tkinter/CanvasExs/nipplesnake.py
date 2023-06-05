import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW


class Cons:
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 500
    DOT_SIZE = 10
    MAX_RAND_POS = 27


class Board(Canvas):

    def __init__(self):
        super().__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT, background='blue', highlightthickness=0)
        self.init_game()
        self.pack()

    def init_game(self):
        self.in_game = True
        self.dots = 3
        self.score = 0
        self.move_x = Cons.DOT_SIZE
        self.move_y = 0
        self.apple_x = 100
        self.apple_y = 190
        self.load_images()
        self.create_objects()
        self.locate_apple()
        self.bind_all('<Key>', self.on_key_pressed)
        self.after(Cons.DELAY, self.on_timer)

    def load_images(self):
        try:
            self.idot = Image.open('dot.png')
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open('head.png')
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open('apple.png')
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError as e:
            print(e)
            sys.exit(1)

    def create_objects(self):
        self.create_text(30, 10, text='Score: {0}'.format(self.score), tag='score', fill='white')
        self.create_image(self.apple_x, self.apple_y, image=self.apple, anchor=NW, tag='apple')
        self.create_image(50, 50, image=self.head, anchor=NW, tag='head')
        self.create_image(30, 50, image=self.dot, anchor=NW, tag='dot')
        self.create_image(40, 50, image=self.dot, anchor=NW, tag='dot')

    def locate_apple(self):
        apple = self.find_withtag('apple')
        self.delete(apple[0])
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_x = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_y = r * Cons.DOT_SIZE
        self.create_image(self.apple_x, self.apple_y, image=self.apple, anchor=NW, tag='apple')

    def on_key_pressed(self, event):
        key = event.keysym
        LEFT_CURSOR_KEY = 'Left'
        if key == LEFT_CURSOR_KEY and self.move_x <=0:
            self.move_x = -Cons.DOT_SIZE
            self.move_y = 0

        RIGHT_CURSOR_KEY = 'Right'
        if key == RIGHT_CURSOR_KEY and self.move_x >= 0:
            self.move_x = Cons.DOT_SIZE
            self.move_y = 0

        UP_CURSOR_KEY = 'Up'
        if key == UP_CURSOR_KEY and self.move_y <= 0:
            self.move_x = 0
            self.move_y = -Cons.DOT_SIZE

        DOWN_CURSOR_KEY = 'Down'
        if key == DOWN_CURSOR_KEY and self.move_y >= 0:
            self.move_x = 0
            self.move_y = Cons.DOT_SIZE

    def on_timer(self):
        self.draw_score()
        self.check_collision()
        if self.in_game:
            self.check_apple_collision()
            self.move_snake()
            self.after(Cons.DELAY, self.on_timer)
        else:
            self.game_over()

    def draw_score(self):
        score = self.find_withtag('score')
        self.itemconfigure(score, text='Score: {0}'.format(self.score))

    def check_collision(self):
        dots = self.find_withtag('dot')
        head = self.find_withtag('head')
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for dot in dots:
            for over in overlap:
                if over == dot:
                    self.in_game = False

        if x1 < 0 or x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.in_game = False

        if y1 < 0 or y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
            self.in_game = False

    def check_apple_collision(self):
        apple = self.find_withtag('apple')
        head = self.find_withtag('head')

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:
            if apple[0] == ovr:
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dot, anchor=NW, tag='dot')
                self.locate_apple()

    def move_snake(self):
        dots = self.find_withtag('dot')
        head = self.find_withtag('head')
        items = dots + head
        z = 0
        while z < len(items) - 1:
            c1 = self.coords(items[z])
            c2 = self.coords(items[z+1])
            self.move(items[z], c2[0] - c1[0], c2[1] - c1[1])
            z += 1

        self.move(head, self.move_x, self.move_y)

    def game_over(self):
        self.delete(ALL)
        self.create_text(
            self.winfo_width()/2, self.winfo_height()/2,
            text='GAME OVER. Score: {0}'.format(self.score), fill='white'
        )


class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Snake by Vs')
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    nib = Snake()
    root.mainloop()


if __name__ == '__main__':
    main()
