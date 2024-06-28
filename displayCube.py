import tkinter as tk
import movements
import time

def displayCube(colorsinput, delay=0):

    color_options = ["white", "orange", "green", "red", "blue", "yellow", "black"]
    colors = colorsinput

    if isinstance(colors[0][0], int):

        for i in range(6):
            for j in range(9):
                colors[i][j] = color_options[colors[i][j]]

    scramble_result = []

    def draw_square(row, col, color, size):
        x1 = col * size
        y1 = row * size
        x2 = x1 + size
        y2 = y1 + size
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def draw_grid():
        canvas.delete("all")
        size = 40

        for i in range(3):
            for j in range(3):
                draw_square(i, j + 3, colors[0][i * 3 + j], size)

        for i in range(3):
            for j in range(3):
                draw_square(i + 3, j, colors[1][i * 3 + j], size)

        for i in range(3):
            for j in range(3):
                draw_square(i + 3, j + 3, colors[2][i * 3 + j], size)

        for i in range(3):
            for j in range(3):
                draw_square(i + 3, j + 6, colors[3][i * 3 + j], size)

        for i in range(3):
            for j in range(3):
                draw_square(i + 3, j + 9, colors[4][i * 3 + j], size)

        for i in range(3):
            for j in range(3):
                draw_square(i + 6, j + 3, colors[5][i * 3 + j], size)

    def on_click(event):
        # The code for changing color is removed to prevent color change on click.
        pass

    def on_done():
        for face_colors in colors:
            scramble_result.append(face_colors)
        root.destroy()

    root = tk.Tk()
    root.title("Ruckus Cube Viewer")

    canvas = tk.Canvas(root, width=480, height=360)
    canvas.pack()

    draw_grid()
    canvas.bind("<Button-1>", on_click)

    done_button = tk.Button(root, text="Done", command=on_done)
    done_button.pack()

    root.mainloop()

    #colours = ["white", "red", "green", "orange", "blue", "yellow", "black"]
    colours = ["white", "orange", "green", "red", "blue", "yellow", "black"]

    numberedscramble = scramble_result

    for i in range(6):
        for j in range(9):
            numberedscramble[i][j] = colours.index(scramble_result[i][j])

    return numberedscramble


if __name__ == "__main__":
    userscramble = [
    [0, 0, 0,
     0, 0, 0,
     0, 0, 0], #White
     
    [1, 1, 1,
     1, 1, 1,
     1, 1, 1], #Orange

    [2, 2, 2,
     2, 2, 2,
     2, 2, 2], #Green

    [3, 3, 3,
     3, 3, 3,
     3, 3, 3], #Red

    [4, 4, 4,
     4, 4, 4,
     4, 4, 4], #Blue

    [5, 5, 5,
     5, 5, 5,
     5, 5, 5] #Yellow
    ]
    print(displayCube(userscramble, 1))