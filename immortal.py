import subprocess
import time
import os
import signal

def start_lt():
    return subprocess.Popen(
        ['gnome-terminal', '--', 'bash', '-c', 'lt --port 8000 --subdomain vani-lmao']
    )

def start_http_server():
    return subprocess.Popen(
        ['gnome-terminal', '--', 'bash', '-c', 'python3 -m http.server 8000']
    )

print("Starting webpage on http://localhost:8000")
print("Opening LocalTunnel at https://sitename.loca.lt ...")

lt_process = start_lt()
http_server_process = start_http_server()

while True:
    time.sleep(10)

    if lt_process.poll() is not None:
        print("LocalTunnel process not detected, killing terminal and restarting.")
        os.kill(lt_process.pid, signal.SIGTERM)
        lt_process = start_lt()

    if http_server_process.poll() is not None:
        print("HTTP server process not detected, killing terminal and restarting.")
        os.kill(http_server_process.pid, signal.SIGTERM)
        http_server_process = start_http_server()
