from matplotlib import pyplot as plt
import numpy as np
import cv2
import math

def run(img_url):
	img = cv2.imread(img_url)
	# Convert to gray
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(3,3), 0)
	

	# Canny edge 
	edges = cv2.Canny(gray,100,200)

	plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray')
	plt.title('Blurred gray'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge detection'), plt.xticks([]), plt.yticks([])

	plt.show()