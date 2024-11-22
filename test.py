import max30102
import hrcalc

m = max30102.MAX30102()

# 100 samples are read and used for HR calculation in a single loop
while True:
    ir = m.read_sequential()

    # Calculate HR, IPM, HRSTD, and RMSSD
    hr, hr_valid, ipm, hrstd, rmssd = hrcalc.calc_hr_metrics(ir)
    print(f"Heart Rate: {hr} bpm (Valid: {hr_valid})")
    print(f"Impulse Per Minute: {ipm}")
    print(f"Heart Rate Standard Deviation (HRSTD): {hrstd:.2f} bpm")
    print(f"Root Mean Square of Successive Differences (RMSSD): {rmssd:.2f} bpm")
    print("")