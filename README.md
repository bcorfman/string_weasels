# string_weasels
Python version of Richard Dawkins' Weasel program

I wrote this after reading Dudley Chapman's blog post on [Shakespeare, Evolution, and Weasels](https://theappleandthefinch.com/2016/04/30/shakespeare-evolution-and-weasels/). It was some good practice with Test-Driven Development (TDD).

My daughter is also learning about genetics in her 7th grade science class, so I thought this might interest her also. (It did. She was startled both at the results and that I built it in an hour and a half.)

To run, you'll need to 
1) Have a Python 3.x version on your machine
2) Clone this repo, then type 'pip install -r requirements.txt' from a command prompt inside the project folder to install the needed dependencies.
3) Also at the command prompt, type 'python weasels.py' to run the code and find the target string. 

On average, my program takes 150 generations starting with a seven-character line of gibberish to generate the line from Hamlet: "Methinks it looks like a weasel." Dudley's program does it faster (30-60 generations), but I don't have his code to see why it makes quicker progress than mine.
