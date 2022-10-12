import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ
RK = 0.11925
RW = 0.04778
ALPHA = np.deg2rad(45)

def compute_motor_torques(Tx, Ty, alpha):
    '''
    Parameters:
    ----------
    Tx: Torque along x-axis
    Ty: Torque along y-axis
    alpha: Motor inclination angle

    Returns:
    --------
            Ty
            T1
            |
            |
            |
            . _ _ _ _ Tx
           / \
          /   \
         /     \
        /       \
       T2       T3

    T1: Motor Torque 1
    T2: Motor Torque 2
    T3: Motor Torque 3

    '''
    T1 = 1.0/3 * (-2.0*Ty/(np.cos(alpha)))
    T2 = 1.0/3 * (1/np.cos(alpha) * (-np.sqrt(3)*Tx +Ty))
    T3 = 1.0/3 * (1/np.cos(alpha) * (np.sqrt(3)*Tx +Ty))

    return T1, T2, T3

if __name__ == "__main__":
    start = time.time()
    t = 0.0

    T1_array = []
    T2_array = []
    T3_array = []

    while(t < EXEC_TIME):
        # Runs @200Hz
        t += (1.0/200)

        Tx = 3.0 * np.sin(t)
        Ty = 2.0 * np.cos(t)

        # Compute Motor Torques
        T1, T2, T3 = compute_motor_torques(Tx, Ty, ALPHA)

        # Append your computed motor torques to their corresponding arrays
        T1_array.append(T1)
        T2_array.append(T2)
        T3_array.append(T3)

        time.sleep(1.0/200)
    
    # Save your arrays as a .csv file
np.savetxt('1_torques.csv',T1_array,delimiter=",")
np.savetxt('2_torques.csv',T2_array,delimiter=",")
np.savetxt('3_torques.csv',T3_array,delimiter=",")