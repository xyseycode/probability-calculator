import copy
import random
# Consider using the modules imported above.

# My codes can be shortened by using comprehensions


class Hat:

  def __init__(self, **kwargs):
    self.kwargs = kwargs
    self.contents = []
    for arg in self.kwargs.items():
      for _ in range(arg[1]):
        self.contents.append(arg[0])

  def draw(self, num_draws):
    if num_draws > len(self.contents):
      return self.contents

    balls = []
    for _ in range(num_draws):
      balls.append(
          self.contents.pop(self.contents.index(random.choice(self.contents))))

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  lucky_draw = 0
  for _ in range(num_experiments):
    hat_experiment = copy.deepcopy(hat)
    balls_drawn = hat_experiment.draw(num_balls_drawn)
    count = 0
    for k, v in expected_balls.items():
      if balls_drawn.count(k) >= v:
        count += 1
      else:
        break
    if count == len(expected_balls):
      lucky_draw += 1

  return lucky_draw / num_experiments
