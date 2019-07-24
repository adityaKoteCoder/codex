class car:
    def __init__(self,mode1,regno,no_gears):
        self.model = model
        self.regno=regno
        self.no_gears=no_gears
        self.is_started= False
        self.c_gear=0

    def start(self):
        if self.is_started:
            print(f"{self.regno} already Started")
        else:
            print(f"{self.regno} Started")
            self.is_started= True

    def stop(self):
        if self.is_started:
            print(f"{self.regno} stopped")
            self.is_started= False 
        else:
            print(f"{self.regno} already stopped")
        
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"{self.regno} changed gear")
            else:
                print(f"{self.regno} Car has reached top gear")

          
        else:
            print(f"{self.regno} already stopped gear")
        

if __name__ == "__main__":
    bmw = car("Ka01300",5)
    audi = car("Ka01323",5)

    bmw.start()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.stop()

    audi.start()
    audi.change_gear()
    audi.change_gear()
    audi.change_gear()
    audi.change_gear()
    audi.change_gear()

    audi.stop()
