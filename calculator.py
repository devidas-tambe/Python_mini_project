from tkinter import *

root = Tk()
root.geometry("370x450")
root.title("Calculator")

# 1. Use a StringVar to track the text on the screen
screen_var = StringVar()

# --- Functions for Logic ---

def click_button(item):
    """Adds the clicked button's text to the entry box."""
    current = screen_var.get()
    screen_var.set(current + str(item))

def clear_screen():
    """Clears the entry box."""
    screen_var.set("")

def calculate():
    """Evaluates the math expression in the entry box."""
    try:
        result = str(eval(screen_var.get()))
        screen_var.set(result)
    except Exception:
        screen_var.set("Error")

# --- UI Components ---

l = Label(root, text="SCREEN", font=("Arial", 14, "bold"), background="sky blue", 
          relief="solid", width=16, height=1, foreground="black")
l.pack(pady=5)

# 2. Link the entry box to screen_var
text2 = Entry(root, textvariable=screen_var, font=("Arial", 20), relief="solid", width=22, justify="right")
text2.place(x=20, y=40)

# --- Row 1 (C, (), %, /) ---
# Note: I've updated commands to use 'lambda' so we can pass arguments to functions
Button(root, text="C", font="bold", bg="orange", width=5, height=2, command=clear_screen).place(x=50, y=80)
Button(root, text="(", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("(")).place(x=120, y=80)
Button(root, text=")", font="bold", bg="gray", width=5, height=2, command=lambda: click_button(")")).place(x=190, y=80)
Button(root, text="/", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("/")).place(x=260, y=80)

# --- Row 2 (7, 8, 9, *) ---
Button(root, text="9", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("9")).place(x=50, y=150)
Button(root, text="8", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("8")).place(x=120, y=150)
Button(root, text="7", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("7")).place(x=190, y=150)
Button(root, text="*", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("*")).place(x=260, y=150)

# --- Row 3 (4, 5, 6, -) ---
Button(root, text="6", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("6")).place(x=50, y=220)
Button(root, text="5", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("5")).place(x=120, y=220)
Button(root, text="4", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("4")).place(x=190, y=220)
Button(root, text="-", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("-")).place(x=260, y=220)

# --- Row 4 (1, 2, 3, +) ---
Button(root, text="3", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("3")).place(x=50, y=290)
Button(root, text="2", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("2")).place(x=120, y=290)
Button(root, text="1", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("1")).place(x=190, y=290)
Button(root, text="+", font="bold", bg="gray", width=5, height=2, command=lambda: click_button("+")).place(x=260, y=290)

# --- Row 5 (0, ., =) ---
Button(root, text="0", font="bold", bg="gray", width=13, height=2, command=lambda: click_button("0")).place(x=50, y=360)
Button(root, text=".", font="bold", bg="gray", width=5, height=2, command=lambda: click_button(".")).place(x=190, y=360)
Button(root, text="=", font="bold", bg="lightgreen", width=5, height=2, command=calculate).place(x=260, y=360)

root.mainloop()