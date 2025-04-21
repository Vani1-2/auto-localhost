![Screenshot from 2025-04-21 19-46-56](https://github.com/user-attachments/assets/5b772ab6-bb14-4856-8715-058028e532ca)
# Local Tunnel Launcher Script

This Python script is designed to simplify the process of exposing a local web server to the internet using LocalTunnel. It automatically starts both the local HTTP server and the LocalTunnel client, and it monitors these processes, restarting them if they crash.

## Features

* **Automatic Server Setup:** Starts a local HTTP server on port 8000 using Python's built-in `http.server` module.
* **LocalTunnel Integration:** Launches a LocalTunnel client to create a publicly accessible URL for your local server.
* **Process Monitoring:** Continuously monitors both the HTTP server and LocalTunnel processes. If either process terminates unexpectedly, the script automatically restarts it.
* **Cross-Platform Compatibility:** Works on both Linux (using `gnome-terminal`) and Windows (using `cmd.exe`).

## Prerequisites

Before using this script, ensure you have the following installed:

* **Python 3:** The script requires Python 3 to run the HTTP server.
* **LocalTunnel:** Install LocalTunnel globally using npm:

    ```bash
    npm install -g localtunnel
    ```

* **Windows Users:** Ensure that Node.js and npm are installed, and that `lt` is available in your system's PATH (Only the `immortal.py` is avaible).

## Usage

1.  Save the Python script. ( For windows users, download the windows version of immortal.py).
2.  Open a terminal or command prompt in the directory where you saved the script. (Alternatively you can place the script in the same directory where your HTML files are located. This will allow the script to serve those files.)
3.  Run any of the script, example:

    ```bash
    python3 immortal.py
    ```

The script will:

* Start the local HTTP server.
* Start LocalTunnel, providing you with a public URL `https://testsite.loca.lt` (You can change the sitename in the code ._.)
* Keep both processes running.  If either process crashes, the script will restart it (Depends on what script you're using).

## Important Notes

* This script assumes that `lt` is in your system's PATH. If it's not, you may need to provide the full path to the `lt` executable in the script.
* The script uses port 8000 for the HTTP server and the subdomain "testsite" for LocalTunnel. You can modify these values by editing the script.
* Windows users may encounter firewall issues. Ensure that your firewall allows connections for Python and LocalTunnel.


