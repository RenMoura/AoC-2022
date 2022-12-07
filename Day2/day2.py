"""Rock-Paper-Scissors points counting"""
score_guide = { "A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}

def rock_paper_scissors(my_hand, enemy_hand, true_strategy):
    if not true_strategy:
        if score_guide[my_hand] == score_guide[enemy_hand]:
            return "draw"
        elif (score_guide[my_hand] - score_guide[enemy_hand] == 1) or (score_guide[my_hand] - score_guide[enemy_hand] == -2):
            return "victory"
        else:
            return "defeat"
    else:
        if my_hand == "X":
            return "defeat"
        elif my_hand == "Y":
            return "draw"
        else:
            return "victory"

def strategy_logic(my_hand, enemy_hand, true_strategy):
    if true_strategy:
        if my_hand == "X":
            if enemy_hand == "A":
                return "C"
            elif enemy_hand == "B":
                return "A"
            else:
                return "B"
        elif my_hand == "Y":
            return enemy_hand
        else:
            if enemy_hand == "A":
                return "B"
            elif enemy_hand == "B":
                return "C"
            else:
                return "A"
    else:
        return my_hand

my_score = 0
enemy_score = 0
victory_points = 6
defeat_points = 0
draw_points = 3
i = 0
true_strategy = True
with open("Day2/input.txt","r") as strategy_guide:
    for match in strategy_guide:
        [enemy_hand, my_hand] = match.strip("\n").split(" ")
        result = rock_paper_scissors(my_hand, enemy_hand, true_strategy)
        my_hand = strategy_logic(my_hand, enemy_hand, true_strategy)
        if result == "victory":
            my_score = my_score + victory_points + score_guide[my_hand]
            enemy_score = enemy_score + defeat_points + score_guide[enemy_hand]
        elif result == "defeat":
            my_score = my_score + defeat_points + score_guide[my_hand]
            enemy_score = enemy_score + victory_points + score_guide[enemy_hand]
        elif result == "draw":
            my_score = my_score + draw_points + score_guide[my_hand]
            enemy_score = enemy_score + draw_points + score_guide[enemy_hand]

print(my_score)
print(enemy_score)


