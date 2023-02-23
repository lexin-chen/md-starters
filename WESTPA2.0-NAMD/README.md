# WESTPA2.0 with NAMD

```WESTPA2.0-NAMD``` is a modified version of the original WESTPA code with NAMD. ```WE_concepts.md``` includes my takeaways taken from [Zuckerman and Chong, 2017](https://www.annualreviews.org/doi/abs/10.1146/annurev-biophys-070816-033834).

## Requirements
- [WESTPA](https://github.com/westpa/westpa) >= 2022.02 edition 
- [NAMD](http://www.ks.uiuc.edu/Research/namd/) >= 2.14
- [Python](http://www.python.org/) >= 3.7

## Getting started

After WESTPA2.0 is downloaded, 
- `common_files` where you put config file, `.psf`, `.pdb`
- `tstate` file where you define target state
- `bstate` directory is where you put all ur restart `.xsc`, `.vel`, `.coor`
- `west.cfg` is where you define bins; 
	- make sure `pcoord lim = `# of time you are outputting `dcdfreq`
	- `bin_target_count= `# of starting trajectories

### About Westpa_Scripts directory
- `w_init` calls for `westpa_scripts/get_pcoord.sh` so if there is an error edit that file.
- you need a `.pdb` file of the last frame of your MD simulation so you can run `get_pcoord.sh`
- Then you submit jobs	

### Submitting Jobs
- `NEW_sub.sh` is submission script used in parallel with multiple GPU
- `run.sh` is submission script for running in serial
- `w_run` calls for `westpa_scripts/runseg.sh`. If you wanna stop or change anything you rename that and submit again. 
- if you make error in anything delete the traj_seg of that iteration and the corresponding seg_log and you need to delete it from west.h5 using command `w_truncate -n 100` if you want to get rid of anything after iteration #99.
- `westpa_scripts/analysis.py` can be used if `w_pdist`,`w_succ`, any `w_` comands gives you an error about cannot read the `h5` file.
