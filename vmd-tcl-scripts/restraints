### Introduce restraints to an area of the protein

set all [atomselect top "all"]
set sel [atomselect top "protein and noh"] ###want to restrain all atoms in protein except hydrogens
$all set beta 0.0
$sel set beta 1.0
$all writepdb restraint.pdb
