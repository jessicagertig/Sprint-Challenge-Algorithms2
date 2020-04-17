class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_towards_the_end(self):
        """
        Returns True if the robot can move towards_the_end or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_towards_the_start(self):
        """
        Returns True if the robot can move towards_the_start or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_towards_the_end(self):
        """
        If the robot can move to the towards_the_end, it moves to the towards_the_end and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_towards_the_start(self):
        """
        If the robot can move to the towards_the_start, it moves to the towards_the_start and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        #Goal: sort list
        #Robot methods: move towards the end, move towards the start, pick up/swap items, compare item held with item in front of
        #Robots light has 3 methods: set it to on(True), set it to off(False), check if light_is_on returns true or false
        
        #Plan
        #set robot's light to on(indicates the sorting is in progress)
        #the robot starts out holding none, none will be used as a placeholder as each swap occurs
        # pick up first item (index 0 will then contain 'None')
        # move towards end (to next index)
        # call compare_item: 
        # if it returns 1 (held item is greater than item in front of robot) move towards end again 
        # if it returns -1 (held item is less than item in front robot) call swap_item
        # keep going until move towards the end returns false,
        # then move towards the start
        # new conditional, if compare returns 1, swap, if compare return -1, move to start, compare, if compare returns none, swap
        self.set_light_on()
        self.swap_item()
        # self.move_towards_the_end()
        while self.light_is_on() == True:
            if self.can_move_towards_the_end() == True:
                self.move_towards_the_end()
                if self.compare_item() == -1:
                    self.swap_item()
                    self.set_light_on()
                elif self.compare_item() == 1 and self.can_move_towards_the_end() == False:
                    self.swap_item()
                    self.set_light_off()
        while self.light_is_on() == False:
            if self.can_move_towards_the_start() == True:
                self.move_towards_the_start()        
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_towards_the_start()    
                elif self.compare_item() == None:
                    self.swap_item()
                    self.set_light_on()
                
        



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    # l = [15, 49, 26, 4]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)