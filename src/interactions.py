
instruction_text = '''
WELCOME TO BLACKJACK
#########

This is a single-player card game where you are trying to score as close to 21 as possible, without going over 21.
If you go over 21, the game is over.

At the start of the game, the dealer will deal you two cards. You then have a choice whether to:
- Hit, to receive another card, increasing your total, or
- Stick, and end the game with the cards you have.

All the cards you are dealt are random - they come from a single, shuffled pack.

If you're dealt an 'Ace' the game will ask you to decide if you want it to score 1 or 11.
You can only decide at the point when you're dealt the 'Ace' - you can't change your mind later.

Good Luck!

'''


def instructions():
    print(instruction_text)


initial_hand_text = "\nThe dealer will now deal you your initial hand of two cards.\n"


def initial_hand():
    print(initial_hand_text)


def set_ace_default() -> bool:
    # default = True means aces worth 11, False is aces worth 1 (aces_high variable elsewhere)
    default = None
    while default not in [True, False]:
        selection = input("Do you want Aces to default to 1 (enter 1) or 11 (enter 11)?\n")
        if selection == "1":
            default = False
        elif selection == "11":
            default = True
        else:
            print("Sorry, I don't understand. Please try that again.")
    return default


def choose_player_name() -> str:
    name: str = ""
    while len(name) < 1:  # catches users not entering a name
        name = input("\nWhat is your name, new player?\n")
    return name


def hit_or_stick() -> str:
    action: str = ""
    while len(action) < 1:  # catches users not entering a name
        action = input("\nDo you wish to Hit (h) or Stick (s)?\n")
        if action == "h":
            return action
        elif action == "s":
            return action


def end_game(player):
    print("\n##########")
    print("GAME OVER")
    print("##########\n")
    if player.current_total() == 21:
        print("CONGRATULATIONS! You scored exactly 21.\n")
    elif player.current_total() > 21:
        print("OH NO! You went over 21.\n")
    player.print_hand(end=True)
    print("\nThanks for playing!\n\n")
