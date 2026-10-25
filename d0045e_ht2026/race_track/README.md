race_track.py: a Q-Learning race track simulation.

Course: D0045E Programming in Python: Code Quality and Best Practices (OOP assignment part 2)
Author: Mattias Westermark

OVERVIEW

This project is about Q-Learning and this is implemented on a vehicle learning the best
way through a race track. There are several tracks and two vehicle types to choose from.

HOW THE PROGRAM WORKS

1. Select a track and a vehicle.
2. Traverse the selected track repeatedly. Stop each run when reaching the goal or when 
   the goal hasn't been reached before a pre-defined limit.
3. Each consecutive run populates the algorithm's QTable.
4. The steps are repeated until
   - The preset number of runs (epochs) has been reached.
   - There is no change in the QTable over a preset number of runs.

PROJECT STRUCTURE

The project is built upon interacting classes:

- Class UserInterface

UserInterface prints user menus and takes user input for selecting race track and vehicle.

- Class ReadTrackFile

ReadTrackFile is responsible for file management and reading track files. The Class creates proper search paths,
reads track files and converts layouts to a list of list which is used to generate the track in RaceTrack.

- Class RaceTrack

RaceTrack uses the list from ReadFileTrack to generate a track with identified walls and open roads. RaceTrack traverses 
the race track and gives the reward for each action taken.

- Class QTable

QTable is initially filled with zeroes and later updated for each epoch completed.

- Class vehicle

Vehicle manages the movement of the selected vehicle and handles the training of the selected vehicle. Training can be
explorative (random) or exploitive. The randomness decreases with each epoch done.

When no change in the QTable has been detected for a preset number of epochs, the learning process is considered complete.

- Class Car(Vehicle)

Car is a vehicle with four degrees of freedom; left, right, up, and down.

- Class Crawler(Vehicle)

Crawler is a more dynamic vehicle with eight degrees of freedom. Crawler can move diagonally as well as left, right, up, and down.

DEPENDENCIES
numpy   - used for matrix and numerical manipulation
pandas  - used for presentation in table format
os      - used for file location control
time    - used for performace testing