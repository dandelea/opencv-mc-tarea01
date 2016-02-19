from matplotlib import pyplot as plt
import numpy as np
import cv2
import math

## Intensity transformations

def invert(image_url):
	img = cv2.imread(image_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	inverse = 255-gray

	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(inverse,cmap = 'gray')
	plt.title('Negative'), plt.xticks([]), plt.yticks([])

	plt.show()

def log_transformation(image_url):
	img = cv2.imread(image_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	c = 255/math.log10(256)

	copy = gray.copy()
	height, width = copy.shape
	for i in range(0, height):
		for j in range(0, width):
			copy[i, j] = c * math.log10(1 + copy[i, j])

	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(copy,cmap = 'gray')
	plt.title('Log transformation'), plt.xticks([]), plt.yticks([])

	plt.show()

def inverse_log_transformation(image_url):
	img = cv2.imread(image_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	c = 255 / math.log10(256)

	copy = gray.copy()/255
	height, width = copy.shape
	for i in range(0, height):
		for j in range(0, width):
			copy[i, j] = c * math.exp(copy[i, j]-1)

	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(copy,cmap = 'gray')
	plt.title('Inverse log transformation'), plt.xticks([]), plt.yticks([])

	plt.show()

def power_law_transformation(image_url, n):
	img = cv2.imread(image_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	c = 255.0 / (255.0**(n))

	copy = gray.copy()
	height, width = copy.shape
	for i in range(0, height):
		for j in range(0, width):
			copy[i, j] = max(0, min(255, int(c * copy[i,j]**n)))
			
	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(copy,cmap = 'gray')
	plt.title('Power-law transformation x' + str(n)), plt.xticks([]), plt.yticks([])

	plt.show()

def compare(img_url):
	img = cv2.imread(img_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	inverse = 255-gray
	c1 = 255/math.log10(256)
	n = 2
	c2 = 255.0 / (255.0**(n))

	log_transformation = gray.copy()
	height, width = log_transformation.shape
	for i in range(0, height):
		for j in range(0, width):
			log_transformation[i, j] = c1 * math.log10(1 + log_transformation[i, j])

	inverse_log_transformation = gray.copy()/255
	height, width = inverse_log_transformation.shape
	for i in range(0, height):
		for j in range(0, width):
			inverse_log_transformation[i, j] = c1 * math.exp(inverse_log_transformation[i, j]-1)

	power_transformation = gray.copy()
	height, width = power_transformation.shape
	for i in range(0, height):
		for j in range(0, width):
			power_transformation[i, j] = max(0, min(255, int(c2 * power_transformation[i,j]**n)))

	plt.subplot(2,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(inverse,cmap = 'gray')
	plt.title('Negative'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(log_transformation,cmap = 'gray')
	plt.title('Log transf'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(inverse_log_transformation,cmap = 'gray')
	plt.title('Inverse log transf'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(power_transformation,cmap = 'gray')
	plt.title('Power-law transf x' + str(n)), plt.xticks([]), plt.yticks([])

	plt.show()