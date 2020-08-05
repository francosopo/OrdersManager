from cx_Freeze import setup, Executable

base = None    

executables = [Executable("GUI.py", base="Win32GUI")]

packages = ["idna","tkinter","tkinter.messagebox","tkinter.ttk","time","Arbol","Cliente","Cola","minHeap"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Organizador de Pedidos",
    options = options,
    version = "1.0",
    description = "Organiza encargos",
    executables = executables
)