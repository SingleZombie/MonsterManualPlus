import tkinter as tk

from tsmm.utils import JsonDict

from .my_config import DEFAULT_CONFIG_PATH


class ConfigFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.descriptor = tk.Label(self, text='Game Config:')
        self.config_dict = JsonDict(DEFAULT_CONFIG_PATH)
        default_config = self.config_dict.setdefault('default_config', '')

        self.entry = tk.Entry(self, width=20)
        self.entry.insert(0, default_config)
        self.button = tk.Button(self, text='Enter')

    def has_default_path(self):
        return self.entry.get() is not None

    def save(self):
        self.config_dict['default_config'] = self.get_config()
        self.config_dict.save()

    def get_config(self):
        return self.entry.get()

    def add_enter_event(self, callback):
        self.button.bind('<Button-1>', callback)

    def show_children(self):
        self.descriptor.grid(row=0, column=0, padx=10, pady=5)
        self.entry.grid(row=0, column=1, padx=10, pady=5)
        self.button.grid(row=0, column=2, padx=50, pady=5)
