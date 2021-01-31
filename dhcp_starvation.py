from scapy.all import *
from time import sleep
from threading import Thread

class DHCPStarvation:
    def __init__(self):
    self.mac = [""]
    self.ip = []
