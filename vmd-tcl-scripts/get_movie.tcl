set n [molinfo top get numframes]
for { set i 0 } { $i < $n } { incr i } {
	animate goto $i
	display update
	render TachyonInternal "C:/Users/lexin/Downloads/new3/$i.png" -fullshade -auto_skylight 0.7 -aasamples 12 %s -format PNG -res 6000 4000 -o %s.png
}
for { set i 160 } { $i < $n } { incr i } {
	animate goto $i
	display update
	render TachyonInternal "C:/Users/lexin/Downloads/new3/$i.png" -fullshade -auto_skylight 0.7 -aasamples 12 %s -format PNG -res 6000 4000 -o %s.png
}
