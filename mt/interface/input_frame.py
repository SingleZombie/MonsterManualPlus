import json
import tkinter as tk

from mt.game import Player
from mt.game.database import build_monsters
from mt.game.effect import get_extra_inputs as load_extra_inputs
from mt.game.equipment import build_equipment


class InputFrame(tk.Frame):

    def __init__(self, *args, input_cfg='config/default.json', **kwargs):
        super().__init__(*args, **kwargs)
        self.config_path = input_cfg
        with open(input_cfg, 'r') as fp:
            config_dict = json.load(fp)
        self.output_cfg = config_dict
        build_monsters(config_dict['display_monster'])

        self.left_grid = tk.Frame(self)

        self.player_items = []
        for i, name in enumerate(config_dict['player_inputs']):
            descriptor = tk.Label(self.left_grid, text=f'{name}:')
            entry = tk.Entry(self.left_grid, width=5)
            self.player_items.append((descriptor, entry))
            entry.insert(0, config_dict['states'][i])

        self.extra_input_items = []
        for name, default_value in load_extra_inputs().items():
            descriptor = tk.Label(self.left_grid, text=f'{name}:')
            entry = tk.Entry(self.left_grid, width=5)
            self.extra_input_items.append((descriptor, entry))
            entry.insert(0, str(default_value))

        self.equipment_descriptor = tk.Label(
            self.left_grid, text='Equipments:')
        self.equipments_entry = tk.Entry(self.left_grid, width=20)
        self.equipment_comb_descriptor = tk.Label(
            self.left_grid, text='Equipment Combination:')
        self.equipments_comb_entry = tk.Entry(self.left_grid, width=20)
        self.equipments_entry.insert(0, ','.join(config_dict['equipments']))
        self.equipments_comb_entry.insert(0, config_dict['equi_comb'])

        self.right_frame = tk.Frame(self)
        self.enter_button = tk.Button(self.right_frame, text='Enter')

    def save_inputs(self):
        self.output_cfg['states'] = []
        for input in self.player_items:
            self.output_cfg['states'].append(input[1].get())
        self.output_cfg['equi_comb'] = self.equipments_comb_entry.get()
        self.output_cfg['equipments'] = self.equipments_entry.get().split(',')
        with open(self.config_path, 'w') as fp:
            json.dump(self.output_cfg, fp)

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
        for i, name in enumerate(load_extra_inputs()):
            res[name] = int(self.extra_input_items[i][1].get())

        return res

    def add_enter_event(self, callback):
        self.enter_button.bind('<Button-1>', callback)

    def show_children(self):
        for i, v in enumerate(self.player_items):
            descpritor, entry = v
            descpritor.grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=i, column=1, padx=10, pady=5)

        for i, v in enumerate(self.extra_input_items):
            descpritor, entry = v
            descpritor.grid(row=i, column=2, padx=10, pady=5)
            entry.grid(row=i, column=3, padx=10, pady=5)

        self.equipment_descriptor.grid(row=0, column=4, padx=10, pady=5)
        self.equipments_entry.grid(row=0, column=5, padx=10, pady=5)
        self.equipment_comb_descriptor.grid(row=1, column=4, padx=10, pady=5)
        self.equipments_comb_entry.grid(row=1, column=5, padx=10, pady=5)

        self.left_grid.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.enter_button.pack()
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)
