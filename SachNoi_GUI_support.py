#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jul 22, 2021 05:43:02 PM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def set_Tk_var():
    global selectedMode
    selectedMode = tk.IntVar()
    global var_cbOnePage
    var_cbOnePage = tk.IntVar()
    global var_cbMultiPagesFrom
    var_cbMultiPagesFrom = tk.IntVar()
    global var_cbMultiPagesTo
    var_cbMultiPagesTo = tk.IntVar()
    global var_rate
    var_rate = tk.IntVar()
    var_rate.set(200)
    global selectedGender
    selectedGender = tk.StringVar()
    selectedGender.set('Male')

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import SachNoi_GUI
    SachNoi_GUI.vp_start_gui()



