from dataclasses import dataclass


@dataclass
class Car:
    fuel: float = 100
    distance: float = 0

    def show_tank(self):
        print(f"The car contains {self.fuel} liters of gasoline.")
        print("-" * 50)

    def drive(self, km: float):
        potential: float = self.fuel * 100 / 5
        driven = min(potential, km)
        self.fuel -= driven / 100 * 5
        self.distance += driven

        print(f"You drove {'only ' if potential < km else ''}{driven} kilometers.")

        if self.fuel >= 10:
            print(f"The car has {self.fuel} liters of gasoline left.")
        elif 10 > self.fuel > 0:
            print(f"You are almost out of fuel! The car has {self.fuel} liters of gasoline left.")
        else:  # self.fuel == 0
            print(f"You're out of fuel! Please fill up the tank.")

        print("-" * 50)

    def refuel(self):
        self.fuel = 100
        self.distance = 0
        print("Your tank is full, you can go.")
        print("-" * 50)

    def driven_distance(self):
        print(f"You drove a total of {self.distance} kilometers since last fill-up.")
        print("-" * 50)


if __name__ == "__main__":
    my_car = Car()

    my_car.show_tank()
    my_car.drive(50)
    my_car.drive(1000)
    my_car.driven_distance()
    my_car.drive(875)
    my_car.driven_distance()
    my_car.drive(100)
    my_car.driven_distance()
