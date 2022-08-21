#By bluedrummer or https://github.com/bluedrummer?tab=repositories at github
#Thank you for using!
import sys
import random

print("By bluedrummer or https://github.com/bluedrummer?tab=repositories at github.")
print("THIS CODE IS NOT FULLY FINISISHED BUGS MAY BE FOUND")
print("This is a board game.")
print()
print()
print('''At the start of the game all levers or tiles are open (cleared, up), showing the numerals 1 to 9.
During the game, each player plays in turn. A player begins their turn by throwing or rolling the die or dice into the box. If all of the remaining tiles show 6 or lower, the player may roll only one die. Otherwise, the player must roll both dice.
After throwing, the player adds up (or subtracts) the pips (dots) on the dice and then shuts (closes, covers) one of any combination of open numbers that sums to the total number of dots showing on the dice. For example, if the total number of dots is 8, the player may choose any of the following sets of numbers (as long as all of the numbers in the set are available to be covered):

    8
    7, 1
    6, 2
    5, 3
    5, 2, 1
    4, 3, 1

The player then rolls the dice again, aiming to shut more numbers. The player continues throwing the dice and shutting numbers until reaching a point at which, given the results produced by the dice, the player cannot shut any more numbers. At that point, the player scores the sum of the numbers that are still uncovered. For example, if the numbers 2, 3, and 5 are still open when the player throws a one, the player's score is 10 (2 + 3 + 5 = 10). Play then passes to the next player.
After every player has taken a turn, the player with the lowest score wins.
If a player succeeds in closing all of the numbers, that player is said to have Shut the Box – the player wins immediately and the game is over. ''')
print()
print()
print("How many players are playing?")
player_with_lower_score = 1000
name_of_player_with_lower_score = ""
number_of_players = 0
while True:
    number_of_players = input()
    if not number_of_players.isdecimal():
        print("Please enter a number.")
    else:
        number_of_players = int(number_of_players)
        break

player_names = []
for i in range(0, number_of_players):
    print(f"What will be player {i+1}'s name?")
    player_names.append(input())
print()
print("Would you like the computer to play (yes or no).")

while True:
    computer_playing = input().upper()
    if computer_playing == "YES":
        computer_playing = True
        break
    elif computer_playing == "NO":
        computer_playing = False
        break
    print("Please enter yes or no.")

print()

def valid_option(numbers, box, total):
    valid = True
    numbers = numbers.split()
    for i in range(0, len(numbers)):
        if numbers[i].isalpha():
            valid = False
            return valid
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    for i in range(0, len(numbers)):
        if numbers[i] >= 10 or numbers[i] <= 0:
            valid = False
            return valid
    if sum(numbers) != total:
        valid = False
        return valid
    for i in range(0, len(numbers)):
        if box[numbers[i]-1] == False:
            valid = False
            return valid
    return valid

def show_box(box):
    box_2 = []
    for i in range(0, len(box)):
        if box[i] == True:
            box_2.append(i+1)
        elif box[i] == False:
            box_2.append("_")
    box_string = f"== {box_2[0]} {box_2[1]} {box_2[2]} {box_2[3]} {box_2[4]} {box_2[5]} {box_2[6]} {box_2[7]} {box_2[8]} =="
    return box_string

def number_of_die_to_roll(box):
    if box[6] == False and box[7] == False and box[8] == False:
        return 1
    return 2

def valid_combos(box, total):
    combos = []
    # One tile match
    if total > 0 and total < 10:
        if box[total-1] == True:
            combos.append([total])
    # Two tile match
    for i in range(0, len(box)):
        for j in range(i+1, len(box)):
            if box[i] == True and box[j] == True:
                if i+1+j+1 == total:
                    combos.append([i+1, j+1])
    # Three tile match
    for i in range(0, len(box)):
        for j in range(i+1, len(box)):
            for l in range(j+1, len(box)):
                if box[i] == True and box[j] == True and box[l] == True:
                    if i+j+l+3 == total:
                        combos.append([i+1, j+1, l+1])
    # Four tile match
    for i in range(0, len(box)):
        for j in range(i+1, len(box)):
            for l in range(j+1, len(box)):
                for m in range(l+1, len(box)):
                    if box[i] == True and box[j] == True and box[l] == True and box[m] == True:
                        if i+j+l+m+4 == total:
                            combos.append([i+1, j+1, l+1, m+1])
    return combos



