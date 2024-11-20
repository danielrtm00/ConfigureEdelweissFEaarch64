This repository can be used to configure https://github.com/EdelweissFE/EdelweissFE for use on aarch64 CPU.

EdelweissFE aarch64 configurator
--------------------------------

USE WITH CARE!

Triggering the configuration will change the following files:
edelweissfe/config/linsolve.py 						(will change the file to the version as of 20th November 2024)
edelweissfe/linsolve/pardiso 						(will get deleted)
edelweissfe/linsolve/panuapardiso 					(will get deleted)
edelweissfe/solvers/nonlinearimplicitstatic.py 	(changes all 'pardiso' to 'superlu')
setup.py												(comment lines 172 to 214)

Triggering the deconfiguration will change the following files:
edelweissfe/config/linsolve.py 						(resets to version before configuring)
edelweissfe/linsolve/pardiso 						(resets to version before configuring)
edelweissfe/linsolve/panuapardiso 					(resets to version before configuring)
edelweissfe/solvers/nonlinearimplicitstatic.py 	(resets to version before configuring)
setup.py												(resets to version before configuring)


Requirements
------------
1. os
2. numpy
3. git


Steps
-----
1. Copy files deconfigureaarch64.py, configureaarch64.py and linsolve.py into the EdelweissFE folder
2. To configure EdelweissFE for aarch64 do 'python configureaarch64.py'
3. To configure EdelweissFE for x86_64 do 'python deconfigureaarch64.py'
