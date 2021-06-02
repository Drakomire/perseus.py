import os
import json
import math
from .__init__ import *

class Retrofit:
    def __init__(self):
        pass

    @staticmethod
    def getRetrofitStats(ship):
        out = {}
        for node in ship["retrofit"]:
            for r in retrofit[str(node)]["effect"]:
                for key in r:
                    if (key in STAT_KEYWORDS):
                        if (STAT_KEYWORDS[key] in out):
                            out[STAT_KEYWORDS[key]] += r[key]
                        else:
                            out[STAT_KEYWORDS[key]] = r[key]
        return out

    @staticmethod
    def getRetrofitShipID(ship):
        """
        :param ship: The ship Object
        :return: the ships retrofit ID if it has one. Otherwise returns the original ID.
        """
        for i in ship.ship["retrofit"]:
            shipId = retrofit[str(i)]["ship_id"]
            if (len(shipId)>0):
                return str(math.floor(shipId[0][1]/10))
        return ship.id