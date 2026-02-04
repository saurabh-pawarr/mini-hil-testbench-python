import time
from simulator.signals import SignalGenerator
from simulator.can_sim import CANBusSim
from simulator.ecu_model import ECUModel
from simulator.logger import CSVLogger

def main():
    gen = SignalGenerator()
    bus = CANBusSim(period_ms=100)
    ecu = ECUModel(timeout_s=0.3)

    logger = CSVLogger("data/run_log.csv")

    start = time.time()
    duration_s = 20  # keep short (change later if you want)

    while (time.time() - start) < duration_s:
        t = time.time() - start

        # Fault injections:
        # After 6 seconds: force overtemp
        if t > 6:
            gen.spike_temp = True

        # After 12 seconds: drop CAN messages for a while (simulate timeout)
        if 12 < t < 13:
            bus.drop_messages = True
        else:
            bus.drop_messages = False

        sig = gen.step()
        frame = bus.publish({
            "speed_kmh": sig.speed_kmh,
            "temp_c": sig.temp_c,
            "torque_nm": sig.torque_nm
        })

        status = ecu.update(frame)

        logger.log(time.time(), {
            "speed_kmh": sig.speed_kmh,
            "temp_c": sig.temp_c,
            "torque_nm": sig.torque_nm
        }, status)

        print(sig, status)

    logger.close()
    print("Done. Log saved to data/run_log.csv")

if __name__ == "__main__":
    main()
