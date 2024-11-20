This repository can be used to configure https://github.com/EdelweissFE/EdelweissFE for use on aarch64 CPU.
It is compatible with the EdelweissFE version from 20th November 2024 and earlier. 

EdelweissFE aarch64 configurator
--------------------------------

USE WITH CARE!

Triggering the configuration will change the following files/folders:
* `edelweissfe/config/linsolve.py` 						(will change the file to the version as of 20th November 2024)
* `edelweissfe/linsolve/pardiso` 						(will get deleted)
* `edelweissfe/linsolve/panuapardiso` 					(will get deleted)
* `edelweissfe/solvers/nonlinearimplicitstatic.py` 	(changes all 'pardiso' to 'superlu')
* `setup.py`												(comment lines 172 to 214)

Triggering the deconfiguration will change the following files/folders:
* `edelweissfe/config/linsolve.py` 						(resets to version before configuring)
* `edelweissfe/linsolve/pardiso` 						(resets to version before configuring)
* `edelweissfe/linsolve/panuapardiso` 					(resets to version before configuring)
* `edelweissfe/solvers/nonlinearimplicitstatic.py` 	(resets to version before configuring)
* `setup.py`												(resets to version before configuring)


Requirements
------------
* os
* numpy
* git


Steps
-----
1. Copy files deconfigureaarch64.py, configureaarch64.py and linsolve.py into the EdelweissFE folder
2. To configure EdelweissFE for aarch64 do `python configureaarch64.py`
3. To configure EdelweissFE for x86_64 do `python deconfigureaarch64.py`
