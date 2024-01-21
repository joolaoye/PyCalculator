import tkinter as tk
from math import *


class Calculator:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Calculator")
        self.window.configure(bg="#ffffff")
        self.window.geometry("333x241")

        self.display = tk.Text(
            self.window, width=37, height=3, borderwidth=4, bg="#4adede"
        )
        self.display.grid(row=0, column=0, columnspan=5)

        self.button_1 = tk.Button(
            self.window,
            text="1/x",
            width=8,
            command=lambda: self.click(self.button_1),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_2 = tk.Button(
            self.window,
            text="loga b",
            width=8,
            command=lambda: self.click(self.button_2),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_3 = tk.Button(
            self.window,
            text="√",
            width=8,
            command=lambda: self.click(self.button_3),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_4 = tk.Button(
            self.window,
            text="x^2",
            width=8,
            command=lambda: self.click(self.button_4),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_5 = tk.Button(
            self.window,
            text="x^n",
            width=8,
            command=lambda: self.click(self.button_5),
            bg="#404040",
            fg="#ffffff",
        )

        self.button_6 = tk.Button(
            self.window,
            text="log",
            width=8,
            command=lambda: self.click(self.button_6),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_7 = tk.Button(
            self.window,
            text="e^n",
            width=8,
            command=lambda: self.click(self.button_7),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_8 = tk.Button(
            self.window,
            text="ln",
            width=8,
            command=lambda: self.click(self.button_8),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_9 = tk.Button(
            self.window,
            text="x10^n",
            width=8,
            command=lambda: self.click(self.button_9),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_10 = tk.Button(
            self.window,
            text="π",
            width=8,
            command=lambda: self.click(self.button_10),
            bg="#404040",
            fg="#ffffff",
        )

        self.button_11 = tk.Button(
            self.window,
            text="sin",
            width=8,
            command=lambda: self.click(self.button_11),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_12 = tk.Button(
            self.window,
            text="cos",
            width=8,
            command=lambda: self.click(self.button_12),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_13 = tk.Button(
            self.window,
            text="tan",
            width=8,
            command=lambda: self.click(self.button_13),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_14 = tk.Button(
            self.window,
            text="(",
            width=8,
            command=lambda: self.click(self.button_14),
            bg="#404040",
            fg="#ffffff",
        )
        self.button_15 = tk.Button(
            self.window,
            text=")",
            width=8,
            command=lambda: self.click(self.button_15),
            bg="#404040",
            fg="#ffffff",
        )

        self.button_16 = tk.Button(
            self.window,
            text="7",
            width=8,
            command=lambda: self.click(self.button_16),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_17 = tk.Button(
            self.window,
            text="8",
            width=8,
            command=lambda: self.click(self.button_17),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_18 = tk.Button(
            self.window,
            text="9",
            width=8,
            command=lambda: self.click(self.button_18),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_19 = tk.Button(
            self.window,
            text="DEL",
            width=8,
            command=lambda: self.del_click(),
            bg="#ff6600",
        )
        self.button_20 = tk.Button(
            self.window, text="AC", width=8, command=lambda: self.clear(), bg="#ff6600"
        )

        self.button_21 = tk.Button(
            self.window,
            text="4",
            width=8,
            command=lambda: self.click(self.button_21),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_22 = tk.Button(
            self.window,
            text="5",
            width=8,
            command=lambda: self.click(self.button_22),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_23 = tk.Button(
            self.window,
            text="6",
            width=8,
            command=lambda: self.click(self.button_23),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_24 = tk.Button(
            self.window,
            text="x",
            width=8,
            command=lambda: self.click(self.button_24),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_25 = tk.Button(
            self.window,
            text="÷",
            width=8,
            command=lambda: self.click(self.button_25),
            bg="#ffffff",
            fg="#000000",
        )

        self.button_26 = tk.Button(
            self.window,
            text="1",
            width=8,
            command=lambda: self.click(self.button_26),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_27 = tk.Button(
            self.window,
            text="2",
            width=8,
            command=lambda: self.click(self.button_27),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_28 = tk.Button(
            self.window,
            text="3",
            width=8,
            command=lambda: self.click(self.button_28),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_29 = tk.Button(
            self.window,
            text="+",
            width=8,
            command=lambda: self.click(self.button_29),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_30 = tk.Button(
            self.window,
            text="-",
            width=8,
            command=lambda: self.click(self.button_30),
            bg="#ffffff",
            fg="#000000",
        )

        self.button_31 = tk.Button(
            self.window,
            text="0",
            width=8,
            command=lambda: self.click(self.button_31),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_32 = tk.Button(
            self.window,
            text=".",
            width=8,
            command=lambda: self.click(self.button_32),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_33 = tk.Button(
            self.window,
            text="Ans",
            width=8,
            command=lambda: self.click(self.button_33),
            bg="#ffffff",
            fg="#000000",
        )
        self.button_34 = tk.Button(
            self.window,
            text="=",
            width=18,
            command=lambda: self.equal(),
            bg="#ffffff",
            fg="#000000",
        )

        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_4.grid(row=1, column=3)
        self.button_5.grid(row=1, column=4)

        self.button_6.grid(row=2, column=0)
        self.button_7.grid(row=2, column=1)
        self.button_8.grid(row=2, column=2)
        self.button_9.grid(row=2, column=3)
        self.button_10.grid(row=2, column=4)

        self.button_11.grid(row=3, column=0)
        self.button_12.grid(row=3, column=1)
        self.button_13.grid(row=3, column=2)
        self.button_14.grid(row=3, column=3)
        self.button_15.grid(row=3, column=4)

        self.button_16.grid(row=4, column=0)
        self.button_17.grid(row=4, column=1)
        self.button_18.grid(row=4, column=2)
        self.button_19.grid(row=4, column=3)
        self.button_20.grid(row=4, column=4)

        self.button_21.grid(row=5, column=0)
        self.button_22.grid(row=5, column=1)
        self.button_23.grid(row=5, column=2)
        self.button_24.grid(row=5, column=3)
        self.button_25.grid(row=5, column=4)

        self.button_26.grid(row=6, column=0)
        self.button_27.grid(row=6, column=1)
        self.button_28.grid(row=6, column=2)
        self.button_29.grid(row=6, column=3)
        self.button_30.grid(row=6, column=4)

        self.button_31.grid(row=7, column=0)
        self.button_32.grid(row=7, column=1)
        self.button_33.grid(row=7, column=2)
        self.button_34.grid(row=7, column=3, columnspan=2)

        self.chars = []

        self.window.mainloop()

    def click(self, button):
        if "\n\n" in self.display.get("1.0", "end"):
            self.display.delete("1.0", "end")

        char = ""
        match button.cget("text"):
            case "log":
                char = button.cget("text") + "("
                self.display.insert(tk.END, char)
            case "cos":
                char = button.cget("text") + "("
                self.display.insert(tk.END, char)
            case "sin":
                char = button.cget("text") + "("
                self.display.insert(tk.END, char)
            case "tan":
                char = button.cget("text") + "("
                self.display.insert(tk.END, char)
            case "ln":
                char = button.cget("text") + "("
                self.display.insert(tk.END, char)
            case "x":
                char = "x"
                self.display.insert(tk.END, char)
            case "x10^n":
                char = "x10^("
                self.display.insert(tk.END, char)
            case "1/x":
                char = "1/("
                self.display.insert(tk.END, char)
            case "x^2":
                char = "^2"
                self.display.insert(tk.END, char)
            case "x^n":
                char = "^("
                self.display.insert(tk.END, char)
            case "e^n":
                char = "e^("
                self.display.insert(tk.END, char)
            case "√":
                char = "√("
                self.display.insert(tk.END, char)
            case "loga b":
                char = "log( ,"
                self.display.insert(tk.END, char)
            case _:
                char = button.cget("text")
                self.display.insert(tk.END, button.cget("text"))

        if char:
            self.chars.append(char)

    def del_click(self):
        if (
            "\n\n" in self.display.get("1.0", "end")
            or "Syntax Error" in self.display.get("1.0", "end")
            or "Math Error" in self.display.get("1.0", "end")
        ):
            self.chars.clear()
        else:
            self.chars.pop(len(self.chars) - 1)
            self.display.delete("1.0", "end")
            self.display.insert(tk.END, "".join(self.chars))

    def clear(self):
        self.chars.clear()
        self.display.delete("1.0", "end")

    def equal(self):
        self.chars.clear()
        try:
            self.answers = []
            value = self.display.get("1.0", "end")
            value = self.display.get("1.0", "end")

            if "ln" in value:
                value = value.replace("ln", "self.my_ln")
            if "^" in value:
                value = value.replace("^", "**")
            if "x" in value:
                value = value.replace("x", "*")
            if "÷" in value:
                value = value.replace("÷", "/")
            if "√" in value:
                value = value.replace("√", "sqrt")
            if "π" in value:
                value = value.replace("π", "pi")
            if "cos" in value:
                value = value.replace("cos", "self.my_cos")
            if "sin" in value:
                value = value.replace("sin", "self.my_sin")
            if "tan" in value:
                value = value.replace("tan", "self.my_tan")
            if "log" in value:
                value = value.replace("log", "self.my_log")
            if "Ans" in value:
                value = value.replace("Ans", "self.Ans")

            if value.count("(") > value.count(")"):
                value += ")" * (value.count("(") - value.count(")"))

            self.display.tag_configure("right", justify="right")
            self.display.insert(tk.END, f"\n\n{eval(value)}", "right")
            self.answers.append(eval(value))
            self.Ans = self.answers[len(self.answers) - 1]

        except ZeroDivisionError:
            self.display.delete("1.0", "end")
            self.display.insert(tk.END, "Math Error")

        except SyntaxError:
            self.display.delete("1.0", "end")
            self.display.insert(tk.END, "Math Error")

        except TypeError:
            self.display.delete("1.0", "end")
            self.display.insert(tk.END, "Math Error")

    def my_ln(self, x):
        return log(x) / log(e**1)

    def my_cos(self, x):
        return float(f"{cos(x * pi / 180):.6f}".rstrip("0").rstrip("."))

    def my_sin(self, x):
        return float(f"{sin(x * pi / 180):.6f}".rstrip("0").rstrip("."))

    def my_tan(self, x):
        return float(f"{tan(x * pi / 180):.6f}".rstrip("0").rstrip("."))

    def my_log(self, x):
        return log(x, 10)


Calculator()
