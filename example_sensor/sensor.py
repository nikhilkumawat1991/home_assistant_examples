"""Platform for sensor integration."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import time
from homeassistant.core import callback
import logging

DOMAIN = "example_sensor"
count = 0

FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    logging.debug("config details are: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    for key, value in config.items():
        print(key, value)
    logging.debug(hass.__dict__["states"].__dict__)

    # Fire event example_component_my_cool_event with event data answer=42
    hass.bus.fire("example_component_my_cool_event", {"answer": 42})

    add_entities([ExampleSensor()])


class ExampleSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Example Temperature nikhil'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        self._state = 23
