import time
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class CANFrame:
    can_id: int
    timestamp: float
    signals: Dict[str, Any]

class CANBusSim:
    """
    Very simple CAN-like bus simulator.
    Generates CANFrame objects at a fixed interval.
    """

    def __init__(self, can_id: int = 0x101, period_ms: int = 100):
        self.can_id = can_id
        self.period_ms = period_ms
        self.drop_messages = False  # fault: drop messages (simulate timeout)

    def publish(self, signals: Dict[str, Any]) -> Optional[CANFrame]:
        time.sleep(self.period_ms / 1000.0)

        if self.drop_messages:
            return None

        return CANFrame(
            can_id=self.can_id,
            timestamp=time.time(),
            signals=signals
        )
