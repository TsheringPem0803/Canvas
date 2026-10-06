import tkinter as tk

root = tk.Tk()
root.title("Simple House")
root.geometry("700x500")

canvas = tk.Canvas(root, width=700, height=500, bg="#BDE0FE")
canvas.pack()

# House body
canvas.create_rectangle(
    180, 230, 520, 430,
    fill="#F9C6C9",
    outline="#6D597A",
    width=4
)

# Roof
canvas.create_polygon(
    140, 230,
    350, 80,
    560, 230,
    fill="#6D597A",
    outline="#493B55",
    width=4
)

# Left window
canvas.create_rectangle(
    220, 275, 300, 345,
    fill="#A2D2FF",
    outline="#493B55",
    width=4
)

# Left window cross
canvas.create_line(260, 275, 260, 345, fill="#493B55", width=3)
canvas.create_line(220, 310, 300, 310, fill="#493B55", width=3)

# Right window
canvas.create_rectangle(
    400, 275, 480, 345,
    fill="#A2D2FF",
    outline="#493B55",
    width=4
)

# Right window cross
canvas.create_line(440, 275, 440, 345, fill="#493B55", width=3)
canvas.create_line(400, 310, 480, 310, fill="#493B55", width=3)

# Door
canvas.create_rectangle(
    305, 330, 395, 430,
    fill="#C08457",
    outline="#493B55",
    width=4
)

# Door knob
canvas.create_oval(
    375, 375, 383, 383,
    fill="#FFD166",
    outline=""
)

root.mainloop()