import tkinter as tk

from .config_frame import ConfigFrame
from .display_frame import DisplayFrame
from .input_frame import InputFrame


class MainWindow(tk.Tk):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.config_frame = ConfigFrame()
        self.input_frame: InputFrame = None
        self.display_frame: DisplayFrame = None
        self.config_frame.add_enter_event(self.build_frames)
        self.config_frame.show_children()
        self.config_frame.pack(side=tk.TOP)
        if self.config_frame.has_default_path():
            try:
                self.build_frames(None)
            except Exception:
                print('The config is not valid')
        self.protocol('WM_DELETE_WINDOW', self.destory_func)

    def build_frames(self, event):
        for frame in [self.input_frame, self.display_frame]:
            if frame is not None:
                frame.destory()

        self.input_frame = InputFrame(input_cfg=self.config_frame.get_config())
        self.display_frame = DisplayFrame()
        game_style = self.input_frame.get_game_style()

        def cal_input(event):
            p = self.input_frame.get_player()
            e_i = self.input_frame.get_extra_inputs()
            self.display_frame.update_content(p, game_style, e_i)

        self.input_frame.show_children()
        self.input_frame.add_enter_event(cal_input)
        self.input_frame.pack(side=tk.TOP)
        self.display_frame.show_children()
        self.display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20)

    def destory_func(self):
        self.config_frame.save()
        if self.input_frame:
            self.input_frame.save_inputs()
        if self.display_frame:
            self.display_frame.save()
        self.destroy()
