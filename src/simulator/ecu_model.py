import time
from dataclasses import dataclass
from typing import Optional
from .can_sim import CANFrame

@dataclass
class ECUStatus:
    overspeed_flag: bool
    overtemp_flag: bool
    comm_timeout: bool

class ECUModel:
    """
    Defines simple 'requirements' we will test:
    - speed > 160 => overspeed_flag True
    - temp  > 105 => overtemp_flag True
    - no message for > 0.3s => comm_timeout True
    """

    def __init__(self, timeout_s: float = 0.3):
        self.timeout_s = timeout_s
        self._last_rx_time: Optional[float] = None

    def update(self, frame: Optional[CANFrame]) -> ECUStatus:
        now = time.time()

        if frame is not None:
            self._last_rx_time = now
            speed = frame.signals["speed_kmh"]
            temp = frame.signals["temp_c"]
        else:
            speed = 0.0
            temp = 0.0

        comm_timeout = False
        if self._last_rx_time is None:
            comm_timeout = True
        else:
            if (now - self._last_rx_time) > self.timeout_s:
                comm_timeout = True

        overspeed = speed > 160.0
        overtemp = temp > 105.0

        return ECUStatus(
            overspeed_flag=overspeed,
            overtemp_flag=overtemp,
            comm_timeout=comm_timeout
        )
