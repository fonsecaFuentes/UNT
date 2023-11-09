import threading
import sys
# import os
import subprocess
from pathlib import Path

theproc = ''

root = Path(__file__).resolve().parent
route_server = root / 'server' / 'up_server.py'
print(route_server)


def try_connection():

    if theproc != '':
        theproc.kill()
        threading.Thread(
            target=launch_server, args=(True, ), daemon=True
        ).start()
    else:
        threading.Thread(
            target=launch_server, args=(True, ), daemon=True
        ).start()


def launch_server(var):

    the_path = route_server

    if var:
        global theproc
        theproc = subprocess.Popen([sys.executable, the_path])
        theproc.communicate()
    else:
        print('')


def stop_server():

    global theproc
    if theproc != '':
        theproc.kill()
