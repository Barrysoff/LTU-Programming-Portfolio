"""
OOP design part 2 - Car racing
Author: Mattias Westermark

Note: Gemini has been used as a sounding board
in accordance with the allowed aids policy.

Reference sites:
https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial
https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/
"""

import numpy as np
import pandas as pd
import os

"""
Constant for path to files containing race track in txt-format.
"""

FILEPATH = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/"

"""
Set hyperparameters (geeksforgeeks)
"""

learning_rate = 0.8         # How much new info overrides old info.
discount_factor = 0.95      # How much future rewards are valued.
exploration_prob = 0.2      # Probability of taking a random action.
epochs = 10000              # Number of training episodes.

"""
UserInterface lets the user select race track and vehicle.
"""

class UserInterface:
    def __init__(self):
        pass

    def runMenu(self):
        track = self._select_track()
        if track is None:
            return None, None
        vehicle = self._select_vehicle()
        if vehicle is None:
            return None, None

        return track, vehicle

    def select_track(self): 
        while True:
            print("# Select Race Track")
            print("1. Track 1: Curved Course    grid 40 x 20")
            print("2. Track 2: Diagonal Course  grid 4 x 4")
            print("3. Track 3: Sharp Turns      grid 10 x 7")
            print("4. Track 4: Open Space       grid 50 x 50")
            print("q. Exit program\n")
            track_option = input("Enter your option: ").strip()

            if track_option.lower() == "q":
                print("Goodbye!\n")
                return None
            elif track_option not in ["1", "2", "3", "4"]:
                print("Invalid option. Please choose 1-4 or q.\n")
            else:
                return track_option
    
    def select_vehicle(self):
        while True:
            print("# Select Vehicle")
            print("1. Vehicle 1: Car            4 degrees of motion")
            print("2. Vehicle 2: Crawler        8 degrees of motion")
            print("q. Exit program\n")
            vehicle_option = input("Enter your option: ").strip()

            if vehicle_option.lower() == "q":
                print("Goodbye!\n")
                return None 
            elif vehicle_option.lower() not in ["1", "2"]:
                print("Invalid option. Please choose 1-2 or q.\n")
            else:
                return vehicle_option

"""
RaceTrack calls ReadTrackFile and maps the track.
"""

class RaceTrack:
    def __init__(self, filename):
        race_track = ReadTrackFile(FILEPATH, filename)
        self.race_track_map = race_track.load_track()

        if not self.race_track_map:
            raise ValueError("File doesn't contain a race track.")

        self.height = len(self.race_track_map)
        self.width = len(self.race_track_map[0])
        self.start = (0, 0)
        self.finish = (self.width - 1, self.height - 1)

        self.walls = set()
        self._parse_track()


    def _parse_track(self):                             # Identify the walls (non-empty positions) in the track file.
        for y, row in enumerate(self.race_track_map):
            for x, char in enumerate(row):
                if char != ' ':
                    self.walls.add((x, y))


    def step(self, current_state, action):              # Geeksforgeeks
        y, x = divmod(current_state, self.width)

        new_x, new_y = x, y

        if action == 0:     # Left
            new_x -= 1
        elif action == 1:   # Right
            new_x += 1
        elif action == 2:   # Up
            new_y -= 1
        elif action == 3:   # Down
            new_y += 1
        elif action == 4:   # Left and up
            new_x -= 1
            new_y -= 1
        elif action == 5:   # Right and down
            new_x += 1
            new_y += 1
        elif action == 6:   # Left and down
            new_x -= 1
            new_y += 1
        elif action == 7:   # Right and up
            new_x += 1
            new_y -= 1      

        done = False
        reward = -1

        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            new_x, new_y = x, y
            reward = -100

        elif (new_x, new_y) in self.walls:
            new_x, new_y = x, y
            reward = -100

        elif (new_x, new_y) == self.finish:
            reward = 1000
            done = True

        next_state = (new_y * self.width) + new_x

        return next_state, reward, done

"""
ReadTrackFile is used to read a file and store it in a list.
"""

class ReadTrackFile:
    def __init__(self, fp, fn):
        self.filepath = fp
        self.filename = fn
        self.fullname = f"{self.filepath}{self.filename}"


    def load_track(self):
        with open(self.fullname, 'r', encoding='utf-8') as file:
            self.track_data = [line.strip('\n') for line in file.readlines()]
        return self.track_data

