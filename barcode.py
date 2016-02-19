from matplotlib import pyplot as plt
import numpy as np
import cv2
import math

def run(img_url):
	img = cv2.imread(img_url)
	# Convert to gray
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# Gaussian blur
	blur = cv2.GaussianBlur(gray,(5,5), 0)
	# Simple equalization in order to not lose forward information
	equ = cv2.equalizeHist(blur)

	c = 255/math.log10(256)
	copy = equ.copy()
	height, width = copy.shape
	for i in range(0, height):
		for j in range(0, width):
			copy[i, j] = c * math.log10(1 + copy[i, j])

	scharrx = cv2.Scharr(copy,cv2.CV_64F,1,0)
	scharry = cv2.Scharr(copy,cv2.CV_64F,0,1)
	scharr = scharrx + scharry

	plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,2),plt.imshow(gray,cmap = 'gray')
	plt.title('Gray'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,3),plt.imshow(blur,cmap = 'gray')
	plt.title('Gaussian blur'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,4),plt.imshow(equ,cmap = 'gray')
	plt.title('Equalization'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,5),plt.imshow(copy,cmap = 'gray')
	plt.title('Log transformation'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,6),plt.imshow(scharr,cmap = 'gray')
	plt.title('Edge detection'), plt.xticks([]), plt.yticks([])

	plt.show()