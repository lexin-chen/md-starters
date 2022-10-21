##Made this script because you have to pay for VideoMach on VMD. 

##This script renders every frame of your trajectory using TachyonInternal and you can string all the rendered picture in a video editor like Blender.

##It works for me on VMD 1.9.3 and very crashable on VMD 1.9.4. If VMD crashes, I suggest setting n to a number less than 80. 

set n [molinfo top get numframes]
for { set i 0 } { $i < $n } { incr i } {
	animate goto $i
	display update
	render TachyonInternal "C:/Users/lexin/Downloads/$i.png" -fullshade -auto_skylight 0.7 -aasamples 12 %s -format PNG -res 6000 4000 -o %s.png
}
