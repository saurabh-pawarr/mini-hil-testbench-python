import random
from dataclasses import dataclass

@dataclass
class Signals:
    speed_kmh: float
    temp_c: float
    torque_nm: float

class SignalGenerator:
    """
    Generates simple vehicle-like signals with optional faults.
    Beginner-friendly, no external tools.
    """

    def __init__(self):
        self._speed = 0.0
        self._temp = 25.0
        self._torque = 0.0

        self.freeze_speed = False
        self.spike_temp = False

    def step(self) -> Signals:
        # SPEED
        if not self.freeze_speed:
            self._speed += random.uniform(-2, 5)
            self._speed = max(0.0, min(200.0, self._speed))

        # TEMP
        self._temp += random.uniform(-0.2, 0.5)
        self._temp = max(20.0, min(120.0, self._temp))

        # TORQUE
        self._torque += random.uniform(-10, 15)
        self._torque = max(0.0, min(400.0, self._torque))

        # Fault injection: temp spike
        temp = self._temp
        if self.spike_temp:
            temp = 115.0  # force overtemp

        return Signals(
            speed_kmh=round(self._speed, 2),
            temp_c=round(temp, 2),
            torque_nm=round(self._torque, 2),
        )
