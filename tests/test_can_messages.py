from src.simulator.can_sim import CANBusSim

def test_can_frame_created():
    bus = CANBusSim(period_ms=1)  # fast for test
    frame = bus.publish({"speed_kmh": 10, "temp_c": 30, "torque_nm": 50})
    assert frame is not None
    assert frame.can_id == 0x101
    assert "speed_kmh" in frame.signals
