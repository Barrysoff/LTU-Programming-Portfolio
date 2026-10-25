"""
Course D0045E
OOP design part 2 - Car racing - Unit test

Unit test for race_track.py.

Author: Mattias Westermark

Note: Gemini has been used as a sounding board
in accordance with the allowed aids policy.
"""

import unittest

import numpy as np
from unittest.mock import patch

from race_track import RaceTrack
from race_track import ReadTrackFile
from race_track import QTable
from race_track import Vehicle
from race_track import Car
from race_track import Crawler


class Test_ReadTrackFile(unittest.TestCase):

    def test_initialization(self):
        """
        Test the ability to concatenate a filepath and a filename to a complete path.
        """

        fp = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/"
        fn = "Track1.txt"
        rtf = ReadTrackFile(fp, fn)

        test_fullname = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/Track1.txt"
        self.assertEqual(rtf.fullname, test_fullname)

    def test_load_track_file_not_found(self):
        """
        Test error handling when trying to load a non-existing file.
        """

        fp = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/"
        fn = "No_file.txt"
        rtf = ReadTrackFile(fp, fn)

        with self.assertRaises(FileNotFoundError):
            rtf.load_track()

    def test_load_track_file_found(self):
        """
        Load a track file and confirm reading.
        """

        fp = "/workspaces/LTU-Programming-Portfolio/d0045e_ht2026/race_track/"
        fn = "Track2.txt"
        rtf = ReadTrackFile(fp, fn)

        read_track = rtf.load_track()

        test_track = [  # Visual view of track 2.
            "  XX",
            "X  X",
            "XX  ",
            "XXX " 
        ]

        self.assertEqual(read_track, test_track)


class Test_RaceTrack(unittest.TestCase):

    def test_initialization(self):
        """
        Test the interpretation of a race track.
        """

        fn = "Track1.txt"
        rt = RaceTrack(fn)

        self.assertEqual(rt.height, 20)
        self.assertEqual(rt.width, 40)
        self.assertEqual(rt.start, (0, 0))
        self.assertEqual(rt.finish, (rt.width - 1, rt.height - 1))

    
    def test_initialization_empty_file(self):
        """
        Test error handling when trying to load an empty file.
        """

        fn = "Track0.txt"   # Track 0 contains no data.

        with self.assertRaises(ValueError):
            rt = RaceTrack(fn)


    def test_parse_track(self):
        """
        Test the ability to identify walls and open spaces in a track file.
        """

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        # Verify location of walls. 'x' marks tested location.

        self.assertIn((2, 0), rt.walls)     # 1 row: __xX
        self.assertIn((3, 0), rt.walls)     # 1 row: __Xx
        self.assertIn((0, 1), rt.walls)     # 2 row: x__X
        self.assertIn((3, 1), rt.walls)     # 2 row: X__x
        self.assertIn((0, 2), rt.walls)     # 3 row: xX__
        self.assertIn((1, 2), rt.walls)     # 3 row: Xx__
        self.assertIn((0, 3), rt.walls)     # 4 row: xXX_
        self.assertIn((1, 3), rt.walls)     # 4 row: XxX_
        self.assertIn((2, 3), rt.walls)     # 4 row: XXx_

        # Verify location of open areas. '-' marks tested location.

        self.assertNotIn((0, 0), rt.walls)  # 1 row: -_XX
        self.assertNotIn((1, 0), rt.walls)  # 1 row: _-XX
        self.assertNotIn((1, 1), rt.walls)  # 2 row: X-_X
        self.assertNotIn((2, 1), rt.walls)  # 2 row: X_-X
        self.assertNotIn((2, 2), rt.walls)  # 3 row: XX-_
        self.assertNotIn((3, 2), rt.walls)  # 3 row: XX_-
        self.assertNotIn((3, 3), rt.walls)  # 4 row: XXX-


    def test_step_valid_movement(self):
        """
        Test movement along a valid path.
        """

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_state = 0                      # Standing left of open space
        test_action = 1                     # Move right into open space

        next_state, reward, done = rt.step(test_state, test_action)

        self.assertEqual(next_state, 1)     # Move one step right
        self.assertEqual(reward, -1)        # Reward for correct move
        self.assertEqual(done, False)       # Epoch is not finished


    def test_step_invalid_movement(self):
        """
        Test movement into a wall.
        """

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_state = 1                      # Standing left of a wall
        test_action = 1                     # Move right into a wall

        next_state, reward, done = rt.step(test_state, test_action)

        self.assertEqual(next_state, 1)     # Move one step right
        self.assertEqual(reward, -100)      # Reward for colliding with a wall
        self.assertEqual(done, False)       # Epoch is not finished


    def test_step_finish_movement(self):
        """
        Test movement into finish.
        """

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_state = 11                     # Standing above finish
        test_action = 3                     # Move down into finish

        next_state, reward, done = rt.step(test_state, test_action)

        self.assertEqual(next_state, 15)    # Move one step down
        self.assertEqual(reward, 1000)      # Reward for reaching the goal
        self.assertEqual(done, True)        # Epoch complete


