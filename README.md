# LocalTunnel Auto-Serve Scripts

This contains Python scripts for automatically starting a local HTTP server and exposing it to the internet using [LocalTunnel](https://theboroer.github.io/localtunnel-www/).

## Files

### `immortal.py`

- Launches a local web server on port 8000.
- Opens a LocalTunnel with a custom subdomain (`you can change this :)`).
- Monitors the server and tunnel processes, automatically restarting them if they crash.

### `live.py`

- Starts the same local server and LocalTunnel.
- Waits for 10 seconds and checks if both processes are running.
- Kills the respective process if not detected (no automatic restart like `immortal.py`).

## Requirements

- Python(Python3 preferably)
- `localtunnel` (can be installed with `npm install -g localtunnel`)
- GNOME Terminal
- Unix-based OS (e.g., Linux)

## Usage

Make sure LocalTunnel is installed and accessible from the terminal.

Run either script using:

```bash
python3 immortal.py

sudo python3 immortal.py
