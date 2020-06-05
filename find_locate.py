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
	
	img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
	cv2.setMouseCallback("screen box",print_locate)
	
	#找尋冒險按鈕位置
	img_edge = cv2.Canny(img_gray,100,200)
	
	advanture_pic = cv2.imread("Symbol_Main_SummonShop.png",0)
	advanture_edges = cv2.Canny(advanture_pic,100,200)
	x = int(advanture_pic.shape[1] * (img_edge.shape[1] / 1202))
	y = int(advanture_pic.shape[0] * (img_edge.shape[0] / 683))
	advanture_edges = cv2.resize(advanture_edges, (x, y),interpolation=cv2.INTER_CUBIC)
	
	found = cv2.matchTemplate(img_edge , advanture_edges, cv2.TM_CCOEFF_NORMED)
	threshold_b1 = .3
	loc = np.where(found >= threshold_b1)
	pts = zip(*loc[::-1])
	print(frame.shape)
	for pt in pts:
	 
	 
		cv2.rectangle(frame,(pt[0], pt[1]), (pt[0] + x, pt[1] + y), 255, 2)
	"""if amount_found != 0: 
		  
		# There may be more than one 
		# sign in the image 
		for (x, y, width, height) in found: 
			  
			# We draw a green rectangle around 
			# every recognized sign 
			cv2.rectangle(frame, (x, y),  
						  (x + height, y + width),  
						  (0, 255, 0), 5) """
	
	cv2.imshow("screen box", frame)
	k = cv2.waitKey(30)&0xFF #64bits! need a mask
	if k ==27:
		cv2.destroyAllWindows()
		break