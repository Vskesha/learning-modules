from tkinter import Canvas, Tk


def recursive_squares(canvas, a, b, c, d):
    """Draw recursive squares"""
    p = 2.5
    if ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 < 20:
        return
    points = []
    for p1, p2 in [(a, b), (b, c), (c, d), (d, a)]:
        canvas.create_line(p1, p2, fill='blue', width=2)
        x = (p1[0] * p + p2[0]) / (p + 1)
        y = (p1[1] * p + p2[1]) / (p + 1)
        points.append((x, y))
    recursive_squares(canvas, *points)


if __name__ == '__main__':
    size = 700
    root = Tk()
    root.geometry(f'{size}x{size}+100+100')
    root.title('recursive squares')
    canvas = Canvas(root, bg='yellow', borderwidth=1)
    canvas.pack(fill='both', expand=True)
    recursive_squares(canvas, (100, 100), (size - 100, 100), (size - 100, size - 100), (100, size - 100))
    canvas.update()
    root.mainloop()
