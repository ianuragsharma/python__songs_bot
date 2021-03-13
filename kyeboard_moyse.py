import pyautogui
while True:
    pyautogui.click(1500,20,duration=0.1)
    pyautogui.keyDown('down')
    pyautogui.hotkey('shift', 'end')
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.click(655,186,duration=0.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(814,182,duration=0.1)
    pyautogui.click(358,503,duration=2)