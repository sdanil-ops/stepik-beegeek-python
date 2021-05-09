#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The input to the program is a line of text - the name of
#    the football team. The program repeats it on the screen
#    with the words "- чемпион!" Uses similar to task1 code.
#    -----------------------------------------------------------

def praise_team(team: str = None):
    """Prints praise to specified team"""
    if team is None:
        team = input()
    print(f'{team} - чемпион!')


praise_team()
