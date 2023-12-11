import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry('800x600')

        self.data = []
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.generate_button = ttk.Button(root, text="Generate Data", command=self.generate_data)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        self.bubble_sort_button = ttk.Button(root, text="Bubble Sort", command=self.bubble_sort)
        self.bubble_sort_button.pack(side=tk.LEFT, padx=10)

        self.selection_sort_button = ttk.Button(root, text="Selection Sort", command=self.selection_sort)
        self.selection_sort_button.pack(side=tk.LEFT, padx=10)

        self.merge_sort_button = ttk.Button(root, text="Merge Sort", command=self.merge_sort)
        self.merge_sort_button.pack(side=tk.LEFT, padx=10)

        self.quick_sort_button = ttk.Button(root, text="Quick Sort", command=self.quick_sort)
        self.quick_sort_button.pack(side=tk.LEFT, padx=10)

    def generate_data(self):
        self.data = random.sample(range(1, 101), 10)  # Generate a random list of 10 numbers
        self.update_plot()

    def update_plot(self, delay=500):
        self.ax.clear()
        self.ax.bar(range(len(self.data)), self.data, color='blue')
        self.canvas.draw()
        self.root.after(delay, self.root.update_idletasks)


    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    self.update_plot(delay=50)  # Decreased delay for smoother animationihififihadifhadihaif
                    self.root.update_idletasks()

    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.update_plot(delay=50)  # Decreased delay for smoother animation
            self.root.update_idletasks()

    def merge_sort(self):
        # Implement merge sort logic here
        pass

    def quick_sort(self):
        # Implement quicksort logic here
        pass

def main():
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
