# Path where the data gets stored
DATA_PATH = "/home/pi/SM_Scripts/Test_EDMI/Sample_Files/"
LOG_PATH = "/home/pi/SM_Scripts/Test_EDMI/Sample_Files/sm.log"

#DATA_PATH = "/home/manoj/Documents/EDMI_Data/Sample_Files/"
#LOG_PATH = "/home/manoj/Documents/EDMI_Data/Sample_Files/sm.log"


# Parameters associated with USB-Modbus device

_EDMI = {
    'meter_id': 47,
    'stopbits': 1,
    'bytesize': 8,
    'parity': 'N',
    'baudrate': 9600,

    # Parameters for communication
    'com_method': 'rtu',
    'timeout': 0.2,
    'base_register': 9001,
    'block_size': 88,
    'retries': 3,

    # All parameters provided (in order from base register)
    # 'params_provided': "VA,W,VAR,PF,VLL,VLN,A,F,VA1,W1,VAR1,PF1,V12,V1,A1,VA2,W2,VAR2,PF2,V23,V2,A2,VA3,W3,VAR3,PF3,V31,V3,A3,FwdVAh,FwdWh,FwdVARh",

    'params_provided': "V1,V2,V3,A1,A2,A3,PA1,PA2,PA3,W1,W2,W3,VAR1,VAR2,VAR3,VA1,VA2,VA3,F,A12,A13,PF,Date,Time,DWh,DVARh,RWh,RVARh,TW,TVAR,TVA,TA,V12,V23,V31,THD1,THD2,THD3,THDA1,THDA2,THDA3,PF1,PF2,PF3",

    # Timestamp,VA,W,VAR,PF,VLL,VLN,A,F,VA1,W1,VAR1,PF1,V12,V1,A1,VA2,W2,VAR2,PF2,V23,V2,A2,VA3,W3,VAR3,PF3,V31,V3,A3,FwdVAh,FwdWh,FwdVARh(inductive),FwdVARh(capacitive)\n"

    # Set of parameters we wish to record (in order)
    # 'params_to_record': "VA,W,VAR,PF,VLN,A,F,A1,VA1,W1,VAR1,A2,VA2,W2,VAR2,FwdVAh,FwdWh,FwdVARh",

    'params_to_record': "V1,V2,V3",

    'vendor': '0403',
    'product': '6001'
}
