from time import sleep


class TrafficLight:

    __color = ['red', 'yellow', 'green']

    def running(self):
        sec = 0
        while sec != 3:
            print(TrafficLight.__color[sec])
            if sec == 0:
                sleep(7)
            elif sec == 1:
                sleep(2)
            elif sec == 2:
                sleep(10)
            sec += 1


time_color = TrafficLight()
time_color.running()