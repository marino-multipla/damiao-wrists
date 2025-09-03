import time
import math
from dm import SerialPort,Motor_Control, MIT_MODE, DM4310, Motor
import termios

def main():
    serial = SerialPort("/dev/ttyACM0", termios.B921600)
    dm = Motor_Control(serial)
    #MIT_MODE= Control_Mode.MIT_MODE
    #DM4310=DM_Motor_Type.DM4310
    M1 = Motor(DM4310, 0x01, 0x11)
    M2 = Motor(DM4310, 0x02, 0x11)

    dm.addMotor(M1)
    dm.addMotor(M2)

    dm.enable(M1)
    dm.enable(M2)

    dm.switchControlMode(M1, MIT_MODE)
    dm.switchControlMode(M2, MIT_MODE)

    dm.save_motor_param(M1)
    dm.save_motor_param(M2)

    # dm.zero_position(M1)
    # dm.zero_position(M2)

    time.sleep(2)

    while True:
        # Simula un movimento sinusoidale
        q = math.sin(time.time())  # tempo in secondi

        # Controllo in modalità MIT
        # control(motore, kp, kd, posizione, velocità, coppia)
        dm.control(M2, 30, 0.3, math.pi / 4, 0, 0)
        time.sleep(1)
        dm.control(M2, 30, 0.3, 0, 0, 0)
        time.sleep(1)
        dm.control(M1, 30, 0.3, math.pi / 4, 0, 0)
        time.sleep(1)
        dm.control(M1, 30, 0.3, 0, 0, 0)
        time.sleep(1)

        # Stampa lo stato del motore
        print(f"m1: pos={M1.Get_Position()} vel={M1.Get_Velocity()} tau={M1.Get_tau()}")

        # Se vuoi provare modalità alternative:
        # dm.control_pos_vel(M1, q*10, 5)
        # dm.control_vel(M1, q*10)
        # dm.control_pos_vel(M2, q*10, 5)

if __name__ == "__main__":
    main()
