# string_weasels

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=264466159&machine=standardLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=EastUs)

Python version of Richard Dawkins' Weasel program

I wrote this after reading Dudley Chapman's blog post on [Shakespeare, Evolution, and Weasels](https://theappleandthefinch.com/2016/04/30/shakespeare-evolution-and-weasels/). It was some good practice with Test-Driven Development (TDD).

My daughter is also learning about genetics in her 7th grade science class, so I thought this might interest her also. (It did. She was startled both at the results and that I built it in an hour and a half.)

To run, you'll need to either

* Click the *Open in GitHub Codespaces* badge at the top of this README

OR

1) Install [Python](https://www.python.org) 3.7 or higher.
2) Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
3) Clone this repo, then type `uv sync --dev` from a command prompt inside the project folder to install the needed dependencies.
4) Also at the command prompt, type `uv run python weasels.py` to run the code and find the target string.

On average, my program takes 150 generations starting with a seven-character line of gibberish to generate the line from Hamlet: "Methinks it is like a weasel." Dudley's program does it faster (30-60 generations), but I don't have his code to see why it makes quicker progress than mine.