"""
State Space (ss) is defined as the size of the track.
Action Space is 4 for Car; left, right, up, down.
Action Space is 8 for Crawler; left, right, up, down, left/up, righht/down, left/down, right/up.
"""

class QTable:
    def __init__(self, ss, action_space):
        self.table = np.zeros((ss,action_space))

"""
"""

class Vehicle:
    def __init__(self, lr, df, ep, epo, ss, dim, action_names):
        self.learning_rate = lr
        self.discount_factor = df
        self.exploration_prob = ep
        self.epochs = epo
        self.dimensions = dim
        self.action_names = action_names
        self.qtable = QTable(ss, dim)

    def learn(self, track):
        start_x, start_y = track.start
        start_index = (start_y * track.width) + start_x

        min_steps = float('inf')
        max_steps = 2000                                    # Prevent infinite loops
        
        for epoch in range(self.epochs): 
            current_state = start_index
            done = False
            steps = 0

            while not done and steps < max_steps:
                    
                if np.random.rand() < self.exploration_prob:
                    action = np.random.randint(0, self.dimensions)          # Explore
                else:
                    action = np.argmax(self.qtable.table[current_state])    # Exploit

                next_state, reward, done = track.step(current_state, action)

                # Bellman equation for updating QTable
                
                self.qtable.table[current_state, action] += self.learning_rate * (reward + self.discount_factor * np.max(self.qtable.table[next_state]) - self.qtable.table[current_state, action])

                current_state = next_state
                steps += 1

            if done and steps < min_steps:
                min_steps = steps

        if min_steps != float('inf'):
            print(f"Shortest route: {min_steps}")
        else:
            print("Goal never reached.")

"""
Vehicles
"""

class Car(Vehicle):
    def __init__(self, lr, df, ep, epo, ss):
        actions = ['Left', 'Right', 'Up', 'Down']
        super().__init__(lr, df, ep, epo, ss, dim = 4, action_names = actions)

class Crawler(Vehicle):
    def __init__(self, lr, df, ep, epo, ss):
        actions = ['Left', 'Right', 'Up', 'Down', 'Left/Up', 'Right/Down', 'Left/Down', 'Right/Up']
        super().__init__(lr, df, ep, epo, ss, dim = 8, action_names = actions)

def main():
    # Call UserInterface to let user select track and vehicle.
    ui = UserInterface()

    track_files = {
        "1": "Track1.txt",
        "2": "Track2.txt",
        "3": "Track3.txt",
        "4": "Track4.txt"
    }

    try:
        while True:

            track_option = ui.select_track()

            if track_option is None:
                break

            filename = track_files.get(track_option)

            # Read the track file, print track data, print track layout.

            try:
                my_track = RaceTrack(filename)
            except FileNotFoundError:
                if not os.path.exists(FILEPATH):
                    print(f"{FILEPATH} does not exist.")
                    print("Exiting program!\n")
                    break
                else:
                    print(f"{filename} does not exist.")
                    print("Please select another race track.\n")
                    continue
            except ValueError as e:
                print(f"Error in {filename}: {e}")
                print("Please select another race track.\n")
                continue


            vehicle_option = ui.select_vehicle()

            if vehicle_option is None:
                break

            print("Visual presentation of the track:\n")
            for line in my_track.race_track_map:
                print(line)
            print()

            # Calculate the state space, ss.

            ss = (my_track.width * my_track.height)

            if vehicle_option == "1":
                my_vehicle = Car(learning_rate, discount_factor, exploration_prob, epochs, ss)
            elif vehicle_option == "2":
                my_vehicle = Crawler(learning_rate, discount_factor, exploration_prob, epochs, ss)
                        
            my_vehicle.learn(my_track)
                
            df_qtable = pd.DataFrame(my_vehicle.qtable.table, columns = my_vehicle.action_names)
            df_qtable.index.name = 'State'

            #pd.set_option('display.max_rows', None)

            df_filtered = df_qtable.loc[(df_qtable != 0).any(axis=1)]

            print("Updated Q-table (Filtered):")
            print(df_filtered.round(2))
            print()

    except KeyboardInterrupt:
        print("\nUser interruption!\n")
    
if __name__ == "__main__":
    main()