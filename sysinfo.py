import socket
import platform
import urllib.request
import os

def get_public_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org').read().decode()
    except:
        return "Could not retrieve"

os.system('cls')
print("=" * 45)
print("        SYSTEM INFORMATION")
print("=" * 45)
print(f"Hostname:       {socket.gethostname()}")
print(f"Local IP:       {socket.gethostbyname(socket.gethostname())}")
print(f"Public IP:      {get_public_ip()}")
print(f"OS:             {platform.system()} {platform.release()}")
print(f"Version:        {platform.version()}")
print(f"Machine:        {platform.machine()}")
print(f"Processor:      {platform.processor()}")
print("=" * 45)
input("\nPress Enter to exit...")
