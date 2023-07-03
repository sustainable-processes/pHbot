"""
Class object to control the Ender platform for cartesian movements of the pH robot.

Author: Leong Chang Jie
Date: June 2022
"""
import time
import numpy as np
import serial
import serial.tools.list_ports
from debugger import Debugger
debug = Debugger(show_logs=True)

# %% Serial / CNC
def display_ports():
    """
    Displays available ports.
    """
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
    if len(ports) == 0:
        print("No ports detected!")
        print("Simulating platform...")
    return


class CNC(object):
    """
    Controller for cnc xyz-movements.
    - address: serial address of cnc Arduino
    """
    def __init__(self, address):
        self.address = address
        # self.cnc = self.connect_cnc(address)
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0
        self.space_range = [(0,0,0), (0,0,0)]
        self.Z_safe = np.nan
        return

    def connect_cnc(self, address):
        """
        Establish serial connection to cnc controller.
        - address: port address

        Return: serial.Serial object
        """
        cnc = None
        try:
            cnc = serial.Serial(address, 115200, timeout=1) 
            cnc.close()
            cnc.open()

            # Start grbl 
            cnc.write(bytes("\r\n\r\n", 'utf-8'))
            time.sleep(2)
            cnc.flushInput()

            # Homing cycle
            cnc.write(bytes("$H\n", 'utf-8'))
            #print(cnc.readline())
            print("CNC ready")
        except:
            pass
        return cnc
    
    def to_position(self, coord, z_to_safe=True, print_statement= False):
        """
        Move cnc to absolute position in 3D
        - coord: (X, Y, Z) coordinates of target
        """

        if z_to_safe and self.current_z < self.Z_safe:
            try:
                self.cnc.write(bytes("G90\n", 'utf-8'))
                #print(self.cnc.readline())
                self.cnc.write(bytes(f"G0 Z{self.Z_safe}\n", 'utf-8'))
                #print(self.cnc.readline())
                self.cnc.write(bytes("G90\n", 'utf-8'))
                #print(self.cnc.readline())
            except:
                pass
            self.current_z = self.Z_safe
            if print_statement == True:
                print(f'{self.current_x}, {self.current_y}, {self.current_z}')

        x, y, z = coord
        z_first = True if self.current_z < z else False
        l_bound, u_bound = np.array(self.space_range)
        next_x = x
        next_y = y
        next_z = z
        next_pos = np.array([next_x, next_y, next_z])

        if all(np.greater_equal(next_pos, l_bound)) and all(np.less_equal(next_pos, u_bound)):
            pass
        else:
            print(f"Range limits reached! {self.space_range}")
            return

        positionXY = f'X{x}Y{y}'
        position_Z = f'Z{z}'
        moves = [position_Z, positionXY] if z_first else [positionXY, position_Z]
        try:
            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())
            for move in moves:
                self.cnc.write(bytes(f"G1 {move} F20000\n", 'utf-8'))
                #print(self.cnc.readline())
            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())
        except:
            pass

        self.current_x = next_x
        self.current_y = next_y
        self.current_z = next_z
        #print(f'{self.current_x}, {self.current_y}, {self.current_z}')
        return


class Ender(CNC):
    """
    XYZ controls for Ender platform.
    - address: serial address of cnc Arduino
    - space_range: range of motion of tool
    """
    def __init__(self, address, space_range=[(0,0,0), (220,220,250)], Z_safe=90):
        super().__init__(address)
        self.cnc = self.connect_cnc(address)
        self.space_range = space_range
        self.Z_safe = Z_safe
        self.home()
        return
    
    def connect_cnc(self, address):
        """
        Establish serial connection to cnc controller.
        - address: port address

        Return: serial.Serial object
        """
        cnc = None
        try:
            cnc = serial.Serial(address, 115200)
        except:
            pass
        return cnc

    def home(self):
        """
        Homing cycle for Ender platform
        """
        try:
            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())
            self.cnc.write(bytes("G0 " + f"Z{self.Z_safe}" + "\n", 'utf-8'))
            #print(self.cnc.readline())
            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())

            self.cnc.write(bytes("G28\n", 'utf-8'))

            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())
            self.cnc.write(bytes("G0 " + f"Z{self.Z_safe}" + "\n", 'utf-8'))
            #print(self.cnc.readline())
            self.cnc.write(bytes("G90\n", 'utf-8'))
            #print(self.cnc.readline())
        except:
            pass
        self.current_x = 0
        self.current_y = 0
        self.current_z = self.Z_safe
        print(f'{self.current_x}, {self.current_y}, {self.current_z}')
        try:
            self.cnc.write(bytes("G1 F5000\n", 'utf-8'))
            #print(self.cnc.readline())
        except:
            pass
        return