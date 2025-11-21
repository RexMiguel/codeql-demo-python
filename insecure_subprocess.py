import sys
import subprocess


def run_ping():
    if len(sys.argv) < 2:
        print("Usage: insecure_subprocess.py <host>")
        return

    host = sys.argv[1]  # untrusted user input
    cmd = f"ping -c 1 {host}"
    print(f"[DEBUG] Running: {cmd}")

    # VULNERABILITY: shell command built from user input
    subprocess.run(cmd, shell=True, check=False)


if __name__ == "__main__":
    run_ping()
