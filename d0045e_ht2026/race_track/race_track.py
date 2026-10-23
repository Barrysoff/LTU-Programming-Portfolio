"""
Course D0045E
OOP design part 2 - Car racing

Train a race car to move from top left corner to bottom right corner, in the
shortest way possible. Q-Learning (reinforcement learning) is used to train
the model.

The program measures time to train, and calculates the difference between
QTable(n) and QTable(n-1) for an early stop function.

Author: Mattias Westermark

Note: Gemini has been used as a sounding board
in accordance with the allowed aids policy.

Reference sites:
https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial
https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/
https://realpython.com/python-profiling/
"""

import numpy as np
import pandas as pd
import os
import time

"""
Global constant for path to folder containing race track in txt-format.
Update FILEPATH if working in other locations.
"""

FILEPATH = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/"

class UserInterface:
    """
    Simple user interface function for presenting the user with race track and vehicle selection choices.

    The main steps of the implementation:
        - Print menu with choices
        - Wait for user input
        - validates user input
        - Return choices alternatively end execution        
    """

    def __init__(self):
        pass


    def runMenu(self):
        """
        Main function for calling race track and vehicle selection menus.

        Returns user choices.
        """

        track = self._select_track()
        if track is None:
            return None, None
        vehicle = self._select_vehicle()
        if vehicle is None:
            return None, None

        return track, vehicle


    def select_track(self):
        """
        Prints the race track selection menu.
        Wait for user input.
        Validate user input.
            - Repeat if invalid input.
            - Continue if valid input.
        """

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
        """
        Prints the vehicle selection menu.
        Wait for user input.
        Validate user input.
            - Repeat if invalid input.
            - Continue if valid input.
        """

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


class RaceTrack:
    """
    RaceTrack handles the loading and interpretation of race tack data as well as movement through the race track.

    The main steps of the implementation:
        - Load the selected race track.
        - Calculate map size and locate start and finish locations.
        - Locate drivable parts as well as blocked areas.
        - Set next location based on current location and algorithm input.

    Additional information:
        - The implementation expect the race track to be a rectangular grid.
    """


    def __init__(self, filename):
        """
        Initialize the RaceTrack instance.

        Arguments:
            filename: the filename corresponding to the user selected Race Track.
        """

        race_track = ReadTrackFile(FILEPATH, filename)
        self.race_track_map = race_track.load_track()

        if not self.race_track_map:
            raise ValueError("File doesn't contain a race track.")

        self.height = len(self.race_track_map)
        self.width = len(self.race_track_map[0])
        self.start = (0, 0)                             # Start hard coded to upper left corner
        self.finish = (self.width - 1, self.height - 1) # Finish hard coded to the bottom right corner

        self.walls = set()
        self._parse_track()


    def _parse_track(self):
        """
        Loop through all positions/characters of the Race Track file.
        Non-space characters are a wall that can't be passed.
        """

        for y, row in enumerate(self.race_track_map):
            for x, char in enumerate(row):
                if char != ' ':
                    self.walls.add((x, y))


    def step(self, current_state, action):
        """
        Step moves the vehicle from one state (location) to another state (location).

        Arguments:
            current_state: the position of the vehicle.
            action: directional movement

        Returns:
            next_state: will be the starting state (location) for the next iteration.
            reward: negative or positive depending on the performance on the race track.
            done: stop the epoch if True.
        """

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
        reward = -1         # Negative reward for moving through open space

        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            new_x, new_y = x, y
            reward = -100   # Negative reward for moving outside the race track

        elif (new_x, new_y) in self.walls:
            new_x, new_y = x, y
            reward = -100   # Negative reward for colliding with a wall.

        elif (new_x, new_y) == self.finish:
            reward = 1000   # Positive reward for reaching the finish.
            done = True

        next_state = (new_y * self.width) + new_x

        return next_state, reward, done


class ReadTrackFile:
    """
    ReadTrackFile handles the file IO for reading data from file.
    """

    def __init__(self, fp, fn):
        """
        Initialize the ReadFileTrack instance.

        Arguments:
            fp: the path to the directory containing the track files.
            fn: the name of the race track file.
        """

        self.filepath = fp
        self.filename = fn
        self.fullname = f"{self.filepath}{self.filename}"


    def load_track(self):
        """
        load_track opens the track file for reading.

        Returns:
            Track data in a list of strings.
        """

        with open(self.fullname, 'r', encoding='utf-8') as file:
            self.track_data = [line.strip('\n') for line in file.readlines()]
        return self.track_data

"""
State Space (ss) is defined as the size of the track.
Action Space is 4 for Car; left, right, up, down.
Action Space is 8 for Crawler; left, right, up, down, left/up, righht/down, left/down, right/up.
"""

class QTable:
    """
    Qtable builds the initial QTable, inhabited by zeroes. 
    """

    def __init__(self, ss, action_space):
        """
        Initialize the QTable instance.

        Arguments:
            ss: state space, the size if the Race Track.
            action_space: the number of movements for the selected Vehicle.    
        """

        self.table = np.zeros((ss,action_space))


