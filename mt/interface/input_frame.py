import tkinter as tk


class InputFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.left_grid = tk.Frame(self)
        self.attack_descriptor = tk.Label(self.left_grid, text='Attack:')
        self.attack_entry = tk.Entry(self.left_grid)
        self.defence_descriptor = tk.Label(self.left_grid, text='Defence:')
        self.defence_entry = tk.Entry(self.left_grid)
        self.equipment_descriptor = tk.Label(
            self.left_grid, text='Equipments:')
        self.equipments_entry = tk.Entry(self.left_grid)
        self.right_frame = tk.Frame(self)
        self.enter_button = tk.Button(self.right_frame, text='Enter')

    def add_enter_event(self, callback):
        self.enter_button.bind('<Button-1>', callback)

    def show_children(self):
        self.attack_descriptor.grid(row=0, column=0, padx=10, pady=5)
        self.attack_entry.grid(row=0, column=1, padx=10, pady=5)
        self.defence_descriptor.grid(row=1, column=0, padx=10, pady=5)
        self.defence_entry.grid(row=1, column=1, padx=10, pady=5)
        self.equipment_descriptor.grid(row=0, column=2, padx=10, pady=5)
        self.equipments_entry.grid(row=0, column=3, padx=10, pady=5)
        self.left_grid.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.enter_button.pack()
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)
