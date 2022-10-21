### Here is a collection of all the tcl scripts I use often

###to introduce restraints to an area of the protein

set all [atomselect top "all"]
set sel [atomselect top "protein and noh"] ###want to restrain all atoms in protein except hydrogens
$all set beta 0.0
$sel set beta 1.0
$all writepdb restraint.pdb

### getting center of mass

proc get_cell {{molid top}} {
 set all [atomselect $molid all]
 set minmax [measure minmax $all]
 set vec [vecsub [lindex $minmax 1] [lindex $minmax 0]]
 puts "cellBasisVector1 [lindex $vec 0] 0 0"
 puts "cellBasisVector2 0 [lindex $vec 1] 0"
 puts "cellBasisVector3 0 0 [lindex $vec 2]"
 set center [measure center $all]
 puts "cellOrigin $center"
 $all delete
}
get_cell

# sasa tcl script

puts -nonewline "\n \t \t Selection: "
gets stdin selmode
 selection
set sel [atomselect top "$selmode"]
set protein [atomselect top "protein"]
set n [molinfo top get numframes]
set output [open "SASA_$selmode.dat" w]
 sasa calculation loop
for {set i 0} {$i < $n} {incr i} {
	molinfo top set frame $i
	set sasa [measure sasa 1.4 $protein -restrict $sel]
	puts "\t \t progress: $i/$n"
	puts $output "$sasa"
}
puts "\t \t progress: $n/$n"
puts "Done."	
puts "output file: SASA_$selmode.dat"
close $output

