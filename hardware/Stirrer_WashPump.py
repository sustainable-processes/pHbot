"""
Class object to control the speed of the pH robot stirrer and suction strength of the wash pump

Author: Sarfaraz Ahamed, Aniket Chitre
Date: July 2022
"""
import serial
import time

class pH_stirrer_WashPump:

    baud_rate = 9600    # Communication rates for the arduino

    def __init__(self, port):

        self.port = port    # Edit port according to listed port in 'Device Manager'
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=1)  # Open serial object and not elsewhere

    def stir_pump(self, stirrer_speed, inlet_pump, outlet_pump, print_statement=False):

        stir_Washpump_str = str(stirrer_speed) + ';' + str(inlet_pump) + ';' + str(outlet_pump) + ';0' + '/n'    # String to send the arduino - Includes speed + separator + suction strength + end character
        self.ser.write(stir_Washpump_str.encode('utf-8'))    # Convert the string to bytes and sends the encoded string to arduino
        if print_statement != False:
            print('Stirring at ' + str(stirrer_speed) + ' speed and wash station inlet and outlet pumps at ' + str(inlet_pump) + ' & ' + str(outlet_pump) + ' speeds, respectively.')