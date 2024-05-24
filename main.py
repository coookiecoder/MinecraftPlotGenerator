from time import sleep
from keyboard import write as write_keyboard
from keyboard import press as press_keyboard

class MinecraftPlot:
    def __init__(self, width, height, material="minecraft:gray_concrete", separation=False):
        self.__width = width
        self.__height = height
        self.__material = material
        self.__separation = separation
        return

    def __del__(self):
        return

    def generate_command_plot(self, x=0, y=0):
        if self.__separation:
            command = "/fill "
            command += str(self.__width * x + 1 + x * int(x != 0)) + " -61 "
            command += str(self.__height * y + 1 + y * int(y != 0)) + " "
            command += str(self.__width * (x + 1) + x * int(x != 0)) + " -61 "
            command += str(self.__height * (y + 1) + y * int(y != 0)) + " "
            command += self.__material
            return command
        else:
            command = "/fill "
            command += str(self.__width * x) + " -61 "
            command += str(self.__height * y) + " "
            command += str(self.__width * (x + 1) - 1) + " -61 "
            command += str(self.__height * (y + 1) - 1) + " "
            command += self.__material
            return command

    def generate_cluster_command(self, x=1, y=1, write=True):
        sleep(5)
        for x_iteration in range(0, x):
            for y_iteration in range(0, y):
                command = self.generate_command_plot(x_iteration, y_iteration)
                if write:
                    press_keyboard("t")
                    sleep(0.1)
                    write_keyboard(command)
                    sleep(0.1)
                    press_keyboard("enter")
                else:
                    print(command)
                sleep(0.1)
        return


def get_data():
    width = int(input("Width: "))
    height = int(input("Height: "))
    material = str(input("Material: "))
    separation = str(input("Separation: "))
    return MinecraftPlot(width, height, material, separation == "y" or separation == "yes")


if __name__ == '__main__':
    data = get_data()
    data.generate_cluster_command(int(input("number of plot on x axis: ")), int(input("number of plot on y axis: ")))
