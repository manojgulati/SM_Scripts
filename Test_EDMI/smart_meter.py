
from utils import find_tty_usb, convert_to_str
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
# import pymodbus.payload
# from pymodbus.payload import BinaryPayloadDecoder
# from pymodbus.constants import Endian

#from pymodbus.constants import Endian
#from pymodbus.payload import BinaryPayloadDecoder
#from pymodbus.payload import BinaryPayloadBuilder

import time
from datetime import datetime
import logging


class SmartMeter(object):

    """
    1. Sets up a smart meter connection
    2. Specifies a serial port to connect to
    3. Methods to read and write data (to csv)
    """

    def __init__(self, retries=2, com_method='rtu',
                 baudrate=9600, stopbits=1, parity='N',
                 bytesize=8, timeout=0.1, logfile='sm.log'):
        """Sets up parameters for modbus connection to the smart meter

        Parameters
        ----------
        retries :  int, default=2
             The number of times a packet read request must be made
        com_method : string, default='rtu'
            Mode of connection
        baudrate : int, default=19200
            Baudrate set on the smart meter, eg. 9600, 19200
        stopbits : int, default=1
            Number of stopbits set on the smart meter, eg. 1
        parity : string, default='N'
            Parity set on the smart meter, eg. 'N':None, 'E':Even
        bytesize : int, default=8
            Size of packet, eg. 8
        timeout : float, default=0.1
            Number of seconds before a request times out, eg. 0.1
        logfile: string, eg. '/home/pi/abc.log'
            File to store the log
        """
        self.retries = retries
        self.com_method = com_method
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.parity = parity
        self.bytesize = bytesize
        self.timeout = timeout
        self.logger = logging.getLogger('smart_meter')
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler(logfile)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

    def connect(self, vendor="", product="", meter_port=None):
        """Connects to a specific port (if specified).
        Else, if the device details
        of USB-Modbus device are given, finds the port
        on which they are attached.
        This may be needed as the serial port on RPi
        was observed to.

        Parameters
        ----------
        vendor: string
        product: string

        Returns
        --------
        client : ModbusSerialClient
        """
        if meter_port is None:
            self.vendor = vendor
            self.product = product
            self.meter_port = find_tty_usb(vendor, product)
            # print vendor
            # print product
        else:
            self.meter_port = meter_port
        self.logger.info('Connecting to port: %s' % self.meter_port)

        self.client = ModbusClient(
            retries=self.retries, method=self.com_method,
            baudrate=self.baudrate, stopbits=self.stopbits, parity=self.parity,
            bytesize=self.bytesize, timeout=self.timeout, port=self.meter_port)
        self.logger.info('Connected to port: %s' % self.meter_port)
        return self.client

    def read_from_meter(self, meter_id, base_register, block_size,
                        params_indices):
        """Reads data from meter correpsonding to the param indices
        specified

        Parameters
        -----------

        meter_id : ID set on the meter (eg. 1, 2), int
        base_register : Base register for block of registers to read, int
        block_size : Number of register bytes in this block, int
        params_indices : List of indices relative to base_register, list

        Returns
        -------
        data: Comma separated values correpsonding to parameters whose indices
        were specified
        """
        try:
            time.sleep(0.5)
            #self.client=self.connect(vendor=self.vendor, product=self.product)
            binary_data = self.client.read_holding_registers(
                base_register, block_size, unit=meter_id)
            #print(self.client)
            # print("Try1")
            if(binary_data.isError()==True):
                self.client.close()
                self.client=self.connect(vendor=self.vendor, product=self.product)
                print("1st reconnect in try")
	    # print binary_data.registers

        except Exception as e:
            # Sleep for some time and again try to connect
            time.sleep(0.5)
            self.logger.exception(e)
            self.logger.info('Will now try to reconnect')
            binary_data = self.client.read_holding_registers(
                base_register, block_size, unit=meter_id)
            while(binary_data.isError()==True):
                self.client.close()
                self.client = self.connect(vendor=self.vendor, product=self.product)
                binary_data = self.client.read_holding_registers(base_register, block_size, unit=meter_id)
                print("2nd time connect in except")

            # print("Try2")
            # print(binary_data.isError())
            # print binary_data.registers

        # print len(binary_data.rep2int binary_data.isError()3isters)
        # print base_register, block_size, meter_id
        # print type(binary_data.registers)
        #A1 = [binary_data.registers[0], binary_data.registers[1]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[2], binary_data.registers[3]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[4], binary_data.registers[5]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[6], binary_data.registers[7]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[36], binary_data.registers[37]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[42], binary_data.registers[43]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_float()
        #print A

        #A1 = [binary_data.registers[46], binary_data.registers[47]]
        #decoder = BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
        #A = decoder.decode_32bit_int()
        #print A
        #if(self.client==False):

        while(binary_data.isError()==True):
            self.client.close()
            self.client = self.connect(vendor=self.vendor, product=self.product)
            binary_data = self.client.read_holding_registers(base_register, block_size, unit=meter_id)
            print("3rd time connect before storing in the file")
        data=""
        k=1
        for i in range(0,block_size-1,2):
            #A1=[binary_data.registers[i], binary_data.registers[i+1]]
            #decoder=BinaryPayloadDecoder.fromRegisters(A1, byteorder=Endian.Big, wordorder=Endian.Big)
            if k!=1:
                data=data+","+ convert_to_str((binary_data.registers[i] << 16) + binary_data.registers[i+1])
            else:
                data=convert_to_str((binary_data.registers[i] << 16) + binary_data.registers[i+1])
                k=k+1
        data=str(time.time())+","+data+"\n"
        print(data)


        # decoder = BinaryPayloadDecoder.fromRegisters(binary_data.registers[3], byteorder=Endian.Big, wordorder=Endian.Big)
        #
        # A = decoder.decode_32bit_float()
        #
        # print A



        #data = ""
        # for i in range(0, (block_size - 1), 2):
        #     for j in params_indices:
        #         if(j == i):
        #             data = data + "," + convert_to_str(
        #                 (binary_data.registers[i + 1] << 16) + binary_data.registers[i])
        #
        # data = data[:-1] + "\n"
        #data = str(time.time()) + data
        return data

    def write_csv(self, csv_path, data):
        """Writes a comma separted row of data into the csv

        Parameters
        ----------
        csv_path : Complete path of the CSV file
        data : string representation of row to write
        """
        with open(csv_path, 'a') as f:
            f.write(data)