def shut_the_box_turn(player, player_with_lower_score, name_of_player_with_lower_score):
    print()
    box = [True,True,True,True,True,True,True,True,True]
    score = 0
    number_of_dice_rolling = 2
    while True:
        dice_1 = 0
        dice_2 = 0
        total = 0
        if number_of_die_to_roll(box) == 1:
            print()
            print("Since the sum of the tiles is 6 or lower you may role 1 dice now.")
            print()
            print("Here is the box.")
            print()
            print(show_box(box))
            print()
            print("Do you want to role 1 or 2 die? (Please answer with 1 or 2).")
            print()
            while True:
                nb_of_die = input()
                if nb_of_die == "2":
                    number_of_dice_rolling = 2
                    break
                elif nb_of_die == "1":
                    number_of_dice_rolling = 1
                    break
                print()
                print("Please enter 1 or 2.")
            print()
        print(f"You rolled the die")
        print()
        if number_of_dice_rolling == 2:
            dice_1 = random.randint(1,6)
            dice_2 = random.randint(1,6)
            print(f"Dice 1 rolled {dice_1} and dice 2 rolled {dice_2} that means your total is {dice_1 + dice_2}.")
            print()
            total = dice_1 + dice_2
        else:
            dice_1 = random.randint(1,6)
            print(f"Dice 1 rolled {dice_1} that means your total is {dice_1}.")
            print()
            total = dice_1
        if valid_combos(box, total) == []:
            print("Your turn is over since you have no options!")
            print()
            all_scores = []
            for i in range(0, len(box)):
                if box[i] == True:
                    score += i+1
            if score < player_with_lower_score:
                player_with_lower_score = score
                name_of_player_with_lower_score = player
                all_scores.append(player_with_lower_score)
                all_scores.append(name_of_player_with_lower_score)
                return all_scores
            print(f"{player}'s score is {score}.")
            break
        print("Here is the box.")
        print()
        print(show_box(box))
        print()
        print("_________________________________________________________________")
        print()
        print("Which tiles do you want to shut? (Display your answer like this 1 2 3).")
        print()
        levers_to_shut = ""
        while True:
            levers_to_shut = input()
            valid = valid_option(levers_to_shut, box, total)
            if valid:
                levers_to_shut = levers_to_shut.split()
                for i in range(0, len(levers_to_shut)):
                    levers_to_shut[i] = int(levers_to_shut[i])
                break
            print("Invalid option problem might be that one of your numbers is below or is 0, one of your numbers might be 10 or above, you added a letter, you didint add spaces between your numbers.")
        for i in range(0, len(levers_to_shut)):
            box[levers_to_shut[i]-1] = False
        count = 0
        for i in range(0, len(box)):
            if box[i] == False:
                count += 1
        if count == 9:
            print()
            print("_____________________________________________________________")
            print()
            print(f"Congratulations {player} has WON by SHUTTING THE BOX!!!")
            print("GAME OVER!")
            print("Hope you enjoyed!")
            sys.exit()
        print("_________________________________________________________________________________")

stats = ""
for i in range(0, number_of_players):
    print()
    print("_____________________________________________________________________")
    print(f"It is now {player_names[i]}'s turn to play")
    stats = shut_the_box_turn(player_names[i], player_with_lower_score, name_of_player_with_lower_score)
    print()
    print(f"The person with the lowest score right now is {stats[1]} with {stats[0]} points.")
    player_with_lower_score = stats[0]
    name_of_player_with_lower_score = stats[1]

print()
print("_________________________________________________________________________")
print()
print("Everybodys turn has finished.")
print()
print("_________________________________________________________________________")
print()
print("The player with the lowest score is.")
print("...")
print("...")
print()
print(f"ITS {stats[1]} WITH {stats[0]} points.")
print("_________________________________________________________________________")
print()
print("Thank you for playing!")
print("GAME OVER")
sys.exit()