class Vehicle:
    """
    Define the behaviour of the vehicles and the learning model.

    The main steps of the implementation:
        - Initialize the function with hyperparameters
        - Run the learning model 
    """
            
    def __init__(self, ss, dim, action_names, learning_rate = 0.8, discount_factor = 0.95, exploration_prob = 0.2, epochs = 10000, epsilon_decay = 0.99):
        """
        Initialize the Vehicle class.

        Arguments:
            ss: state space, size of the race track
            dim: degrees of freedom for the selected 
            action_names: directional names of Vehicle movements.
            learning_rate: how much new info overrides old info.
            discount_factor: how much future rewards are valued.
            exploration_prob: probability of taking a random action.
            epochs: number of training episodes.
            epsilon_decay: decrease exploration rate
        """

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.epochs = epochs
        self.dimensions = dim
        self.action_names = action_names
        self.epsilon_decay = epsilon_decay
        self.qtable = QTable(ss, dim)


    def learn(self, track):
        """
        The training model for the Vehicles. Training continues until no changes in the Qtable can be detected for a defined number of iterations.

        The Bellamn Equation is used for updating the QTable.

        Arguments:
            track: the track selected by the user.
        """

        start_x, start_y = track.start
        start_index = (start_y * track.width) + start_x     # start_index is a 2D position.

        min_steps = float('inf')                            # Initialize min_steps with an infinitemal number
        max_steps = 2000                                    # Prevent infinite loops
        last_qtable = np.copy(self.qtable.table)            # Used for (n) to (n-1) comparision of the QTable
        stale_epochs = 0                                    # How many continous epochs without a change in the QTable has there been?
        stale_threshold = 100                               # How many continous epochs without a change in the QTable is considered a completed run?
        
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

                """ Bellman equation for updating QTable """
                
                self.qtable.table[current_state, action] += self.learning_rate * (reward + self.discount_factor * np.max(self.qtable.table[next_state]) - self.qtable.table[current_state, action])

                current_state = next_state
                steps += 1

            """
            Calculate the difference between current (n) and previous (n-1) QTable using element matrix subtraction.
            Pick out the single largest absolute value, delta.
            If delta is smaller than a defined limit, the QTable is considered stale (stable).
            After stale_threshold stale runs, the learning model is considered to be complete.
            """

            if done:
                delta = np.max(np.abs(self.qtable.table - last_qtable))
                if delta < 1e-5:
                    stale_epochs += 1
                else:
                    stale_epochs = 0

                last_qtable = np.copy(self.qtable.table)

                if stale_epochs >= stale_threshold:
                    print(f"Shortest route found. Stopping after {epoch + 1} epochs.")

                    break

            if done and steps < min_steps:
                min_steps = steps

            self.exploration_prob = self.exploration_prob * self.epsilon_decay  # Increase focus on exploitation each run.

        if min_steps != float('inf'):
            print(f"Shortest route: {min_steps}")
        else:
            print("Goal never reached.")


class Car(Vehicle):
    """
    Car is a child of Vehicle.
    """

    def __init__(self, ss, **kwargs):
        """
        Initialize the Car instance.

        Arguments:
            ss: state space
            **kwargs: keyword arguments

        Note:
            The car has 4 degrees of freedom
        """

        actions = ['Left', 'Right', 'Up', 'Down']
        super().__init__(ss, dim = 4, action_names = actions, **kwargs)


class Crawler(Vehicle):
    """
    Crawler is a child of Vehicle.
    """

    def __init__(self, ss, **kwargs):
        """
        Initialize the Crawler instance.

        Arguments:
            ss: state space
            **kwargs: keyword arguments

        Note:
            The Crawler has 8 degrees of freedom.
        """

        actions = ['Left', 'Right', 'Up', 'Down', 'Left/Up', 'Right/Down', 'Left/Down', 'Right/Up']
        super().__init__(ss, dim = 8, action_names = actions, **kwargs)

def main():
    """
    Main is keeping all together:

        - Initialize user interface
        - Read track data
        - Initialize learning
        - Presents results

    Note:
        - Error handling (try/except) is used for reading data from file.
        - Performance is measured by timing the learning module.
    """

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

            ss = (my_track.width * my_track.height)

            if vehicle_option == "1":
                my_vehicle = Car(ss)
            elif vehicle_option == "2":
                my_vehicle = Crawler(ss)

            start_time = time.perf_counter()          
            my_vehicle.learn(my_track)
            end_time = time.perf_counter()

            learn_time = end_time - start_time
 
            df_qtable = pd.DataFrame(my_vehicle.qtable.table, columns = my_vehicle.action_names)
            df_qtable.index.name = 'State'

            df_filtered = df_qtable.loc[(df_qtable != 0).any(axis=1)] # Filter out states corresponding to walls.

            print("Updated Q-table (Filtered):")
            print(df_filtered.round(2))
            print()

            print(f"Vehicle {vehicle_option} needed {learn_time:.4f} seconds to optimise track {track_option}.\n")

    except KeyboardInterrupt:
        print("\nUser interruption!\n")
    
if __name__ == "__main__":
    main()