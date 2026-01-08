from abc import ABC, abstractmethod
class Meal(ABC):
    @abstractmethod
    def prepare():
       pass
class Pizza(Meal):
    def prepare():
         print("""preparing the dough(mxing, kneading, rising), 
                 preheating the oven very hot(475 F)
                 Shaping the dough
                 adding sauce, cheese and toppings 
                 baking until golden and bubly, usualy 10-20 minutes on store or pan """)


class Salad(Meal):
    def prepare():
        print("""Make sure your greens are dry. 
                 Lay your greens out on a towel to air-dry for a little while.
                 Tear up your greens. ...
                 Toss it in a mixing bowl.
                 Add grated vegetables and chopped herbs.
                 Prepare your salad dressing. ...
                 Drizzle your salad with dressing. ...
                 Sprinkle on salt and pepper.""")
        