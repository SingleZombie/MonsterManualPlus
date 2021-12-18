import tkinter as tk

from mt.game import Player
from mt.game.database import default_equipments
from mt.game.effect import extra_inputs
from mt.game.equipment import build_equipment

player_inputs = ['Attack', 'Defence', 'HP', 'MAX HP', 'Level']


class InputFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.left_grid = tk.Frame(self)

        self.player_items = []
        for name in player_inputs:
            descriptor = tk.Label(self.left_grid, text=f'{name}:')
            entry = tk.Entry(self.left_grid)
            self.player_items.append((descriptor, entry))

        self.extra_input_items = []
        for name in extra_inputs:
            descriptor = tk.Label(self.left_grid, text=f'{name}:')
            entry = tk.Entry(self.left_grid)
            self.extra_input_items.append((descriptor, entry))

        self.equipment_descriptor = tk.Label(
            self.left_grid, text='Equipments:')
        self.equipments_entry = tk.Entry(self.left_grid)
        self.equipment_comb_descriptor = tk.Label(
            self.left_grid, text='Equipment Combination:')
        self.equipments_comb_entry = tk.Entry(
            self.left_grid, text=','.join(default_equipments))

        self.right_frame = tk.Frame(self)
        self.enter_button = tk.Button(self.right_frame, text='Enter')

    def get_player(self):
        equi_names = self.equipments_entry.get().split(',')
        equis = [build_equipment(x) for x in equi_names]
        combs_list = eval(self.equipments_comb_entry.get())
        eq_list = [[equis[idx] for idx in ls] for ls in combs_list]
        p = Player(
            life=int(self.player_items[2][1].get()),
            attack=int(self.player_items[0][1].get()),
            defence=int(self.player_items[1][1].get()),
            life_max=int(self.player_items[3][1].get()),
            level=int(self.player_items[4][1].get()),
            speed=100,
            effects=[],
            equipment_set_list=eq_list)
        return p

    def get_extra_inputs(self):
        res = {}
        for i, name in enumerate(extra_inputs):
            res[name] = int(self.extra_input_items[i][1].get())

        return res

    def add_enter_event(self, callback):
        self.enter_button.bind('<Button-1>', callback)

    def show_children(self):
        for i, v in enumerate(self.player_items):
            descpritor, entry = v
            descpritor.grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=0, column=1, padx=10, pady=5)

        for i, v in enumerate(self.extra_input_items):
            descpritor, entry = v
            descpritor.grid(row=i, column=2, padx=10, pady=5)
            entry.grid(row=0, column=3, padx=10, pady=5)

        self.equipment_descriptor.grid(row=0, column=4, padx=10, pady=5)
        self.equipments_entry.grid(row=0, column=5, padx=10, pady=5)
        self.equipment_comb_descriptor.grid(row=1, column=4, padx=10, pady=5)
        self.equipments_comb_entry.grid(row=1, column=5, padx=10, pady=5)

        self.left_grid.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.enter_button.pack()
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)
