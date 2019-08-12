import matplotlib.pyplot as plt

class SensorGraph():

    # interval: Plotting Interval in seconds
    # length: How many points to show at a moment
    def __init__(self, interval, length, sensor):
        self.interval = interval
        self.length   = length
        self.sensor   = sensor

    def start_plotting(self):
        while True:
            # Fetches latest data from the sensor
            x, y = self.sensor.get_graphing_data(self.length)

            # Plots the data on the device
            plt.plot(x, y)
            plt.pause(self.interval)
            plt.clf()