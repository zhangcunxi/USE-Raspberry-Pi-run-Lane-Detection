from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
from lane_detect_pi import Lines


ap = argparse.ArgumentParser()

args = vars(ap.parse_args())

lines = Lines()
lines.look_ahead = 10
lines.remove_pixels = 100
lines.enlarge = 2.25

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)




while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	


	#cv2.imshow("Frame", frame)
	cv2.imshow("Rpi lane detection", lines.project_on_road_debug(frame))
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	#fps.update()

print("[INFO]  stop the video stream...")

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

