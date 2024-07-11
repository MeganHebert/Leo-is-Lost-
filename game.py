import csv
import io

with open('Leo_is_Lost_input.csv','r') as file:
    game_input = csv.reader(file)
   
    input_rows = list(game_input)
print()


class Scenes:
    def __init__(self):
        self.scenes = {}

    def get_scenes(self):

        for i in range(len(input_rows)):
            self.scenes["scene_" + str(i)] = input_rows[i][1]

        return self.scenes


class Choices:
    def __init__(self):
        self.choices = {}
    
    def get_choices(self):
        inc_num = 0

        for i in range(len(input_rows)):
            if i == 0 or input_rows[i][2] == "": # read left to right, first part will continue if true 
                continue

            inc_num += 1

            self.choices["choice_" + str(inc_num)] = input_rows[i][2]

        for k in range(len(input_rows)):
            if k == 0 or input_rows[k][4] == "": 
                continue

            inc_num += 1

            self.choices["choice_" + str(inc_num)] = input_rows[k][4]

        return self.choices
    

class Play: 
    def user_game(self):
        scenes_obj = Scenes()
        scenes_dic = scenes_obj.get_scenes()

        choices_obj = Choices()
        choices_dic = choices_obj.get_choices()


        question_1 = f"{scenes_dic['scene_1']}. Should he '{choices_dic['choice_1']}' or '{choices_dic['choice_4']}':"
        print(question_1)

        user_choice1 = input()
        user_choice1 = user_choice1.strip()


        while True:
            if user_choice1 == choices_dic['choice_1']:
                question_2 = f"{scenes_dic['scene_2']}. Should he '{choices_dic['choice_2']}' or '{choices_dic['choice_5']}':"
                question_final = question_2
                print(question_2)

                while True:
                    user_choice2 = input()
                    user_choice2 = user_choice2.strip()
                    user_choice_final = user_choice2

                    if user_choice2 == choices_dic['choice_2']:
                        print(scenes_dic['scene_3']) 
                        winning_scene = scenes_dic['scene_3'] 
                        break
                    elif user_choice2 == choices_dic['choice_5']:
                        print(scenes_dic['scene_6'])
                        winning_scene = scenes_dic['scene_6']
                        break
                    else:
                        print("Please enter a valid answer.")

                break

            elif user_choice1 == choices_dic['choice_4']:
                question_3 = f"{scenes_dic['scene_4']}. Should he '{choices_dic['choice_3']}' or '{choices_dic['choice_6']}':"
                question_final = question_3
                print(question_3)

                while True:
                    user_choice3 = input()
                    user_choice3 = user_choice3.strip()
                    user_choice_final = user_choice3

                    if user_choice3 == choices_dic['choice_3']:
                        print(scenes_dic['scene_5'])
                        winning_scene = scenes_dic['scene_5']
                        break
                    elif user_choice3 == choices_dic['choice_6']:
                        print(scenes_dic['scene_7'])
                        winning_scene = scenes_dic['scene_7']
                        break
                    else:
                        print("Please enter a valid answer.")

                break

            else:
                print("Please enter a valid answer.")
                user_choice1 = input()
                continue 


        with open('Leo_is_Lost_output.csv', 'w', newline="") as file: 
            writer = csv.writer(file, delimiter=",")

            writer.writerow([question_1, user_choice1])
            writer.writerow([question_final, user_choice_final])
            writer.writerow([winning_scene])
            

if __name__ == "__main__":
    print("Welcome to Leo is Lost!")
    print("A golden retriever, Leo, and his owner went on a hike through the wilderness.")
    print("Unfortunately Leo got distracted by a butterfly and lost track of his owner.")
    print("You need to help Leo make decisions to get back to his owner.")
    print("Before we begin, please enter your name:")
    name = input()
    print(f"Thank you, {name}! Lets help Leo!")
    print()


    play_obj = Play()
    play_this = play_obj.user_game()
    
    
            