import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
  

    def draw(self, number):
        balls_drawn = []
        if number > len(self.contents):
            return self.contents
        for i in range(number):
            ball = random.randint(0, (len(self.contents)-1))
            balls_drawn.append(self.contents[ball])
            self.contents.remove(self.contents[ball])
        return balls_drawn
                    
        #remove one ball at random and add to a new list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    
    hat_copy = copy.deepcopy(hat)
    expected_balls_copy = copy.deepcopy(expected_balls)

    colours_drawn = hat_copy.draw(num_balls_drawn)

    for colours in colours_drawn:
      if colours in expected_balls_copy.keys():
        expected_balls_copy[colours] -= 1

    if all (x <= 0 for x in expected_balls_copy.values()):
      count += 1

  return count / num_experiments
  