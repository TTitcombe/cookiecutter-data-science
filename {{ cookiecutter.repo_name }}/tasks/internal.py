from shutil import which
import os


# Configure cross-platform settings
shell = which("bash") if os.name != "nt" else which("cmd")
pty = False if os.name == "nt" else True
