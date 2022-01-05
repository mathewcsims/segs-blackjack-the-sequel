## BBC SEGS Blackjack Tech Test - the sequel

This is my second iteration of code to solve this task. My first attempt (aborted because I had concentrated on making the game playable rather than on ensuring my code passed the set tests) is at [segs-blackjack](https://github.com/mathewcsims/segs-blackjack).

The game implements a simple, single-player version of blackjack using a standard, single deck of cards (i.e., 52 cards, from Ace to King in the standard four suits). I give the player the choice of whether an Ace should be High (worth 11) or low (1). I've assumed that the user is comfortable interacting with a text-based application, and using the keyboard. 

I've not implemented any variations on the standard game, though I've taken an OO approach and sought to leave opportunities for variations to be added later, where appropriate (e.g., using more packs of cards, or adding additional players).

I have made the game fully playable, by a single player, and sought to provide instructions and feedback where needed.

You can play the game by running `blackjack.py`. The code should run on any installation of Python 3.x (3.8 used for development and testing) without any additional requirements.

Several unit tests are available, which can be run using `python3 -m unittest discover test` from the main directory (containing `blackjack.py`). Testing has not been exhaustive; it's likely there are still plenty of bugs
