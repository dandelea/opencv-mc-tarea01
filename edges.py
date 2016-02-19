from matplotlib import pyplot as plt
import numpy as np
import cv2

# Edges detection

def scharr(img_url):
	img = cv2.imread(img_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.blur(gray,(5,5))

	scharrx = cv2.Scharr(gray,cv2.CV_64F,1,0)
	scharry = cv2.Scharr(gray,cv2.CV_64F,0,1)
	scharr = scharrx + scharry
	# Otsu's thresholding
	ret,th = cv2.threshold(np.array(scharr, np.uint8),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	plt.subplot(2,3,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Blurred avg 5x5'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,2),plt.imshow(scharr,cmap = 'gray')
	plt.title('Scharr X + Scharr Y'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,3),plt.imshow(scharrx,cmap = 'gray')
	plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,4),plt.imshow(scharry,cmap = 'gray')
	plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,5),plt.imshow(th,cmap = 'gray')
	plt.title('Threshold'), plt.xticks([]), plt.yticks([])

	plt.show()

def laplacian(img_url):
	img = cv2.imread(img_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(5,5), 0)

	laplacian = cv2.Laplacian(gray,cv2.CV_64F)
	# Otsu's thresholding
	ret,th = cv2.threshold(np.array(laplacian, np.uint8),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	plt.subplot(2,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Blurred Gaussian 5x5'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
	plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(th,cmap = 'gray')
	plt.title('Threshold'), plt.xticks([]), plt.yticks([])

	plt.show()

def sobel(img_url):
	img = cv2.imread(img_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.blur(gray,(5,5))

	sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
	sobel = sobelx + sobely
	# Otsu's thresholding
	ret,th = cv2.threshold(np.array(sobel, np.uint8),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	plt.subplot(2,3,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Blurred avg 5x5'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,2),plt.imshow(sobel,cmap = 'gray')
	plt.title('Sobel X + Sobel Y'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
	plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
	plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,3,5),plt.imshow(th,cmap = 'gray')
	plt.title('Threshold'), plt.xticks([]), plt.yticks([])


	plt.show()

def canny(img_url):
	img = cv2.imread(img_url)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	edges = cv2.Canny(gray,100,200)

	plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,2,2),plt.imshow(edges,cmap = 'gray')
	plt.title('Canny edge image'), plt.xticks([]), plt.yticks([])

	plt.show()