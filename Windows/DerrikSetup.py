from termcolor import colored
import time
import subprocess

pythonDependencies = ["termcolor", "colorama","validators","webp","Pillow"]
chocoDependencies = ["WebP"]

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


print("Installing python dependencies")
for dep in pythonDependencies:
    print(f"Installing {dep}")
    depResult = subprocess.call(['pip', 'install', dep])
    if depResult != 0:
        print(f"Failed to install python dependency {dep}")

print("Installing choco dependencies")
for dep in chocoDependencies:
    print(f"Installing {dep}")
    depResult = subprocess.call(['choco', 'install', dep, '-y'])
    if depResult != 0:
        print(f"Failed to install choco dependency {dep}")


text = 'Done installing!'
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
start_time = time.time()

while time.time() - start_time < 2:
    for color in colors:
        print(colored(text, color), end='\r')
        time.sleep(0.1)


print(colored(text, colors[-1]))
