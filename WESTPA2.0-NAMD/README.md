# Westpa2 with NAMD

This is helpful if you want to use WESTPA2022.02 edition with NAMD, this code is a modified version of the original [WESTPA code](https://github.com/westpa/westpa).

The pdf includes my notes taken from the [annual review paper](https://www.annualreviews.org/doi/abs/10.1146/annurev-biophys-070816-033834) for anyone unfamiliar to the method.

## To get started

- ```common_files``` where you put config file, ```.psf```, ```.pdb```
- ```tstate``` file where you define target state
- ```bstate``` directory is where you put all ur restart ```.xsc```, ```.vel```, ```.coor```


- west.cfg - where you define bins; 
	- make sure ```pcoord lim = ```# of time you are outputting dcdfreq
	- ```bin_target_count= ```# of starting trajectories

### About Westpa_Scripts directory
- ```w_init``` calls for ```westpa_scripts/get_pcoord.sh``` so if there's an error edit that file.
- you need a ```.pdb``` file of the last frame of your MD simulation so you can run ```get_pcoord.sh```
- Then you submit jobs	

### Submitting Jobs
- ```NEW_sub.sh``` is submission script used in parallel with multiple GPU
- ```run.sh``` is submission script for running in serial

- ```w_run``` calls for ```westpa_scripts/runseg.sh```. If you wanna stop or change anything you rename that and submit again. 

- if you make error in anything delete the traj_seg of that iteration and the corresponding seg_log and you need to delete it from west.h5 using command ```w_truncate -n 100``` if you want to get rid of anything after ite. 99.

- ```westpa_scripts/analysis.py``` can be used if ```w_pdist```,```w_succ```, any ```w_``` comands gives you an error about cannot read the ```h5``` file.
