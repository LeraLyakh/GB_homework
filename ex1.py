from time import sleep
class TrafficLight:

    __color = ('красный', 'желтый', 'зеленый')

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(7)
            print(self.__color[1])
            sleep(2)

tl = TrafficLight()
tl.running()
