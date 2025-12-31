import tkinter as tk
import math

def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(float(entry.get())))

def cbrt():
    entry.delete(0, tk.END)
    entry.insert(0, float(entry.get()) ** (1/3))

def log():
    entry.delete(0, tk.END)
    entry.insert(0, math.log10(float(entry.get())))

def ln():
    entry.delete(0, tk.END)
    entry.insert(0, math.log(float(entry.get())))

def trig(func):
    value = math.radians(float(entry.get()))
    if func == "sin":
        res = math.sin(value)
    elif func == "cos":
        res = math.cos(value)
    elif func == "tan":
        res = math.tan(value)
    entry.delete(0, tk.END)
    entry.insert(0, res)

def square():
    entry.delete(0, tk.END)
    entry.insert(0, float(entry.get()) ** 2)

def area_circle():
    r = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.pi * r * r)

def perimeter_circle():
    r = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, 2 * math.pi * r)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black", padx=10, pady=10)
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Arial", 26),
    bg="white",
    fg="black",
    bd=8,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, pady=15, ipady=12)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r = 1
c = 0
for b in buttons:
    cmd = calc if b == "=" else lambda x=b: click(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        width=8,
        height=3,
        font=("Arial", 14, "bold"),
        bg="yellow" if b in "+-*/=" else "gray"
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(
    root, text="⌫", command=backspace,
    width=8, height=3, font=("Arial", 12),
    bg="orange"
).grid(row=r, column=0, padx=6, pady=6)

tk.Button(
    root, text="C", command=clear,
    width=8, height=3, font=("Arial", 12),
    bg="red", fg="white"
).grid(row=r, column=1, padx=6, pady=6)

tk.Button(
    root, text="//", command=lambda: click("//"),
    width=8, height=3, font=("Arial", 12)
).grid(row=r, column=2, padx=6, pady=6)

tk.Button(
    root, text="^", command=lambda: click("**"),
    width=8, height=3, font=("Arial", 12)
).grid(row=r, column=3, padx=6, pady=6)

r += 1
tk.Button(root, text="√", command=sqrt, width=8, height=3).grid(row=r, column=0, padx=6, pady=6)
tk.Button(root, text="∛", command=cbrt, width=8, height=3).grid(row=r, column=1, padx=6, pady=6)
tk.Button(root, text="x²", command=square, width=8, height=3).grid(row=r, column=2, padx=6, pady=6)
tk.Button(root, text="log", command=log, width=8, height=3).grid(row=r, column=3, padx=6, pady=6)

r += 1
tk.Button(root, text="sin", command=lambda: trig("sin"), width=8, height=3).grid(row=r, column=0, padx=6, pady=6)
tk.Button(root, text="cos", command=lambda: trig("cos"), width=8, height=3).grid(row=r, column=1, padx=6, pady=6)
tk.Button(root, text="tan", command=lambda: trig("tan"), width=8, height=3).grid(row=r, column=2, padx=6, pady=6)
tk.Button(root, text="ln", command=ln, width=8, height=3).grid(row=r, column=3, padx=6, pady=6)

r += 1
tk.Button(root, text="Area", command=area_circle,
          width=17, height=3).grid(row=r, column=0, columnspan=2, padx=6, pady=6)

tk.Button(root, text="Perimeter", command=perimeter_circle,
          width=17, height=3).grid(row=r, column=2, columnspan=2, padx=6, pady=6)

root.mainloop()
