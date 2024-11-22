import max30102
import hrcalc

m = max30102.MAX30102()

# 100 samples are read and used for HR calculation in a single loop
while True:
    ir = m.read_sequential()
    # # print(ir)
    # print(hrcalc.calc_hr(ir))

    # Calculate heart rate and IPM
    hr, hr_valid, ipm = hrcalc.calc_hr_and_ipm(ir)
    print(f"Heart Rate: {hr} bpm (Valid: {hr_valid}), Impulse Per Minute: {ipm}")