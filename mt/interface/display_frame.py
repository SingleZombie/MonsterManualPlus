import tkinter as tk
from tkinter.constants import LEFT
from typing import Dict

from ..game import Dule, Player
from ..game.database import display_monster, monster_dict


class DisplayFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = tk.Frame(self)
        names = [
            'name', 'life', 'atk', 'def', 'spd', 'gold', 'exp', 'cost', 'turn',
            'note'
        ]
        for name in names:
            tk.Label(self.title, text=name).pack(side=LEFT, padx=10)

        self.display_area = tk.Canvas(self, height=2000, width=2000)
        self.vscrollbar = tk.Scrollbar(self, command=self.display_area.yview)
        self.hscrollbar = tk.Scrollbar(
            self, orient='horizontal', command=self.display_area.xview)
        self.display_area.configure(
            yscrollcommand=self.vscrollbar.set,
            xscrollcommand=self.hscrollbar.set)

        self.sub_frame = tk.Frame(self.display_area)
        self.display_area.create_window((0, 0),
                                        width=2000,
                                        window=self.sub_frame,
                                        anchor='nw')

        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (self.sub_frame.winfo_reqwidth(),
                    self.sub_frame.winfo_reqheight())
            self.display_area.config(scrollregion='0 0 %s %s' % size)
            if self.sub_frame.winfo_reqwidth() != \
                    self.display_area.winfo_width():
                # update the canvas's width to fit the inner frame
                self.display_area.config(width=self.sub_frame.winfo_reqwidth())

        self.sub_frame.bind('<Configure>', _configure_interior)

        def on_configure(event):
            self.display_area.configure(
                scrollregion=self.sub_frame.bbox('all'))
            # if self.sub_frame.winfo_reqwidth() != \
            #         self.display_area.winfo_width():
            #     # update the inner frame's width to fill the canvas
            #     self.display_area.itemconfigure(
            #         id, width=self.display_area.winfo_width())

        self.display_area.bind('<Configure>', on_configure)

    def show_children(self):
        # self.title.pack(side=tk.TOP)
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.display_area.pack(side=tk.LEFT, fill=tk.X)

    def update_content(self, player: Player, extra_input: Dict):
        for child in self.sub_frame.winfo_children():
            child.destroy()

        for i, monster_name in enumerate(display_monster):
            monster = monster_dict[monster_name]

            dule = Dule(monster, player)
            dmg, turn, equip_id = dule.cal_opt_res()
            dmg_atk_1, _, _ = dule.cal_opt_res(1, 0)
            dmg_atk_2, _, _ = dule.cal_opt_res(2, 0)
            dmg_def_1, _, _ = dule.cal_opt_res(0, 1)
            dmg_def_2, _, _ = dule.cal_opt_res(0, 2)
            dmg_atk_def_1, _, _ = dule.cal_opt_res(1, 1)
            dmg_atk_def_2, _, _ = dule.cal_opt_res(2, 2)

            texts = [
                monster_name,
                f'dmg: {dmg}',
                f'turn: {turn}',
                f'equip: {equip_id}',
                f'a+1: {dmg_atk_1 - dmg}',
                f'd+1: {dmg_def_1 - dmg}',
                f'a/d+1: {dmg_atk_def_1 - dmg}',
                f'a+2: {dmg_atk_2 - dmg}',
                f'd+2: {dmg_def_2 - dmg}',
                f'a/d+2: {dmg_atk_def_2 - dmg}',
            ]

            for j, text in enumerate(texts):
                tk.Label(
                    self.sub_frame, text=text).grid(
                        row=i, column=j, padx=5)
