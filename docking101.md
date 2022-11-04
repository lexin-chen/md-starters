# Docking 101
### Preparing the ligands
- ZINC15 search the ligands 
- Downloading the ```.mol2``` for desired ligands.
  - Chrome might not download so use another browser.
  - Files you should get after: 
  - Convert to ```.pdbqt```
      - ```ml openbabel```
      - ```obabel *.mol2 -O *.pdbqt```

### Autodock Vina
- Run Autodock Vina for the ligands.
- Using autodocktool to make the flexible receptorr
  - Flexible docking (this is a struggle point; here are some videos that “may” help)
  [Video help](https://www.youtube.com/watch?v=YTQIuUZRNbA&ab_channel=Euz%C3%A9bioGuimar%C3%A3es) or [Link help](
https://bioinformaticsreview.com/20201010/how-to-perform-flexible-docking-using-autodock-vina/)
  - The flexible residues I selected: ASP147, W293, H297, Y326 (critical residues)

### Ligand simulation
- Convert docked ligand ```.pdbqt``` into ```.mol2``` files
	- You can module load openbabel
	- ```obabel *.pdbqt -O *.mol2```
- Setting up the docked ligand for future steps
	- ```Module load chimera``` 
	- Add in hydrogen and standard charges
	- Save it as ```<ligand>.mol2``` files
- Creating psf files for the ligand
	- Load the mol2 files from last step on CHARMM-GUI Input Generator 
		- Check guess connectivity on the next page
		- Download the ```.tgz``` file to your directories
- Creating force field for the ligand
	- Load the mol2 files in step 15 on https://cgenff.umaryland.edu/userRegistration/ 
	- Check first 2 boxes. 
	- Get the ```.str``` file on the output and put it in your directory
- Then go to CHARMM-GUI

	



