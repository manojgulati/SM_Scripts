# Path where the data gets stored
DATA_PATH = "/Users/manojgulati/Documents/Test_SM_6436/"
LOG_PATH = "/Users/manojgulati/Documents/Test_SM_6436/sm.log"

# Parameters associated with USB-Modbus device

_6436 = {
    'meter_id': 1,
    'stopbits': 1,
    'bytesize': 8,
    'parity': 'N',
    'baudrate': 9600,

    # Parameters for communication
    'com_method': 'rtu',
    'timeout': 0.2,
    'base_register': 3900,
    'block_size': 66,
    'retries': 2,

    # All parameters provided (in order from base register)
    'params_provided': "VA,W,VAR,PF,VLL,VLN,A,F,VA1,W1,VAR1,PF1,V12,V1,A1,VA2,W2,VAR2,PF2,V23,V2,A2,VA3,W3,VAR3,PF3,V31,V3,A3,FwdVAh,FwdWh,FwdVARh",

    # Set of parameters we wish to record (in order)
    'params_to_record': "VA,W,VAR,PF,VLN,A,F,A1,VA1,W1,VAR1,A2,VA2,W2,VAR2,FwdVAh,FwdWh,FwdVARh",

#    'vendor': '0403',
#    'product': '6001'
    'vendor': '1027',
    'product': '24577'
}
