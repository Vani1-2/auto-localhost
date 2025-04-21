import subprocess
import time
import os
import signal

print("Starting webpage on http://localhost:8000")
print("Opening LocalTunnel at https://vani-lmao.loca.lt ...")

lt_process = subprocess.Popen(
    ['gnome-terminal', '--', 'bash', '-c', 'lt --port 8000 --subdomain vani-lmao']
)

http_server_process = subprocess.Popen(
    ['gnome-terminal', '--', 'bash', '-c', 'python3 -m http.server 8000']
)

time.sleep(10)

if lt_process.poll() is not None:
    print("LocalTunnel process not detected, killing terminal.")
    if lt_process.poll() is not None:  
        os.kill(lt_process.pid, signal.SIGTERM)

if http_server_process.poll() is not None:
    print("HTTP server process not detected, killing terminal.")
    if http_server_process.poll() is not None:  
        os.kill(http_server_process.pid, signal.SIGTERM)
