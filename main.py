# -*- coding: utf-8 -*-
import blurring, contrast, intensity, edges, barcode

def valid_input(input):
	try:
		i = int(input)
		valid = 1;
	except ValueError:
		print('Not valid input');
		valid = 0;
	return valid;

def valid_float(input):
	try:
		f = float(input)
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
	logo_file = 'logo.png'
	star_file = 'star.png'
	chess_file = 'chess.jpg'
	barcode_file = 'barcode.jpg'

	while(True):
		print("\n")
		print('Tarea 01 de MC - BASIC PROCESSING')
		print('1. Blurring')
		print('2. Contrast enhancement')
		print('3. Intensity transformation')
		print('4. Edges detection')
		print('5. Bar code processing')
		print('6. exit')
		option = input('Select option [1 - 6]: ')

		if valid_input(option)==1:
			option = int(option)
			if option > 0 and option < 7:
				if option==1:
					print('\n')
					print('1. Averaging mask')
					print('2. Gaussian filter')
					print('3. Median filter')
					print('4. Compare all')
					print('5. exit')
					method = input('Select method [1 - 5]: ')

					if valid_input(method)==1:
						method = int(method)
						if method > 0 and method < 6:
							if method==1:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring.blurring_averaging(logo_file, mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										blurring.blurring_averaging(logo_file, mask_size)
							elif method==2:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring.blurring_gaussian(logo_file, mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										if odd_input(mask_size):
											blurring.blurring_gaussian(logo_file, mask_size)		
							elif method==3:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring.blurring_median(logo_file, mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										if odd_input(mask_size):
											blurring.blurring_median(logo_file, mask_size)
							elif method==4:
								print("\n")
								mask_size = input('Write mask size (default=5): ')
								if mask_size=="":
									mask_size = 5
									blurring.compare(logo_file, mask_size)
								else:
									if valid_input(mask_size):
										mask_size = int(mask_size)
										if odd_input(mask_size):
											blurring.compare(logo_file, mask_size)	
							else:
								print("Bye")
								break;
				elif option==2:
					print('\n')
					print('1. Histogram equalization')
					print('2. CLAHE (Contrast Limited Adaptive Histogram Equalization)')
					print('3. Compare all')
					print('4. exit')
					method = input('Select method [1 - 4]: ')

					if valid_input(method)==1:
						method = int(method)
						if method > 0 and method < 5:
							if method==1:
								print("\n")
								contrast.histogram_equalization(star_file)
							elif method==2:
								print("\n")
								contrast.histogram_CLAHE(star_file)
							elif method==3:
								print("\n")
								contrast.compare(star_file)
							else:
								print("Bye")
								break;


				elif option==3:
					print('\n')
					print('1. Image negative')
					print('2. Log transformation')
					print('3. Inverse log transformation')
					print('4. Power-law transformation')
					print('5. Compare all')
					print('6. exit')
					method = input('Select method [1 - 6]: ')

					if valid_input(method)==1:
						method = int(method)
						if method > 0 and method < 7:
							if method==1:
								print("\n")
								intensity.invert(star_file)
							elif method==2:
								print("\n")
								intensity.log_transformation(star_file)
							elif method==3:
								print("\n")
								intensity.inverse_log_transformation(star_file)
							elif method==4:
								print("\n")
								n = input('Write pow factor (default=0.5): ')
								if n=="":
									n = 0.5
									intensity.power_law_transformation(star_file, n)
								else:
									if valid_float(n):
										n = float(n)
										intensity.power_law_transformation(star_file, n)
							elif method==5:
								print("\n")
								intensity.compare(star_file)
							else:
								print("Bye")
								break;
				elif option==4:
					print('\n')
					print('1. Sobel')
					print('2. Scharr')
					print('3. Laplacian')
					print('4. Canny edge')
					print('5. exit')
					method = input('Select method [1 - 5]: ')

					if valid_input(method)==1:
						method = int(method)
						if method > 0 and method < 6:
							if method==1:
								print("\n")
								edges.sobel(chess_file)
							elif method==2:
								print("\n")
								edges.scharr(chess_file)
							elif method==3:
								print("\n")
								edges.laplacian(chess_file)
							elif method==4:
								print("\n")
								edges.canny(chess_file)
							else:
								print("Bye")
								break;
				elif option==5:
					print('\n')
					barcode.run(barcode_file)
				else:
					print("Bye")
					break;
			else:
				print('Entrada no válida');


if __name__=='__main__':
	main()