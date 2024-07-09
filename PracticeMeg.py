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


class Scenes:

    scenes = {}

    for i in range(len(input_rows)):
        scenes["scene_" + str(i)] = input_rows[i][1]

    print(scenes)

"""     def get_scenes():
        scenes = {}

        for i in range(len(input_rows)):
            scenes["scene_" + str(i+1)] = input_rows[i][1]


        print(scenes)


    def __init__(self):
        self.scenes = {}

        for i in range(len(input_rows)):
            self.scenes["scene_" + str(i+1)] = input_rows[i][1]

        print(self.scenes)
    
 """


