# -*- coding: utf-8 -*-

import cv2;

img_url = 'logo.png'

def valid_input(input):
	try:
		input = int(input)
		valid = 1;
	except ValueError:
		print('Not valid input');
		valid = 0;
	return valid;

def odd_input(input):
	if input%2 != 0:
		return True
	else:
		print('Input must be odd');
		return False


def main():
	while(True):
		print("\n")
		print('Tarea 01 de MC - BASIC PROCESSING')
		print('1. Blurring')
		print('2. Contrast enhancement')
		print('3. Intensity transformation')
		print('4. Edges detection')
		print('5. exit')
		option = input('Select option [1 - 5]: ')

		if valid_input(option)==1:
			option = int(option)
			if option > 0 and option < 6:
				if option==1:
					print('\n')
					print('1. Averaging mask')
					print('2. Gaussian filter')
					print('3. Median filter')
					print('4. back')
					method = input('Select method [1 - 4]: ')

					if valid_input(method)==1:
						method = int(method)
						if method > 0 and method < 5:
							if method==1:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring_averaging(mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										blurring_averaging(mask_size)
							elif method==2:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring_gaussian(mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										if odd_input(mask_size):
											blurring_gaussian(mask_size)		
							elif method==3:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring_median(mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										if odd_input(mask_size):
											blurring_median(mask_size)	
							else:
								break;
				elif option==2:
					break;
				elif option==3:
					break;
				elif option==4:
					break;
				else:
					print("Bye")
					break;
			else:
				print('Entrada no válida');

def blurring_averaging(mask_size):
	img = cv2.imread(img_url)
	blur = cv2.blur(img,(mask_size,mask_size))

	cv2.imshow('original',img)
	cv2.imshow('blurred',blur)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

def blurring_gaussian(mask_size):
	img = cv2.imread(img_url)
	blur = cv2.GaussianBlur(img,(mask_size,mask_size), 0)

	cv2.imshow('original',img)
	cv2.imshow('blurred',blur)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

def blurring_median(mask_size):
	img = cv2.imread(img_url)
	blur = cv2.medianBlur(img, mask_size)

	cv2.imshow('original',img)
	cv2.imshow('blurred',blur)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=='__main__':
	main();