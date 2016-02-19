from matplotlib import pyplot as plt
import numpy as np
import cv2

## Blurring

def blurring_averaging(img_url, mask_size):
	img = cv2.imread(img_url)
	blur = cv2.blur(img,(mask_size,mask_size))

	plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(blur,cmap = 'gray')
	plt.title('Blurred avg '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])

	plt.show()

def blurring_gaussian(img_url, mask_size):
	img = cv2.imread(img_url)
	blur = cv2.GaussianBlur(img,(mask_size,mask_size), 0)

	plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(blur,cmap = 'gray')
	plt.title('Blurred Gaussian '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])

	plt.show()

def blurring_median(img_url, mask_size):
	img = cv2.imread(img_url)
	blur = cv2.medianBlur(img, mask_size)

	plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(blur,cmap = 'gray')
	plt.title('Blurred Median '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])

	plt.show()

def compare(img_url, mask_size):
	img = cv2.imread(img_url)
	avg_blur = cv2.blur(img,(mask_size,mask_size))
	gaussian_blur = cv2.GaussianBlur(img,(mask_size,mask_size), 0)
	median_blur = cv2.medianBlur(img, mask_size)

	plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(avg_blur,cmap = 'gray')
	plt.title('Blurred avg '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(gaussian_blur,cmap = 'gray')
	plt.title('Blurred Gaussian '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(median_blur,cmap = 'gray')
	plt.title('Blurred Median '+str(mask_size)+"x"+str(mask_size)), plt.xticks([]), plt.yticks([])

	plt.show()