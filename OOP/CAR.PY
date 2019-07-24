class Car:
    def __init__(self,regno,no_gears):
        self.regno =  regno
        self.no_gears = no_gears
        self.is_started =False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"{self.regno} is already started")
        else:
            print(f"Car with reg no.:{self.regno} started...")
            self.is_started =True

    def stop(self):
        if self.is_started:
            print(f"Car with reg no.:{self.regno} stopped...")
            self.is_started =False

        else:
            print(f"Car with reg no.:{self.regno} already stopped...")

    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear+=1
                print(f"Car with reg no.:{self.regno} Changed gear.")
            else:
                print("Car is already in top gear")
        else:
            print(f"Car with reg no.:{self.regno} already stopped,you can't change gears.")
    def showInfo(self):
        print(f"{self.regno} started. Gears:{self.no_gears}. no. of Gears:{self.c_gear}")

    

