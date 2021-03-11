import pyautogui, pyshorteners

link = input("Enter a link: ")

shortener = pyshorteners.Shortener()
short = shortener.tinyurl.short(link)

print(short)