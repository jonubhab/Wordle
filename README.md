# Wordle
A bot to solve 5-lettered Wordle

Files to be used:
1) Go.py: Automatically solves Wordle
2) Normal.py: Automatically solves Wordle in Normal mode
3) Hard.py: Automatically solves Wordle in Hard mode
4) Normal Manual.py: Solves wordle in normal mode with user intervention
5) Hard Manual.py: Solves wordle in hard mode with user intervention
6) cursor.py: Fine-tune coordinates for colour detection

Steps to use Go.py:
1) Snap the python terminal on the left half of your screen.
   Open Wordle and set the window on right half of your screen.
2) Select Normal or Hard mode. It calls 'Normal.py' or 'Hard.py' accordingly.
3) Watch it solve the wordle.
Caution: The coordinates of pyautogui are fine-tuned according to my system. It may differ in some other PC. Setting up coordinates:-
1) Run 'cursor.py' and snap the python terminal on the left half of your screen.
   Open Wordle and set the window on right half of your screen.
2) Enter (x,y) in python terminal to move the cursor.
3) Place the cursor at one of the corners of the top left box, so that the tip of the cursor can always sense colour.
4) Try moving the cursor to the same point of adjacent boxes.
5) Note the initial position of the cursor and the difference between adjacent boxes and replace them at the mark function of 'Normal.py' and 'Hard.py'.
6) Also, the program only runs in light mode.
   For night mode or if any other filter is applied on the screen, use 'pyscreenshot.grab().getpixel((x,y))' to get RGB value of the colour.
   Put the RGB value in mark function of 'Normal.py' and 'Hard.py'.

Other Files:
1) dictionary.txt: Contains all 5-lettered words.
2) Wordle Solutions.txt: Contains possible solutions of wordle.
3) Top Openers.txt: Contains words that eliminate highest number of words in first guess.
