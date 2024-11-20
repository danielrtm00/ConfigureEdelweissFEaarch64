import os
import numpy as np

print("Changing version to aarch64 version ...")
print('\x1b[1;31;40m' + "!!The following file will be overwritten: linsolve.py; nonlinearimplicitstatic.py; setup.py." + '\x1b[0m')
print('\x1b[1;31;40m' + "!!The following file will be deleted: pardiso and panuapardiso." + '\x1b[0m')
print('\x1b[1;31;40m' + "Please save these files before continuing!" + '\x1b[0m')
inp = input("Are you sure [y/n]?")
if inp != "y":
    print("Process aborted.")
    quit()
os.system('cp -i linsolve.py edelweissfe/config/linsolve.py')
os.system('rm -r edelweissfe/linsolve/pardiso')
os.system('rm -r edelweissfe/linsolve/panuapardiso')

commentLines = np.arange(172,214)

with open('setup.py', 'r') as f:
    lines = f.readlines()
    count = 0
for line in lines:
    count += 1
    if count in commentLines:
        lines[count-1] = '#'+line
    else:
        lines[count-1] = line
with open('setup.py', 'w') as f:
    f.writelines(lines)

with open('edelweissfe/solvers/nonlinearimplicitstatic.py', 'r') as f:
    data = f.read()
    data = data.replace('pardiso','superlu')
with open('edelweissfe/solvers/nonlinearimplicitstatic.py', 'w') as f:
    f.write(data)