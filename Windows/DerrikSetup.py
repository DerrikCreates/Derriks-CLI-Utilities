import subprocess

pythonDependencies = ["termcolor","colorama"]

print("Installing Chocolatey")
powerShellPolicyResult = subprocess.call(
    ['powershell', 'Set-ExecutionPolicy', 'Bypass', '-Scope', 'Process', '-Force'])
if powerShellPolicyResult != 0:
    print("Failed to set power shell policy required to install chocolatey")
    quit()

chocoInstallResult = subprocess.call(['powershell',
                                      'iex',
                                      '((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))'])
if chocoInstallResult != 0:
    print("Failed to install chocolatey")
    quit()



for dep in pythonDependencies:
   depResult = subprocess.call(['pip', 'install', dep])
   if depResult != 0:
    print(f"Failed to install python dependency {dep}")

import time
from termcolor import colored

text = 'Done installing!'
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
start_time = time.time()

while time.time() - start_time < 2:
    for color in colors:
        print(colored(text, color), end='\r')
        time.sleep(0.1)
        

print(colored(text, colors[-1]))

