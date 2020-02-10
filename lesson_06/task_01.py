from time import sleep, time
from typing import Iterator


class TrafficLight:
    __color = None

    class ColorOrderError(Exception):
        ...

    def running(self) -> Iterator[str]:
        color_order = (
            ('red', 7),
            ('yellow', 9),
            ('green', 10),
        )

        previous_color = self.__color
        time_start = time()

        while time() - time_start < color_order[-1][1]:
            if self.__color != previous_color:
                self.__color = None
                raise self.ColorOrderError

            time_delta = time() - time_start

            for color, time_ in color_order:
                if time_ < time_delta:
                    continue

                self.__color = previous_color = color

                yield self.__color
                break

        self.__color = None
        return self.__color


traffic_light = TrafficLight()

for status in traffic_light.running():
    print(status)
    sleep(1)
else:
    print('Stop')

