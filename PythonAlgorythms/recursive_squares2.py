import graphics as gr

size = 700
alpha = 0.2
window = gr.GraphWin("Recursive rectangles", size, size)


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)


if __name__ == '__main__':
    fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))
    A = window.getMouse()
    for i in range(10):
        B = window.getMouse()
        gr.Line(A, B).draw(window)
        A = B
    text = gr.Text(A, 'Click to Close the Window')
    text.setSize(20)
    #text.setStyle('Arial')
    text.setTextColor('red')
    text.draw(window)
    print(window.getMouse())
