from PIL import ImageGrab
import numpy as np
import cv2
import win32gui, win32api, win32con
import summor_store
global frame
flag = True
hwnd = win32gui.FindWindow(None, 'BlueStacks') #抓取BlueStacks

while(1):
	try :
		left, top, right, bot = win32gui.GetWindowRect(hwnd) #取得該視窗位置
	except :
		print("找不到視窗")
	img = ImageGrab.grab(bbox = (left, top, right, bot))
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
	
	#偵查免費抽
	if list(frame[515, 519]) == [0, 72, 255] and flag == True:
		print("find!!")
		summor_store.summor(left,top)
		flag = False
	
	cv2.imshow("screen box", frame)
	k = cv2.waitKey(30)&0xFF #64bits! need a mask
	if k ==27:
		cv2.destroyAllWindows()
		break