class Test_QTable(unittest.TestCase):

    def test_initialization(self):
        """
        Test creation of QTable filled with 0.
        """

        test_state_space = 4
        test_action_space = 5

        test_table = QTable(test_state_space, test_action_space)

        self.assertEqual(test_table.table.shape, (test_state_space, test_action_space))
        self.assertTrue(np.all(test_table.table == 0))  # Compare all cell values with 0.


class Test_Vehicle(unittest.TestCase):

    def test_initialization(self):
        """
        Test initialization of Vehicle. 
        """
        
        test_ss = 16
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_vehicle = Vehicle(test_ss, test_dim, test_action_names)

        self.assertEqual(test_vehicle.learning_rate, 0.8)
        self.assertEqual(test_vehicle.discount_factor, 0.95)
        self.assertEqual(test_vehicle.exploration_prob, 0.2)
        self.assertEqual(test_vehicle.epochs, 10000)
        self.assertEqual(test_vehicle.dimensions, test_dim)
        self.assertEqual(test_vehicle.action_names, test_action_names)
        self.assertEqual(test_vehicle.epsilon_decay, 0.99)
        self.assertIsNotNone(test_vehicle.qtable)


    def test_learn_update_qtable(self):
        """
        Test to see that the QTable gets updated after an epoch.
        """
        
        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_ss = rt.height * rt.width
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_vehicle = Vehicle(test_ss, test_dim, test_action_names, epochs = 5)

        last_qtable = np.copy(test_vehicle.qtable.table)

        test_vehicle.learn(rt)

        self.assertFalse(np.array_equal(test_vehicle.qtable.table, last_qtable)) # Initial and last QTable should be equal

    @patch("numpy.random.rand")
    @patch("numpy.random.randint")
    def test_learn_explore(self, mock_randint, mock_rand):
        """
        Test to see that the Explore path is followed.
        The use of @patch and mock after suggestion from Gemini.
        """
        
        mock_rand.return_value = 0.0    # Hardcoded random number to force exploration
        mock_randint.return_value = 0

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_ss = rt.height * rt.width
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_vehicle = Vehicle(test_ss, test_dim, test_action_names, epochs = 1)

        test_vehicle.learn(rt)
        mock_randint.assert_called()


    @patch("numpy.random.rand")
    @patch("numpy.random.randint")
    def test_learn_exploit(self, mock_randint, mock_rand):
        """
        Test to see that the Exploitation path is followed.
        The use of @patch and mock after suggestion from Gemini.
        """
        
        mock_rand.return_value = 1.0    # Hardcoded random number to force exploitation.
        mock_randint.return_value = 0

        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_ss = rt.height * rt.width
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_vehicle = Vehicle(test_ss, test_dim, test_action_names, epochs = 1)

        test_vehicle.learn(rt)
        mock_randint.assert_not_called()


    def test_learn_epsilon_decay(self):
        """
        Test to see that exploration_prob gets smaller for each epoch.
        """
        
        fn = "Track2.txt"
        rt = RaceTrack(fn)

        test_ss = rt.height * rt.width
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_vehicle = Vehicle(test_ss, test_dim, test_action_names, epochs = 10) # Epochs must be less than stale_threshold.

        start_exploration_prob = test_vehicle.exploration_prob

        test_vehicle.learn(rt)

        final_exploaration_prob = test_vehicle.exploration_prob

        self.assertAlmostEqual(final_exploaration_prob, (start_exploration_prob * (test_vehicle.epsilon_decay ** test_vehicle.epochs)), 5)


class Test_Car(unittest.TestCase):
    
    def test_initialization(self):
        """
        Test the initialization of Car, a child of Vehicle.
        """
        
        test_ss = 16
        test_dim = 4
        test_action_names = ["Left", "Right", "Up", "Down"]

        test_car = Car(test_ss)

        self.assertEqual(test_car.learning_rate, 0.8)
        self.assertEqual(test_car.discount_factor, 0.95)
        self.assertEqual(test_car.exploration_prob, 0.2)
        self.assertEqual(test_car.epochs, 10000)
        self.assertEqual(test_car.dimensions, test_dim)
        self.assertEqual(test_car.action_names, test_action_names)
        self.assertEqual(test_car.epsilon_decay, 0.99)
        self.assertIsNotNone(test_car.qtable)


class Test_Crawler(unittest.TestCase):
    
    def test_initialization(self):
        """
        Test the initialization of Crawler, a child of Vehicle.
        """
        
        test_ss = 16
        test_dim = 8
        test_action_names = ["Left", "Right", "Up", "Down", "Left/Up", "Right/Down", "Left/Down", "Right/Up"]

        test_crawler = Crawler(test_ss)

        self.assertEqual(test_crawler.learning_rate, 0.8)
        self.assertEqual(test_crawler.discount_factor, 0.95)
        self.assertEqual(test_crawler.exploration_prob, 0.2)
        self.assertEqual(test_crawler.epochs, 10000)
        self.assertEqual(test_crawler.dimensions, test_dim)
        self.assertEqual(test_crawler.action_names, test_action_names)
        self.assertEqual(test_crawler.epsilon_decay, 0.99)
        self.assertIsNotNone(test_crawler.qtable)


if __name__ == "__main__":
    unittest.main(verbosity=2)  # Verbosity to get some output from the tests.