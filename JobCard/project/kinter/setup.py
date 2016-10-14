import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable('BitCoins.py', base=base, icon='btc.ico')]

cx_Freeze.setup(
    name="Bit Coin The app",
    options={"build_exe": {"packages": ["tkinter","matplotlib"], "include_files": ["btc.ico"]}},
    version="0.01",
    description=" The Bit Coin App",
    executables=executables
    )

