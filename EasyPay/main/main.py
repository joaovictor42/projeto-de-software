import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from business.control.SystemControl import SystemControl
from view.home import home_view

system = SystemControl()
system.start()
system.prompt(home_view)
system.end()




