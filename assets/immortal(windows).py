import subprocess
import time
import os
import signal
import platform

def start_lt():
    os_name = platform.system()
    if os_name == "Windows":
        return subprocess.Popen(
            ['start', 'cmd', '/c', 'lt --port 8000 --subdomain testsite'],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        return subprocess.Popen(
            ['gnome-terminal', '--', 'bash', '-c', 'lt --port 8000 --subdomain testsite']
        )

def start_http_server():
    os_name = platform.system()
    if os_name == "Windows":
        return subprocess.Popen(
            ['start', 'cmd', '/c', 'python -m http.server 8000'],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        return subprocess.Popen(
            ['gnome-terminal', '--', 'bash', '-c', 'python3 -m http.server 8000']
        )

print("Starting webpage on http://localhost:8000")
print("Opening LocalTunnel at https://testsite.loca.lt ...")

lt_process = start_lt()
http_server_process = start_http_server()

while True:
    time.sleep(10)

    if lt_process and lt_process.poll() is not None:
        print("LocalTunnel process not detected, killing terminal and restarting.")
        if platform.system() == "Windows" and lt_process.pid:
            subprocess.call(['taskkill', '/F', '/PID', str(lt_process.pid)])
        elif lt_process.pid:
            os.kill(lt_process.pid, signal.SIGTERM)
        lt_process = start_lt()

    if http_server_process and http_server_process.poll() is not None:
        print("HTTP server process not detected, killing terminal and restarting.")
        if platform.system() == "Windows" and http_server_process.pid:
            subprocess.call(['taskkill', '/F', '/PID', str(http_server_process.pid)])
        elif http_server_process.pid:
            os.kill(http_server_process.pid, signal.SIGTERM)
        http_server_process = start_http_server()
