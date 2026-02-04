import csv
from pathlib import Path
from typing import Dict, Any
from .ecu_model import ECUStatus

class CSVLogger:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

        self._file = open(self.filepath, "w", newline="", encoding="utf-8")
        self._writer = csv.DictWriter(self._file, fieldnames=[
            "timestamp",
            "speed_kmh",
            "temp_c",
            "torque_nm",
            "overspeed_flag",
            "overtemp_flag",
            "comm_timeout"
        ])
        self._writer.writeheader()

    def log(self, timestamp: float, signals: Dict[str, Any], status: ECUStatus):
        self._writer.writerow({
            "timestamp": timestamp,
            "speed_kmh": signals["speed_kmh"],
            "temp_c": signals["temp_c"],
            "torque_nm": signals["torque_nm"],
            "overspeed_flag": status.overspeed_flag,
            "overtemp_flag": status.overtemp_flag,
            "comm_timeout": status.comm_timeout
        })

    def close(self):
        self._file.close()
