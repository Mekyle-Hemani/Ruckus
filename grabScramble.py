import tkinter as tk
import solve

def grabScramble():
    solution_str = None

    color_map = {
        'white': 'U',
        'red': 'R',
        'green': 'F',
        'yellow': 'D',
        'orange': 'L',
        'blue': 'B'
    }
    color_order = ['white', 'red', 'green', 'yellow', 'orange', 'blue']
    button_colors = {
        'white': '#FFFFFF',
        'red': '#FF0000',
        'green': '#00FF00',
        'yellow': '#FFFF00',
        'orange': '#FFA500',
        'blue': '#0000FF',
        'grey': '#808080'
    }
    face_indices = {
        'U': 0,
        'R': 9,
        'F': 18,
        'D': 27,
        'L': 36,
        'B': 45
    }
    centers = {
        'U': 'white',
        'R': 'red',
        'F': 'green',
        'D': 'yellow',
        'L': 'orange',
        'B': 'blue'
    }
    facelets = [''] * 54
    for face, color in centers.items():
        base = face_indices[face]
        for i in range(9):
            facelets[base + i] = color_map[color]
    
    inverse_color_map = {v: k for k, v in color_map.items()}
    fixed_centers_indices = set()
    for face, color in centers.items():
        center_index = face_indices[face] + 4
        facelets[center_index] = color_map[color]
        fixed_centers_indices.add(center_index)

    def on_facelet_click(index, button):
        if index in fixed_centers_indices:
            return
        current_color = facelets[index]
        if current_color == '':
            next_color = color_order[0]
        else:
            try:
                current_color_name = inverse_color_map[current_color]
                current_index = color_order.index(current_color_name)
                next_color = color_order[(current_index + 1) % len(color_order)]
            except (ValueError, KeyError):
                next_color = color_order[0]
        facelets[index] = color_map[next_color]
        button.config(bg=button_colors[next_color])

    def solve_cube():
        nonlocal solution_str
        cube_string = ''.join(facelets)
        solution_str = cube_string
        root.destroy()

    root = tk.Tk()
    root.title("Ruckus UI")
    face_positions_dict = {
        'U': (0, 3),
        'L': (3, 0),
        'F': (3, 3),
        'R': (3, 6),
        'B': (3, 9),
        'D': (6, 3)
    }

    for face in ['U', 'L', 'F', 'R', 'B', 'D']:
        frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
        face_pos = face_positions_dict[face]
        frame.grid(row=face_pos[0], column=face_pos[1], padx=5, pady=5)
        tk.Label(frame, text=face, font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3, pady=5)
        base = face_indices[face]
        for i in range(3):
            for j in range(3):
                index = base + i * 3 + j
                if index in fixed_centers_indices:
                    color_name = inverse_color_map[facelets[index]]
                    button = tk.Button(frame, width=4, height=2, bg=button_colors[color_name], state='disabled', bd=1, relief=tk.SUNKEN)
                else:
                    initial_color = facelets[index]
                    if initial_color:
                        color_name = inverse_color_map.get(initial_color, 'grey')
                        bg_color = button_colors.get(color_name, 'grey')
                    else:
                        bg_color = button_colors['grey']
                    button = tk.Button(frame, width=4, height=2, bg=bg_color, bd=1, relief=tk.RAISED)
                    button.config(command=lambda idx=index, btn=button: on_facelet_click(idx, btn))
                button.grid(row=i+1, column=j, padx=1, pady=1)

    solve_button = tk.Button(root, text="Solve Cube", command=solve_cube, bg='grey', font=('Arial', 12, 'bold'))
    solve_button.grid(row=9, column=3, columnspan=6, pady=20)
    root.mainloop()
    
    return solution_str

if __name__ == "__main__":
    print(solve.solve(grabScramble()))