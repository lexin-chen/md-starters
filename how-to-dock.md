# How to Dock
### Preparing the ligands
- ZINC15 search the ligands 
- Downloading the mol2 for morphine, naloxegol, naloxone, fentanyl, herkinorin (idk if there are any more but these for now) 
  - Chrome might not download but if not use firefox or something
  - Files you should get after: /orange/colina/le.chen/OpoidReceptor/Docking/ZincLigands
  - Convert to .pdbqt
      - ```ml openbabel```
      - ```obabel *.mol2 -O *.pdbqt```

### Autodock Vina
- Run autodock vina for the ligands.
  - You can poke around here: ```cd /orange/colina/le.chen/OpoidReceptor/Docking/FlexDocking```
- Using autodocktool to make the flexible receptorr
  - Flexible docking (this is a struggle point; here are some videos that “may” help)
  [Video help](https://www.youtube.com/watch?v=YTQIuUZRNbA&ab_channel=Euz%C3%A9bioGuimar%C3%A3es
https://bioinformaticsreview.com/20201010/how-to-perform-flexible-docking-using-autodock-vina/)
  - The flexible residues I selected: ASP147, W293, H297, Y326 (critical residues)

Ligand simulation
Convert docked ligand pdbqt into mol2 files
You can module load openbabel
obabel *.pdbqt -O *.mol2
Setting up the docked ligand for future steps
Module load chimera (you can use others as well)
Add in hydrogen and standard charges
Save it as <ligand>.mol2 files
/orange/colina/le.chen/OpoidReceptor/Docking/FlexDocking/DockedLigands
Creating psf files for the ligand
Load the mol2 files from step 15 on CHARMM-GUI Input Generator 
Check guess connectivity on the next page
Download the tgz file to your directories
Creating force field for the ligand
Load the mol2 files in step 15 on https://cgenff.umaryland.edu/userRegistration/ (register for an acc w gatormail) 

Check first 2 boxes. 
Get the .str file on the output and put it in your directory
Combining the ligand and protein as a complex
 Run this script for combining the protein with ligand (change the paths and stuff) /orange/colina/le.chen/OpoidReceptor/ComplexSims/Common/complex.tcl
Check that it is docked on vmd, that it is in the pocket. 
Load the pdb and psf into vmd
Add water box
Add ions
Move one Na between resid 147 and 154
I realize this was unnecessary as the ion should eventually equilibrate to that place. 
You can run the simulation now using same conf file as before.
Remember to load the ligand parameter into the parameter section of the conf file

Please let me know if anything is unclear, esp step 4 is pretty weird or there is a mistake I made.  Sorry, my directories may be a bit messy. 

	



