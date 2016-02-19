from matplotlib import pyplot as plt
import numpy as np
import cv2
import math

def run(img_url):
	img = cv2.imread(img_url)
	# Convert to gray
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# Simple equalization in order to not lose forward information
	equ = cv2.equalizeHist(gray)

	# Canny edge 
	edges = cv2.Canny(equ,100,200)

	plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray')
	plt.title('Gray'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(equ,cmap = 'gray')
	plt.title('Equalization'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(edges,cmap = 'gray')
	plt.title('Canny edge detection'), plt.xticks([]), plt.yticks([])

	plt.show()