"""Example Load Platform integration."""
import logging

FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

DOMAIN = 'example_load_platform'


def setup(hass, config):
    """Your controller/hub specific code."""
    # Data that you want to share with your platforms
    hass.data[DOMAIN] = {
        'temperature': 90
    }
    logging.info(f"hass data value is:           {hass.data}")
    logging.info(f"inside setup of exampleload platform.................................................................*************************************")
    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True
