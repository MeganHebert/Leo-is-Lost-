if __name__ == "__main__":
    print("Welcome to Leo is Lost!")
    print("A golden retriever, Leo, and his owner went on a hike through the wilderness.")
    print("Unfortunately Leo got distracted by a butterfly and lost track of his owner.")
    print("You need to help Leo make decisions to get back to his owner.")
    print("Before we begin, please enter your name:")
    name = input()
    print(f"Thank you, {name}! Lets help Leo!")


import csv

with open('Leo_is_Lost_input.csv','r') as file:
    game_input = csv.reader(file)
   
    input_rows = list(game_input)
    #print(input_rows)
print()



first_scene = input_rows[1][1]
second_scene = input_rows[2][1]
third_scene = input_rows[3][1]
fourth_scene = input_rows[4][1]
fifth_scene = input_rows[5][1]
sixth_scene = input_rows[6][1]
seventh_scene = input_rows[7][1]

first_scene_choice1 = input_rows[1][2]
first_scene_choice2 = input_rows[1][4]


#print(first_scene_choice2)


def scene_one():
    print(first_scene)

    print(f"Should Leo: {first_scene_choice1} or {first_scene_choice2}")
    user_input1 = input()

    if user_input1 == first_scene_choice1:
        print(second_scene)
    elif user_input1 == first_scene_choice2:
        print(fourth_scene)
    else:
        print("Please enter a valid input, either type: turn left or turn right")
        user_input1 = input().lower()
        #scene_one()


    #print(user_choice_first_scene)



scene_one()


