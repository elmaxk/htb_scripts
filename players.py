#!/usr/bin/env python

from random import choice


players = ['Harry', 'Mary', 'Larry', 'Lenny', 'Dookie', 'Freddie', 'Kollie', 'Dali', 'Mali']

teamA = []
teamB = []

playerA = players
playerB = players


try:
    while len(players) > 0:
        playerA = choice(players)
        teamA.append(playerA)
        players.remove(playerA)

        playerB = choice(players)
        teamB.append(playerB)
        players.remove(playerB)

except Exception as e:
    print(e)


print('Team A: ', teamA)
print('Team B: ', teamB)

