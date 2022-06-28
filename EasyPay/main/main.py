import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from business.control.SystemControl import SystemControl
from business.command.Prompt import Prompt
from view.home import home_view

system = SystemControl()
system.start()
Prompt(home_view)
system.end()




