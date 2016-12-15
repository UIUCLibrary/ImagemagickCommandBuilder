import configparser
import shutil


def get_configure():
    config = configparser.ConfigParser()
    config.read("settings/imdsettings.ini")
    return config

try:
    IMAGEMAGICK = get_configure()['commands'].get('convert', shutil.which("convert"))
except KeyError:
    IMAGEMAGICK = shutil.which("convert")
from .director import Director
