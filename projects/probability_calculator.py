# Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

# For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

# First, create a Hat class in main.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

# The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

# Next, create an experiment function in main.py (not inside the Hat class). This function should accept the following arguments:

# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.

# For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

# Here is how you would call the experiment function based on the example above with 2000 experiments:

# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)
# The output would be something like this:

# 0.356
# Since this is based on random draws, the probability will be slightly different each time the code is run.

# Hint: Consider using the modules that are already imported at the top. Do not initialize random seed within the file.

import copy
import random

# Define a class called Hat
class Hat:

  # Initialize the Hat object with a dictionary of colors and their counts
  def __init__(self, **kwargs):
    # Initialize an empty list to store the contents of the hat
    self.contents = []
    # Iterate through the key-value pairs in the input dictionary
    for key, value in kwargs.items():
      # Extend the contents list with 'value' number of 'key' elements
      self.contents.extend([key] * value)

  # Define a method to draw a specified number of balls from the hat
  def draw(self, number):
    # If the number requested is greater than or equal to the total number of balls, return a copy of all the balls
    if number >= len(self.contents):
      return self.contents.copy()
    balls = []
    # Iterate 'number' times to draw that many balls
    for _ in range(number):
      # Generate a random index to select a ball from the contents list
      choice = random.randrange(len(self.contents))
      # Append the selected ball to the balls list and remove it from the contents
      balls.append(self.contents.pop(choice))
    return balls

# Define a function called experiment to perform experiments with the hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # Create a list of expected ball counts based on the expected_balls dictionary
  expected_counts = [expected_balls[key] for key in expected_balls]
  successes = 0

  # Repeat the experiment 'num_experiments' times
  for _ in range(num_experiments):
    # Create a deep copy of the original hat to avoid modifying it
    new_hat = copy.deepcopy(hat)
    # Draw 'num_balls_drawn' balls from the new hat
    balls = new_hat.draw(num_balls_drawn)

    # Count the occurrences of each expected ball in the drawn balls
    ball_counts = [balls.count(key) for key in expected_balls]

    # Check if all the actual counts are greater than or equal to the expected counts
    if all(
        ball_count >= expected_count
        for ball_count, expected_count in zip(ball_counts, expected_counts)):
      successes += 1

  # Calculate the probability of success and return it
  return successes / num_experiments