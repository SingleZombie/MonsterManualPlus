import tkinter as tk
from mt.game import *
from mt.interface import *


def main():
    root = tk.Tk()
    root.geometry('600x400')

    input_frame = InputFrame(root)
    display_frame = DisplayFrame(root)

    def cal_input(event):
        p = Player(1000, int(input_frame.attack_entry.get()),
                   int(input_frame.defence_entry.get()), 100, [], None, 1,
                   1000)
        display_frame.update_content(p)

    input_frame.show_children()
    input_frame.add_enter_event(cal_input)
    input_frame.pack(side=tk.TOP)
    display_frame.show_children()
    display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20, pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
