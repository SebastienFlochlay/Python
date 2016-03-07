

from PIL import Image
import time
import sys
import os

def compareTwoPics(picture_1, picture_2, step=20):
	step = int(step)
	if step < 1:
		step = 1
	
	percent_similar = 0.0
	percent_red = 0.0
	percent_green = 0.0
	percent_blue = 0.0
	percent_totalcolor = 0.0
	
	
	total_check_points = 0.0
	total_not_match = 0.0
	percent_similar = 0.0

	pic1_total_red = 0
	pic1_total_green = 0
	pic1_total_blue = 0
	pic1_total_color = 0

	pic2_total_red = 0
	pic2_total_green = 0
	pic2_total_blue = 0
	pic2_total_color = 0

	#print picture_1
	#print picture_2
	
	try:
		pic1 = Image.open(picture_1)
		pic2 = Image.open(picture_2)
	except:
		# tried to open an unsupported format!!
		#print str(picture_1) + " is not a supported image format"
		#print str(picture_2) + " is not a supported image format"
		return -1.0

	pic1_width = pic1.size[0]
	pic1_height = pic1.size[1]

	pic2_width = pic2.size[0]
	pic2_height = pic2.size[1]
	

	if pic1_width != pic2_width:
		print "\n widths must be the same \n"
		sys.exit()
	if pic1_height != pic2_height:
		print "\n widths must be the same \n"
		sys.exit()
	

	for x in range(0, pic1_width):
		for y in range(0, pic1_height):
		
			if x % step == 0:
				pic1_color = pic1.getpixel((x,y))
				pic2_color = pic2.getpixel((x,y))
				
				total_check_points += 3
				
				if pic1_color[0] != pic2_color[0]:
					total_not_match += 1
				if pic1_color[1] != pic2_color[1]:
					total_not_match += 1
				if pic1_color[2] != pic2_color[2]:
					total_not_match += 1
					
				pic1_total_red += pic1_color[0]
				pic1_total_green += pic1_color[1]
				pic1_total_blue += pic1_color[2]
				

				pic2_total_red += pic2_color[0]
				pic2_total_green += pic2_color[1]
				pic2_total_blue += pic2_color[2]
	
	
	pic1_total_color = pic1_total_red + pic1_total_green + pic1_total_blue
	pic2_total_color = pic2_total_red + pic2_total_green + pic2_total_blue
	
	
	percent_similar = 1 - (total_not_match / total_check_points)
	percent_red = abs(float(pic2_total_red) / float(pic1_total_red))
	percent_green = abs(float(pic2_total_green) / float(pic1_total_green))
	percent_blue = abs(float(pic2_total_blue) / float(pic1_total_blue))
	percent_totalcolor = abs(float(pic2_total_color) / float(pic1_total_color))
	
	print '----'
	print "total % comparible red:  " + str(percent_red)
	print "total % comparible green:" + str(percent_green)
	print "total % comparible blue: " + str(percent_blue)
	print "total % comparible:      " + str(percent_totalcolor)
	
	
	return percent_similar
	
	

if __name__ == '__main__':
	try:
		import psyco
		psyco.full()
	except ImportError:
		print "...installing psyco would provide additional performance"
	
	
	thedetail = 20
	if len( sys.argv ) < 3:
		print "\n\n"
		print "Usage: " + str(sys.argv[0]) + " <photo1.png> <photo2.png> [detail]"
		print ""
		print " - photo1.png and photo2.png are the photos you are comparing"
		print " - detail is just a number.  The higher the number the faster"
		print " and less detailed the comparison will be.  Default detail is 20"
		print ""
		print "example:"
		print "	# Highest quality comparison, slowest turn around"
		print "	" + str(sys.argv[0]) + " photo.png photo2.png 1"
		print " "
		print "	# Low quality comparison, high turn around"
		print "	" + str(sys.argv[0]) + " photo.png photo2.png 100"
		sys.exit()
	else:
		try:
			thedetail = sys.argv[3]
		except:
			thedetail = 20
		
		tt = time.time()
		compareTwoPics(sys.argv[1], sys.argv[2], step=thedetail)
		print "execution seconds: " + str(time.time() - tt)
	
