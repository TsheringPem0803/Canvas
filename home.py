import tkinter as tk

root = tk.Tk()
root.title("Simple House")
root.geometry("700x500")

canvas = tk.Canvas(root, width=700, height=500, bg="#BDE0FE")
canvas.pack()

# ---------------- SUN ----------------

canvas.create_oval(
    570, 40, 630, 100,
    fill="#FFD166",
    outline=""
)

# ---------------- CLOUD ----------------

canvas.create_oval(
    70, 70, 130, 105,
    fill="white",
    outline=""
)

canvas.create_oval(
    100, 50, 170, 105,
    fill="white",
    outline=""
)

canvas.create_oval(
    140, 70, 200, 105,
    fill="white",
    outline=""
)

# ---------------- HOUSE BODY ----------------

canvas.create_rectangle(
    180, 230, 520, 430,
    fill="#F9C6C9",
    outline="#6D597A",
    width=4
)

# ---------------- ROOF ----------------

canvas.create_polygon(
    140, 230,
    350, 80,
    560, 230,
    fill="#6D597A",
    outline="#493B55",
    width=4
)

# ---------------- LEFT WINDOW ----------------

canvas.create_rectangle(
    220, 275, 300, 345,
    fill="#A2D2FF",
    outline="#493B55",
    width=4
)

canvas.create_line(
    260, 275, 260, 345,
    fill="#493B55",
    width=3
)

canvas.create_line(
    220, 310, 300, 310,
    fill="#493B55",
    width=3
)

# ---------------- RIGHT WINDOW ----------------

canvas.create_rectangle(
    400, 275, 480, 345,
    fill="#A2D2FF",
    outline="#493B55",
    width=4
)

canvas.create_line(
    440, 275, 440, 345,
    fill="#493B55",
    width=3
)

canvas.create_line(
    400, 310, 480, 310,
    fill="#493B55",
    width=3
)

# ---------------- DOOR ----------------

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

# ---------------- TREE ----------------

# Tree trunk
canvas.create_rectangle(
    70, 300, 105, 430,
    fill="#9B6A45",
    outline="#6B4423",
    width=3
)

# Tree leaves
canvas.create_oval(
    30, 240, 130, 340,
    fill="#76C893",
    outline="#40916C",
    width=3
)

canvas.create_oval(
    70, 210, 170, 330,
    fill="#76C893",
    outline="#40916C",
    width=3
)

canvas.create_oval(
    100, 250, 180, 340,
    fill="#76C893",
    outline="#40916C",
    width=3
)

# ---------------- DOG HOUSE ----------------

# Dog house body
canvas.create_rectangle(
    570, 350, 670, 430,
    fill="#E9A66F",
    outline="#704214",
    width=3
)

# Dog house roof
canvas.create_polygon(
    550, 350,
    620, 290,
    690, 350,
    fill="#B56576",
    outline="#704214",
    width=3
)

# Dog house entrance
canvas.create_oval(
    600, 365, 640, 420,
    fill="#493B55",
    outline=""
)

root.mainloop()