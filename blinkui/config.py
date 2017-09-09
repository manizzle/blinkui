import configparser

DATABASE = 'blinkui.db'
DEBUG = True

conf = configparser.ConfigParser()
conf.read('blinkui.conf')

BLINK_USERNAME = conf.get('blink', 'username')
BLINK_PASSWORD = conf.get('blink', 'password')