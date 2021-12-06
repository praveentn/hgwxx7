import os
import random

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

# addToClipBoard("praveen")

quotes = [
    "Your patience is your power",
    "Nothing changes if nothing changes",
    "Keep it simple but significant",
    "The time is always right to do what is right",
    "Be a voice, not an echo",
    "Keep going, no matter what",
    "Focus on what matters",
    "Be wild for a while",
    "Keep life simple",
    "The best is yet to be",
    "Do what they think you can't do",
]

quote = random.choice(quotes)
print(quote)

addToClipBoard(quote)
