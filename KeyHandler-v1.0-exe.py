from cx_Freeze import setup, Executable

setup(name = "keyHandler", version = "2.0", description = "hooks how many times you press keys on keyboard", executables = [Executable("KeyHandler-v2.0.py")],)