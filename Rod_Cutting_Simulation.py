import tkinter as tk
from tkinter import messagebox

def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            if j <= len(prices):
                if max_val < prices[j - 1] + dp[i - j]:
                    max_val = prices[j - 1] + dp[i - j]
                    cuts[i] = j
        dp[i] = max_val

    result_cuts = []
    length = n
    while length > 0:
        result_cuts.append(cuts[length])
        length -= cuts[length]

    return dp[n], result_cuts

def calculate():
    try:
        prices = list(map(int, price_entry.get().split()))
        rod_length = int(length_entry.get())

        if rod_length <= 0 or not prices:
            raise ValueError

        max_profit, cut_list = rod_cutting(prices, rod_length)

        result_text.set(f"Max Profit: {max_profit}\nCut Sizes: {cut_list}")

        draw_visual(cut_list, rod_length)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")

def draw_visual(cuts, rod_length):
    canvas.delete("all")
    x = 10
    canvas_width = 500
    scale = canvas_width / rod_length

    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]

    for i, cut in enumerate(cuts):
        width = cut * scale
        canvas.create_rectangle(x, 20, x + width, 70, fill=colors[i % len(colors)])
        canvas.create_text(x + width / 2, 45, text=str(cut), fill="black", font=('Arial', 12, 'bold'))
        x += width

# GUI Setup
app = tk.Tk()
app.title("Rod Cutting Simulation")
app.geometry("600x300")

tk.Label(app, text="Enter prices for lengths (space-separated):").pack()
price_entry = tk.Entry(app, width=50)
price_entry.pack()

tk.Label(app, text="Enter rod length:").pack()
length_entry = tk.Entry(app, width=10)
length_entry.pack()

tk.Button(app, text="Calculate Optimal Cuts", command=calculate).pack(pady=10)

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, font=('Arial', 12), fg="blue").pack()

canvas = tk.Canvas(app, width=500, height=100, bg="white")
canvas.pack(pady=10)

app.mainloop()
