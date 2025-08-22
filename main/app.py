#!/usr/bin/env python3
"""
Python ping utility
"""

import subprocess
import sys

def ping_host(host, count=4):
    """
    Ping a host using system ping command
    """
    try:
        result = subprocess.run(
            ['ping', '-c', str(count), host],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Ping timeout"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    success, output = ping_host(host)
    
    if success:
        print(f"✅ {host} is reachable")
        print(output)
    else:
        print(f"❌ {host} is unreachable")
        print(output)

if __name__ == "__main__":
    main()
