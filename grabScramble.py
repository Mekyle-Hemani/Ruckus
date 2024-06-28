import tkinter as tk

def grabscramble():
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
        size = 40
        row = event.y // size
        col = event.x // size

        face = None
        index = None

        if 0 <= row < 3 and 3 <= col < 6:
            face = 0
            index = row * 3 + (col - 3)
        elif 3 <= row < 6:
            if 0 <= col < 3:
                face = 1
                index = (row - 3) * 3 + col
            elif 3 <= col < 6:
                face = 2
                index = (row - 3) * 3 + (col - 3)
            elif 6 <= col < 9:
                face = 3
                index = (row - 3) * 3 + (col - 6)
            elif 9 <= col < 12:
                face = 4
                index = (row - 3) * 3 + (col - 9)
        elif 6 <= row < 9 and 3 <= col < 6:
            face = 5
            index = (row - 6) * 3 + (col - 3)

        if face is not None and index is not None and index != 4:
            current_color = colors[face][index]
            next_color_index = (color_options.index(current_color) + 1) % len(color_options)
            colors[face][index] = color_options[next_color_index]
            draw_grid()

    def on_done():
        for face_colors in colors:
            scramble_result.append(face_colors)
        root.destroy()

    root = tk.Tk()
    root.title("Ruckus Scramble Input")

    color_options = ["red", "white", "blue", "green", "yellow", "orange"]
    colors = [
        ["white", "white", "white", "white", "white", "white", "white", "white", "white"],
        ["orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange"],
        ["green", "green", "green", "green", "green", "green", "green", "green", "green"],
        ["red", "red", "red", "red", "red", "red", "red", "red", "red"],
        ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"],
        ["yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]
    ]

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
    #return

if __name__ == "__main__":
    print(grabscramble())