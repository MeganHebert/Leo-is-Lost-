import csv

with open('Leo_is_Lost_input.csv','r') as file:
    game_input = csv.reader(file)
   
    input_rows = list(game_input)
    # print(input_rows)
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
            if i == 0 or input_rows[i][2] == "":
                continue

            """ if input_rows[i][2] == "":
               continue  # continue to next iteration of the for loop  """

            inc_num += 1

            self.choices["choice_" + str(inc_num)] = input_rows[i][2]
            self.choices["choice_" + str(inc_num)] = input_rows[i][4]


            # filtered_choices = {key: value for key, value in self.choices.items() if value.strip()}

            # print(filtered_choices)
        return self.choices


if __name__ == "__main__":
    print("Welcome to Leo is Lost!")
    print("A golden retriever, Leo, and his owner went on a hike through the wilderness.")
    print("Unfortunately Leo got distracted by a butterfly and lost track of his owner.")
    print("You need to help Leo make decisions to get back to his owner.")
    print("Before we begin, please enter your name:")
    name = input()
    print(f"Thank you, {name}! Lets help Leo!")

    scenes_obj = Scenes()
    scenes_dic = scenes_obj.get_scenes()
    print(scenes_dic["scene_1"])

    choices_obj = Choices()
    choices_dic = choices_obj.get_choices()
    print(choices_dic)



