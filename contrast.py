from matplotlib import pyplot as plt
import numpy as np
import cv2

## Contrast Enhancement

def histogram_equalization(image_url):
	img = cv2.imread(image_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	hist,bins = np.histogram(gray.flatten(),256,[0,256])
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max()/ cdf.max()
	plt.plot(cdf_normalized, color = 'b')

	plt.hist(img.flatten(),256,[0,256], color = 'r')
	plt.xlim([0,256])
	plt.legend(('filter','histogram'), loc = 'upper left')
	plt.title('Original histogram filtered. Close to continue')
	plt.show()

	equ = cv2.equalizeHist(gray)

	plt.hist(equ.flatten(),256,[0,256], color = 'r')
	plt.xlim([0,256])
	plt.legend(('histogram'), loc = 'upper left')
	plt.title('Equalized histogram. Close to continue')
	plt.show()

	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(equ,cmap = 'gray')
	plt.title('Equalized'), plt.xticks([]), plt.yticks([])
	plt.show()

def histogram_CLAHE(image_url):
	img = cv2.imread(image_url, 0)

	clahe = cv2.createCLAHE() # DEFAULT: Contrast clip limit: 40, block size: 8x8
	cl1 = clahe.apply(img)

	plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(cl1,cmap = 'gray')
	plt.title('Adaptative equalization'), plt.xticks([]), plt.yticks([])

	plt.show()

def compare(img_url):
	img = cv2.imread(img_url)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	equ = cv2.equalizeHist(img)
	clahe = cv2.createCLAHE() # DEFAULT: Contrast clip limit: 40, block size: 8x8
	cl1 = clahe.apply(img)

	plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(equ,cmap = 'gray')
	plt.title('Simple equalization'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(cl1,cmap = 'gray')
	plt.title('Adaptative equalization'), plt.xticks([]), plt.yticks([])

	plt.show()
