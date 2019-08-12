import time

# Importing our modules
from settings import Constants
from sensor_graph import SensorGraph
from temperature_sensor import TemperatureSensor

# Entry Point
def main():
    # Temperature Sensor Object (Deals with API and provides graphable data (x, y) values)
    temp_sensor = TemperatureSensor(Constants.group_id, Constants.temp_widget_id)

    # Sensor Graph Object (Takes in the sensor object, reads sensor data periodically, and plots it)
    interval = 3 * 60  # Seconds 
    graph_points = 10  # At an instance, this many latest data points will be plotted
    sensor_graph = SensorGraph(interval, graph_points, temp_sensor)

    # Starts the plotting process (Shows the graph and gets updates for sensor in a while loop)
    sensor_graph.start_plotting()

# If the file is being executed as main file (i.e: not being used as a module)
if __name__ == "__main__":
    main()