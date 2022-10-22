## To get started

- common_files where you put config file, psf, pdb
- tstate file where you define target state
- bstate directory is where you put all ur restart .xsc .vel .coor


- west.cfg - where you define bins; 
	- make sure pcoord lim = # of time you are outputting dcdfreq
	- bin_target_count= # of starting trajectories
<br/>
### About Westpa_Scripts directory
- w_init calls for westpa_scripts/get_pcoord.sh so if there's an error edit that file.
- you need a pdb file of the last frame of your MD simulation so you can run get_pcoord.sh

Then you submit jobs	
<br/>
### Submitting Jobs
- NEW_sub.sh is submission script used in parallel with multiple GPU
- run.sh is submission script for running in serial

- w_run calls for westpa_scripts/runseg.sh. If you wanna stop or change anything you rename that and submit again. 

- if you make error in anything delete the traj_seg of that iteration and the corresponding seg_log and you need to delete it from west.h5 using command "w_truncate -n 100" if you want to get rid of anything after ite. 99.

- ```westpa_scripts/analysis.py``` can be used if ```w_pdist``` gives you an error about cannot read the h5 file.


Software Not Mine, cite:<br/>
MC Zwier, JL Adelman, JW Kaus, AJ Pratt, KF Wong, NB Rego, E Suárez, S Lettieri, DW Wang, M Grabe, DM Zuckerman, and LT Chong. “WESTPA: An interoperable, highly scalable software package for weighted ensemble simulation and analysis”. J. Chem. Theory Comput., 11: 800-809 (2015).

JD Russo*, S Zhang*, JMG Leung*, AT Bogetti*, JP Thompson, AJ DeGrave, PA Torrillo, AJ Pratt, KF Wong, J Xia, J Copperman, JL Adelman, MC Zwier, DN LeBard, DM Zuckerman, and LT Chong. "WESTPA 2.0: High-Performance Upgrades for Weighted Ensemble Simulations and Analysis of Longer-Timescale Applications". J. Chem. Theory Comput., 18 (2), 638–649 (2022). *equal authorship
