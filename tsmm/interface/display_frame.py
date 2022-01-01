import tkinter as tk
from typing import Dict

from ..game import ComplexDule, Player, SimpleDule
from ..game.database import get_monsters


class DisplayFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display_area = tk.Canvas(self, height=2000, width=2000)
        self.vscrollbar = tk.Scrollbar(self, command=self.display_area.yview)
        self.hscrollbar = tk.Scrollbar(
            self, orient='horizontal', command=self.display_area.xview)
        self.display_area.configure(
            yscrollcommand=self.vscrollbar.set,
            xscrollcommand=self.hscrollbar.set)

        self.sub_frame = tk.Frame(self.display_area)
        self.display_area.create_window((0, 0),
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
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.display_area.pack(side=tk.LEFT, fill=tk.X)

    def update_content(self, player: Player, game_style: str,
                       extra_input: Dict):
        for child in self.sub_frame.winfo_children():
            child.destroy()

        monster_names, monster_list = get_monsters()

        def process_dmg(dmg1, dmg2=''):
            if dmg2 == '':
                if dmg1 is None:
                    return '???'
                else:
                    dmg2 = 0
            if dmg1 is None or dmg2 is None:
                if dmg2 is not None:
                    return f'-{dmg2}'
                else:
                    return '???'
            else:
                return dmg1 - dmg2

        for i, monster in enumerate(monster_list):

            if game_style == 'complex':
                dule = ComplexDule(monster, player)
                dmg, turn, equip_id = dule.cal_opt_res(
                    extra_inputs=extra_input)
                dmg_atk_1, _, _ = dule.cal_opt_res(
                    1, 0, extra_inputs=extra_input)
                dmg_atk_2, _, _ = dule.cal_opt_res(
                    2, 0, extra_inputs=extra_input)
                dmg_def_1, _, _ = dule.cal_opt_res(
                    0, 1, extra_inputs=extra_input)
                dmg_def_2, _, _ = dule.cal_opt_res(
                    0, 2, extra_inputs=extra_input)
                dmg_atk_def_1, _, _ = dule.cal_opt_res(
                    1, 1, extra_inputs=extra_input)
                dmg_atk_def_2, _, _ = dule.cal_opt_res(
                    2, 2, extra_inputs=extra_input)
                dmg_atk_def_3, _, _ = dule.cal_opt_res(
                    3, 3, extra_inputs=extra_input)

                note_str = ''
                if monster.has_test:
                    test_effects = monster.test_effects
                    for effect in test_effects:
                        res = dule.cal_test_res(
                            type(effect), extra_inputs=extra_input)
                        for key, value in res.items():
                            note_str += f'{key}:{value} '
                monster_name = monster_names[i]

                texts = [
                    monster_name, f'dmg: {process_dmg(dmg)}', f'turn: {turn}',
                    f'equip: {equip_id + 1}',
                    f'a+1: {process_dmg(dmg_atk_1, dmg)}',
                    f'd+1: {process_dmg(dmg_def_1, dmg)}',
                    f'a/d+1: {process_dmg(dmg_atk_def_1, dmg)}',
                    f'a+2: {process_dmg(dmg_atk_2, dmg)}',
                    f'd+2: {process_dmg(dmg_def_2, dmg)}',
                    f'a/d+2: {process_dmg(dmg_atk_def_2, dmg)}',
                    f'a/d+3: {process_dmg(dmg_atk_def_3, dmg)}',
                    f'note: {note_str}'
                ]
            elif game_style == 'simple':
                dule = SimpleDule(monster, player)
                res_arr = dule.cal_all_res()
                res = dule
                monster_name = monster_names[i]

                threshold_note = ''
                for idx in range(len(res_arr) - 1):
                    diff, dmg, turn = res_arr[idx + 1]
                    dmg = process_dmg(res_arr[0][1], dmg)
                    threshold_note += f' ({diff}, {dmg})\t'

                texts = [
                    monster_name, f'dmg: {process_dmg(res_arr[0][1])}',
                    f'turn: {res_arr[0][2]}', f'thresholds: {threshold_note}'
                ]
            else:
                raise KeyError(game_style)

            for j, text in enumerate(texts):
                tk.Label(
                    self.sub_frame, text=text, font=('Arial', 12)).grid(
                        row=i, column=j, padx=5, sticky='w')
