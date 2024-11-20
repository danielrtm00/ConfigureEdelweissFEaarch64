import os

print("Changing version to x86_64 version ...")
print('\x1b[1;31;40m' + "!!The following files will be restored to the last commit." + '\x1b[0m')
print('\x1b[1;31;40m' + "!!linsolve.py, setup.py, nonlinearimplicitstatic.py, folders pardiso and panuapardiso" + '\x1b[0m')
print('\x1b[1;31;40m' + "Please save these files before continuing!" + '\x1b[0m')
inp = input("Are you sure [y/n]?")
if inp != "y":
    print("Process aborted.")
    quit()
os.system('git restore edelweissfe/config/linsolve.py')
os.system('git restore edelweissfe/linsolve/panuapardiso/__init__.py')
os.system('git restore edelweissfe/linsolve/panuapardiso/panuapardiso.pyx')
os.system('git restore edelweissfe/linsolve/pardiso/__init__.py')
os.system('git restore edelweissfe/linsolve/pardiso/pardiso.pyx')
os.system('git restore edelweissfe/linsolve/pardiso/__init__.py')
os.system('git restore edelweissfe/solvers/nonlinearimplicitstatic.py')
os.system('git restore setup.py')
print("Done!")