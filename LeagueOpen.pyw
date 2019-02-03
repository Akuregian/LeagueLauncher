# League Launcher and Sign in

import pyautogui
import time

LeagueSigninBox ='C:/Users/Antho/Desktop/PythonProject/Projects/League/Login.png'
SignInButton = 'C:/Users/Antho/Desktop/PythonProject/Projects/League/Signin.png'
SignInButton2 = 'C:/Users/Antho/Desktop/PythonProject/Projects/League/Signin2.png'

finding= True
while finding:
	if finding == True:
		#Locate the Password box
		print('Locating Password Box')
		SignPass = pyautogui.locateOnScreen(LeagueSigninBox, grayscale=False, confidence=0.75)
		if SignPass:
			print("Doing calculations on box")
			passX = int(SignPass[0] + SignPass[2] / 2)
			passY = int(SignPass[1] + SignPass[3] / 2) + 33
			finding = False

		else:
			continue

	else:
		print("Not Found, Retrying")
		fiding = True




if SignPass:
	# Sign in and click login Button
	print('Found!')
	time.sleep(0.5)
	pyautogui.click(passX, passY)
	print('Entering Password')
	time.sleep(0.5)
	pyautogui.typewrite('Eclecticowl12', interval=0.1)

	LoginBox = pyautogui.locateOnScreen(SignInButton, grayscale=False, confidence=0.75)
	LoginBox2 = pyautogui.locateOnScreen(SignInButton2, grayscale=False, confidence=0.75)

	if LoginBox:
		print('First Attemp Worked')
		signX = int(LoginBox[0] + LoginBox[2] / 2)
		signY = int(LoginBox[1] + LoginBox[3] / 2)
		pyautogui.click(signX, signY)
		print("Logging in Please Wait")
	elif LoginBox2:
		print('Second Attemp Worked')
		sign2X = int(LoginBox2[0] + LoginBox2[2] / 2)
		sign2Y = int(LoginBox2[1] + LoginBox2[3] / 2)
		pyautogui.click(sign2X, sign2Y)
		print("Logging in Please Wait")
	else:
		print("Neither Boxes Where found, please Retry.")
		
else:
	print("Login Box Not Found, Searching")
	time.sleep(1)


