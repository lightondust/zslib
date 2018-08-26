import usb.core
import usb.util
import sys
import time
from zslib.data.CONST import LIB_PATH

sys.path = LIB_PATH + sys.path

from usb_4_mic_array.tuning import Tuning

EXE_TIME = 100

class Respeaker:

    def __init__(self):
        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.mic_tuning = Tuning(self.dev)

    def doa(self, exe_time=EXE_TIME):
        """
        :param time: excecution time
        :return:
        """
        for t in range(exe_time):
            sys.stdout.write(str(self.mic_tuning.direction) + ',')
            time.sleep(1)

    def vad(self, exe_time=EXE_TIME):
        """
        :param exe_time:
        :return:
        """
        print(self.mic_tuning.is_voice())
        for t in range(exe_time):
            sys.stdout.write(str(self.mic_tuning.is_voice()) + ',')
            time.sleep(1)
