from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
global frame

def print_locate(event,x,y,flags,param):
	global frame
	if event == cv2.EVENT_LBUTTONDOWN:
		print("locate: ",[x,y])
		print("color: ",frame[y, x])

hwnd = win32gui.FindWindow(None, 'BlueStacks') #抓取BlueStacks
while(1):
	try :
		left, top, right, bot = win32gui.GetWindowRect(hwnd) #取得該視窗位置
	except :
		print("找不到視窗")
	img = ImageGrab.grab(bbox = (left, top, right, bot))
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
	cv2.setMouseCallback("screen box",print_locate)
	
	cv2.imshow("screen box", frame)
	k = cv2.waitKey(30)&0xFF #64bits! need a mask
	if k ==27:
		cv2.destroyAllWindows()
		break