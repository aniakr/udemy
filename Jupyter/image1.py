import numpy
import cv2

im_g=cv2.imread("smallgray.png",0)

print(im_g)
# iteracja po row:

# for i in im_g:
#     print(i)
#
# # iteracja po kolumnie
#
# for i in im_g.T:
#     print(i)
#
# # iteracja po elementach
#
# for i in im_g.flat:
#     print(i)


im_g_hstuck=numpy.hstack((im_g,im_g))
im_g_vstuck=numpy.vstack((im_g,im_g))
print(im_g_vstuck)

# hsplit, vsplit

