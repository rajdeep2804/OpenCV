#the hough transform basics: the hough transform is a popluar technique to detect any shape, if you can represent that
# represent that shape in a mathematical form. it can detect the shape even if it is broken or distored a little bit.

# A line in the image space can be expressed with two variables. For eg :
#1 In the cartesian coordinate system Yi = mXi +c
#2 in the polar coordinate system xcosQi + ysinQ = r

# in polar coordinate system
# r = x.cosQ + y.sinQ

# Hough transform algorithm :
#1 Edge detection, e.g using the canny edge detector.
#2 Mapping of edge points to the hough space and storge in an accumulator.
#3 Interpretation of the accumulator to yield lines of infinte length. the interpretation is done by thresholding
# and possibly other constraints.
#4 Conersion of infinte lines to finte lines.

# open cv implements two kind of hough line transforms.
#1 The Standard Hough Transform (HoughLines method)
#2 The probabilistic hough line transorm(Hough Lines P method)

