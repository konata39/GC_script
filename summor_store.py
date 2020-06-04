from PIL import ImageGrab
import numpy as np
import cv2
import win32gui, win32api, win32con
import summor_store
global frame
from time import sleep

def summor(left,top):
	
	#進入召喚商店
	x = left + 499
	y = top + 537
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	sleep(5)

	#點選召喚稀有英雄
	x = left + 171
	y = top + 405
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	sleep(0.5)
	
	#點選召喚一次
	x = left + 418
	y = top + 544
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	sleep(0.5)
	
	#點選確認
	x = left + 619
	y = top + 464
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	sleep(5)
	
	#跳過畫面ˇ
	for i in range(3):
		x = left + 658
		y = top + 324
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
		sleep(0.5)
		
	x = left + 960
	y = top + 71
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	sleep(5)
	