import tkinter as tk
from graphics import SimpleGraphics

def main():
    root = tk.Tk()
    root.title("Prosty System Graficzny")
    app = SimpleGraphics(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
