#Valeria Rico
#Assignment 10.1: Your own class
#Credit to Professor Hari, "Intro to python"


class RollerCoaster:
    motor = True
    wheels =3
    def __init__(self,color, seats =4, speed_m_s=150):
        self.color = color
        self.seats = seats
        self.__speed = speed_m_s
        self.__position = 0

    def foward(self):
        self.__position += self.__speed
    def backwards(self):
        self.__position -= self.__speed

    def starting_speed(self, speed):
        if speed < 0:
            print("The cart is not moving.")
            raise ValueError
        else:
            self.__speed = speed

    def set_speed(self):
        return self.__speed
    def get_position(self):
        return self.__position

    def __str__(self):
        return(f"The cart: color - {self.color}, Speed - {self.__speed}, Position - {self.__position}, Seats - {self.seats}")
    
    def __init__(self):
        return(self.__position)
    
    def main():
        red_cart = RollerCoaster()

    if __name__ == "__main__":
        main()


