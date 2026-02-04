from src.simulator.signals import SignalGenerator

def test_signals_within_range():
    gen = SignalGenerator()
    for _ in range(200):
        s = gen.step()
        assert 0.0 <= s.speed_kmh <= 200.0
        assert 20.0 <= s.temp_c <= 120.0
        assert 0.0 <= s.torque_nm <= 400.0
