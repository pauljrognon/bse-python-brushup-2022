from typing import Union

class Car:
    def __init__(self, color: str, horse_power: int, location: Union[int, float] = 0) -> None:  # class constructor
        self.color = color
        self.horse_power = horse_power
        self.location = location
        
    def drive(self, direction: str, distance: Union[int, float]) -> None:  # class method
        if direction not in ['left', 'right']:
            raise ValueError('Direction has to be either "left" or "right".')
        self.location = self.location + 2 * ((direction == 'right') - 1 / 2) * distance
        print(f"We drive the car towards {direction} direction by {distance}")

        
if __name__ == '__main__':  # this part of the code runs when we execute the script through the command line
    car = Car('pink', 88)
    car.drive('left', 1)
    print(car.location)