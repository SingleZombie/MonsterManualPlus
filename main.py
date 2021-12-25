import tkinter as tk

from mt.interface import DisplayFrame, InputFrame


def main():
    root = tk.Tk()
    root.geometry('1024x768')

    input_frame = InputFrame(root)
    display_frame = DisplayFrame(root)

    def cal_input(event):
        p = input_frame.get_player()
        e_i = input_frame.get_extra_inputs()
        display_frame.update_content(p, e_i)

    input_frame.show_children()
    input_frame.add_enter_event(cal_input)
    input_frame.pack(side=tk.TOP)
    display_frame.show_children()
    display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20, pady=20)

    def destory_func():
        input_frame.save_inputs()
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', destory_func)
    root.mainloop()


if __name__ == '__main__':
    main()
