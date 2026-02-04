import time
from src.simulator.ecu_model import ECUModel
from src.simulator.can_sim import CANFrame

def test_overspeed_flag():
    ecu = ECUModel(timeout_s=0.3)
    frame = CANFrame(can_id=0x101, timestamp=time.time(),
                     signals={"speed_kmh": 170, "temp_c": 50, "torque_nm": 20})
    status = ecu.update(frame)
    assert status.overspeed_flag is True

def test_overtemp_flag():
    ecu = ECUModel(timeout_s=0.3)
    frame = CANFrame(can_id=0x101, timestamp=time.time(),
                     signals={"speed_kmh": 50, "temp_c": 110, "torque_nm": 20})
    status = ecu.update(frame)
    assert status.overtemp_flag is True

def test_comm_timeout():
    ecu = ECUModel(timeout_s=0.1)
    frame = CANFrame(can_id=0x101, timestamp=time.time(),
                     signals={"speed_kmh": 0, "temp_c": 0, "torque_nm": 0})
    ecu.update(frame)

    time.sleep(0.2)
    status = ecu.update(None)
    assert status.comm_timeout is True
