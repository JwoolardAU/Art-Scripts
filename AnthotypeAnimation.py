# importing libraries 
import cv2 
import numpy as np
import time

vidNum = 1
videoFileName = [r'Little_Eve.mov',r'Nev.mov',r'Car.mov',r'Pat.mov']
frameTransitionPause = .125 # How long you want the video to pause in-between each frame (in seconds)
window_name = "window"
borderPixel = 135 # 128 for crt


cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while True:
	# Create a VideoCapture object and read from input file 
	cap = cv2.VideoCapture(videoFileName[vidNum-1])

	# Check if camera opened successfully 
	if (cap.isOpened()== False): 
		print("Error opening video file") 


	# Read until video is completed 
	while(cap.isOpened()): 
		
	# Capture frame-by-frame 
		ret, frame = cap.read()
		time.sleep(frameTransitionPause) 
		if ret == True:
			frame = cv2.copyMakeBorder(frame, 0, 0, borderPixel, borderPixel, cv2.BORDER_CONSTANT, None, value = 0) 
			cv2.imshow(window_name, frame)
			
		# Press Q on keyboard to exit 
			if cv2.waitKey(25) & 0xFF == ord('q'): 
				exit()
				#break

	# Break the loop 
		else:
			if  vidNum == len(videoFileName):
				vidNum = 1
			else:
				vidNum += 1
			break

	# When everything done, release the video capture object 
	cap.release() 

	# Closes all the frames 
	#cv2.destroyAllWindows() # Commented out because we want an endless video loop
