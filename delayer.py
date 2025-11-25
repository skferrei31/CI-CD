import subprocess
import time

def run_cmd(cmd):
    try:
        print(f"Executing: {cmd}")
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)

if __name__ == "__main__":
    # Add 100ms delay
    run_cmd("tc qdisc add dev ens3 root netem delay 100ms")

    print("Delay applied. Waiting 60 seconds...")
    time.sleep(60)

    # Remove the rule
    run_cmd("tc qdisc del dev ens3 root netem")
    print("Delay removed.")
