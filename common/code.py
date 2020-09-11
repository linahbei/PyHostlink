from .type import UnitType
from .type import DirectionType
from .type import ProtocolType
from .type import HeaderCodeType
from .type import EndCodeType
from .type import FinsCommandCodeType
from .type import FinsEndCodeType
from .type import FinsUnitConnectionType


class CmodeCode():
    @property
    def extension_header_codes(self):
        return self._extension_header_codes
        
    @property
    def header_codes(self):
        return self._header_codes
        
    @property
    def end_codes(self):
        return self._end_codes
        
    def __init__(self):
        self._extension_header_codes = {
            b'QQMR': {'name': 'REGISTER I/O MEMORY', 'type': HeaderCodeType.IO_MEMORY_AREA_REG_AND_READING},
            b'QQIR': {'name': 'READ I/O MEMORY', 'type': HeaderCodeType.IO_MEMORY_AREA_REG_AND_READING},
            b'FA': {'name': 'FINS MESSAGE', 'type': HeaderCodeType.FINS_OVER_HOSTLINK},
            b'CF': {'name': 'FINS MESSAGE', 'type': HeaderCodeType.FINS_OVER_HOSTLINK},
        }
    
        self._header_codes = {
            #EXTENSION_4BYTES_HEADER_CODE
            b'QQ': {'name': 'Extension 4 bytes header code', 'type': HeaderCodeType.EXTENSION_4BYTES_HEADER_CODE},
            b'FA': {'name': 'Extension header code', 'type': HeaderCodeType.EXTENSION_HEADER_CODE},
            b'CF': {'name': 'Extension header code', 'type': HeaderCodeType.EXTENSION_HEADER_CODE},

            #IO_MEMORY_READING
            b'RR': {'name': 'CIO AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RL': {'name': 'LR AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RH': {'name': 'HR AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RC': {'name': 'TIMER/COUNTER PV READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RG': {'name': 'TIMER/COUNTER STATUS READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RD': {'name': 'DM AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RJ': {'name': 'AR AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            b'RE': {'name': 'EM AREA READ', 'type': HeaderCodeType.IO_MEMORY_READING},
            
            #IO_MEMORY_WRITING
            b'WR': {'name': 'CIO AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WL': {'name': 'LR AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WH': {'name': 'HR AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WC': {'name': 'TIMER/COUNTER PV WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WD': {'name': 'DM AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WJ': {'name': 'AR AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},
            b'WE': {'name': 'EM AREA WRITE', 'type': HeaderCodeType.IO_MEMORY_WRITING},

            #TIMER_COUNTER_SV_READING
            b'R#': {'name': 'TIMER/COUNTER SV READ 1', 'type': HeaderCodeType.TIMER_COUNTER_SV_READING},
            b'R$': {'name': 'TIMER/COUNTER SV READ 2', 'type': HeaderCodeType.TIMER_COUNTER_SV_READING},
            b'R%': {'name': 'TIMER/COUNTER SV READ 3', 'type': HeaderCodeType.TIMER_COUNTER_SV_READING},
            
            #TIMER_COUNTER_SV_CHANGING
            b'W#': {'name': 'TIMER/COUNTER SV CHANGE 1', 'type': HeaderCodeType.TIMER_COUNTER_SV_CHANGING},
            b'W$': {'name': 'TIMER/COUNTER SV CHANGE 2', 'type': HeaderCodeType.TIMER_COUNTER_SV_CHANGING},
            b'W%': {'name': 'TIMER/COUNTER SV CHANGE 3', 'type': HeaderCodeType.TIMER_COUNTER_SV_CHANGING},
            
            #CPU_UNIT_STATUS
            b'MS': {'name': 'STATUS READ', 'type': HeaderCodeType.CPU_UNIT_STATUS},
            b'SC': {'name': 'STATUS CHANGE', 'type': HeaderCodeType.CPU_UNIT_STATUS},
            b'MF': {'name': 'ERROR READ', 'type': HeaderCodeType.CPU_UNIT_STATUS},
            
            #FORCED_SET_RESET
            b'KS': {'name': 'FORCED SET', 'type': HeaderCodeType.FORCED_SET_RESET},
            b'KR': {'name': 'FORCED RESET', 'type': HeaderCodeType.FORCED_SET_RESET},
            b'FK': {'name': 'MULTIPLE FORCEDSET/RESET', 'type': HeaderCodeType.FORCED_SET_RESET},
            b'KC': {'name': 'FORCED SET/RESET CANCEL', 'type': HeaderCodeType.FORCED_SET_RESET},
            
            #PLC_model_code_reading
            b'MM': {'name': 'PLC MODEL READ', 'type': HeaderCodeType.PLC_MODEL_CODE_READING},
            
            #TESTING
            b'TS': {'name': 'TEST', 'type': HeaderCodeType.TESTING},
            
            #PROGRAM_AREA_ACCESSING
            b'RP': {'name': 'PROGRAM READ', 'type': HeaderCodeType.PROGRAM_AREA_ACCESSING},
            b'WP': {'name': 'PROGRAM WRITE', 'type': HeaderCodeType.PROGRAM_AREA_ACCESSING},
            
            #IO_TABLE_CREATION
            b'MI': {'name': 'I/O TABLE CREATE', 'type': HeaderCodeType.IO_TABLE_CREATION},
     
            #HOST_LINK_COMMUNICATIONS_PROCESSING
            b'XA': {'name': 'ABORT (command only)', 'type': HeaderCodeType.HOST_LINK_COMMUNICATIONS_PROCESSING},
            b'**': {'name': 'INITIALIZE (command only)', 'type': HeaderCodeType.HOST_LINK_COMMUNICATIONS_PROCESSING},
            b'IC': {'name': 'Undefined command (response only)', 'type': HeaderCodeType.HOST_LINK_COMMUNICATIONS_PROCESSING},
        }
    
        self._end_codes = {
            b'00': {'name': 'Normal completion', 'type': EndCodeType.C_MODE_END_CODE},
            b'01': {'name': 'Not executable in RUN mode', 'type': EndCodeType.C_MODE_END_CODE},
            b'02': {'name': 'Not executable in MONITOR mode', 'type': EndCodeType.C_MODE_END_CODE},
            b'03': {'name': 'UM write-protected', 'type': EndCodeType.C_MODE_END_CODE},
            b'04': {'name': 'Address over', 'type': EndCodeType.C_MODE_END_CODE},
            b'0B': {'name': 'Not executable in PROGRAM mode ', 'type': EndCodeType.C_MODE_END_CODE},
            b'13': {'name': 'FCS error', 'type': EndCodeType.C_MODE_END_CODE},
            b'14': {'name': 'Format error', 'type': EndCodeType.C_MODE_END_CODE},
            b'15': {'name': 'Entry number data error', 'type': EndCodeType.C_MODE_END_CODE},
            b'16': {'name': 'Command not supported', 'type': EndCodeType.C_MODE_END_CODE},
            b'18': {'name': 'Frame length error', 'type': EndCodeType.C_MODE_END_CODE},
            b'19': {'name': 'Not executable', 'type': EndCodeType.C_MODE_END_CODE},
            b'20': {'name': 'Could not create I/O table', 'type': EndCodeType.C_MODE_END_CODE},
            b'21': {'name': 'Not executable due to CPU Unit CPU error', 'type': EndCodeType.C_MODE_END_CODE},
            b'23': {'name': 'User memory protected', 'type': EndCodeType.C_MODE_END_CODE},
            b'A3': {'name': 'Aborted due to FCS error in transmission data', 'type': EndCodeType.C_MODE_END_CODE},
            b'A4': {'name': 'Aborted due to format error in transmission data', 'type': EndCodeType.C_MODE_END_CODE},
            b'A5': {'name': 'Aborted due to entry number data error in transmission data', 'type': EndCodeType.C_MODE_END_CODE},
            b'A8': {'name': 'Aborted due to frame length error in transmission data', 'type': EndCodeType.C_MODE_END_CODE},
        }

    
class FinsCode():
    @property
    def command_codes(self):
        return self._command_codes
        
    @property
    def end_codes(self):
        return self._end_codes

    def __init__(self):
        self._command_codes = {
            #IO_MEMORY_AREA_ACCESS
            b'0101': {'name': 'MEMORY AREA READ', 'type': FinsCommandCodeType.IO_MEMORY_AREA_ACCESS},
            b'0102': {'name': 'MEMORY AREA WRITE ', 'type': FinsCommandCodeType.IO_MEMORY_AREA_ACCESS},
            b'0103': {'name': 'MEMORY AREA FILL', 'type': FinsCommandCodeType.IO_MEMORY_AREA_ACCESS},
            b'0104': {'name': 'MULTIPLE MEMORY AREA READ', 'type': FinsCommandCodeType.IO_MEMORY_AREA_ACCESS},
            b'0105': {'name': 'MEMORY AREA TRANSFER', 'type': FinsCommandCodeType.IO_MEMORY_AREA_ACCESS},
            
            #PARAMETER_AREA_ACCESS
            b'0201': {'name': 'PARAMETER AREA READ', 'type': FinsCommandCodeType.PARAMETER_AREA_ACCESS},
            b'0202': {'name': 'PARAMETER AREA WRITE ', 'type': FinsCommandCodeType.PARAMETER_AREA_ACCESS},
            b'0203': {'name': 'PARAMETER AREA FILL', 'type': FinsCommandCodeType.PARAMETER_AREA_ACCESS},
            
            #PROGRAM_AREA_ACCESS
            b'0306': {'name': 'PROGRAM AREA READ', 'type': FinsCommandCodeType.PROGRAM_AREA_ACCESS},
            b'0307': {'name': 'PROGRAM AREA WRITE', 'type': FinsCommandCodeType.PROGRAM_AREA_ACCESS},
            b'0308': {'name': 'PROGRAM AREA CLEAR', 'type': FinsCommandCodeType.PROGRAM_AREA_ACCESS},
            
            #OPERATING_MODE_CHANGES
            b'0401': {'name': 'RUN', 'type': FinsCommandCodeType.OPERATING_MODE_CHANGES},
            b'0402': {'name': 'STOP', 'type': FinsCommandCodeType.OPERATING_MODE_CHANGES},
            
            #MACHINE_CONFIGURATION_0READING
            b'0501': {'name': 'CPU UNIT DATA READ', 'type': FinsCommandCodeType.MACHINE_CONFIGURATION_0READING},
            b'0502': {'name': 'CONNECTION DATA READ', 'type': FinsCommandCodeType.MACHINE_CONFIGURATION_0READING},
            
            #STATUS_READING
            b'0601': {'name': 'CPU UNIT STATUS READ', 'type': FinsCommandCodeType.STATUS_READING},
            b'0620': {'name': 'CYCLE TIME READ', 'type': FinsCommandCodeType.STATUS_READING},
            
            #TIME_DATA_ACCESS
            b'0701': {'name': 'CLOCK READ', 'type': FinsCommandCodeType.TIME_DATA_ACCESS},
            b'0702': {'name': 'CLOCK WRITE', 'type': FinsCommandCodeType.TIME_DATA_ACCESS},
            
            #MESSAGE_DISPLAY
            b'0920': {'name': 'MESSAGE READ/CLEAR', 'type': FinsCommandCodeType.MESSAGE_DISPLAY},
            
            #ACCESS_RIGHTS
            b'0C01': {'name': 'ACCESS RIGHT ACQUIRE', 'type': FinsCommandCodeType.ACCESS_RIGHTS},
            b'0C02': {'name': 'ACCESS RIGHT FORCED ACQUIRE', 'type': FinsCommandCodeType.ACCESS_RIGHTS},
            b'0C03': {'name': 'ACCESS RIGHT RELEASE', 'type': FinsCommandCodeType.ACCESS_RIGHTS},
            
            #ERROR_LOG
            b'2101': {'name': 'ERROR CLEAR', 'type': FinsCommandCodeType.ERROR_LOG},
            b'2102': {'name': 'ERROR LOG READ', 'type': FinsCommandCodeType.ERROR_LOG},
            b'2103': {'name': 'ERROR LOG CLEAR', 'type': FinsCommandCodeType.ERROR_LOG},
            
            #FINS_WRITE_ACCESS_LOG
            b'2140': {'name': 'FINS WRITE ACCESS LOG READ', 'type': FinsCommandCodeType.FINS_WRITE_ACCESS_LOG},
            b'2141': {'name': 'FINS WRITE ACCESS LOG CLEAR', 'type': FinsCommandCodeType.FINS_WRITE_ACCESS_LOG},
            
            #FILE_MEMORY
            b'2201': {'name': 'FILE NAME READ', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2202': {'name': 'SINGLE FILE READ', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2203': {'name': 'SINGLE FILE WRITE', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2204': {'name': 'FILE MEMORY FORMAT', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2205': {'name': 'FILE DELETE', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2207': {'name': 'FILE COPY', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2208': {'name': 'FILE NAME', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'220A': {'name': 'MEMORY AREA–FILE TRANSFER', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'220B': {'name': 'PARAMETER AREA–FILE TRANSFER', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'220C': {'name': 'PROGRAM AREA–FILE TRANSFER', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2215': {'name': 'DIRECTORY CREATE/DELETE', 'type': FinsCommandCodeType.FILE_MEMORY},
            b'2220': {'name': 'MEMORY CASSETTE TRANSFER', 'type': FinsCommandCodeType.FILE_MEMORY},
            
            #DEBUGGING
            b'2301': {'name': 'FORCED SET/RESET', 'type': FinsCommandCodeType.DEBUGGING},
            b'2302': {'name': 'FORCED SET/RESET CANCEL', 'type': FinsCommandCodeType.DEBUGGING},
            
            #SERIAL_GATEWAY_FUNCTIONS
            b'2803': {'name': 'CONVERT TO COMPOWAY/F COMMAND', 'type': FinsCommandCodeType.SERIAL_GATEWAY_FUNCTIONS},
            b'2804': {'name': 'CONVERT TO MODBUS-RTU COMMAND', 'type': FinsCommandCodeType.SERIAL_GATEWAY_FUNCTIONS},
            b'2805': {'name': 'CONVERT TO MODBUS-ASCII COMMAND', 'type': FinsCommandCodeType.SERIAL_GATEWAY_FUNCTIONS},
            b'.*': {'name': 'CONVERT TO HOST LINK FINS COMMAND', 'type': FinsCommandCodeType.SERIAL_GATEWAY_FUNCTIONS},
        }
        
        self._end_codes = {
            #NORMAL_COMPLETION
            b'0000': {'name': ' Normal completion', 'type': FinsEndCodeType.NORMAL_COMPLETION},
            b'0001': {'name': 'Service canceled', 'type': FinsEndCodeType.NORMAL_COMPLETION},
            
            #LOCAL_NODE_ERROR
            b'0101': {'name': 'Local node not in network', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
            b'0102': {'name': 'Token timeout', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
            b'0103': {'name': 'Retries failed', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
            b'0104': {'name': 'Too many send frames', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
            b'0105': {'name': 'Node address range error', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
            b'0106': {'name': 'Node address duplication', 'type': FinsEndCodeType.LOCAL_NODE_ERROR},
        }
            
        '''
        Todo: following FINS command codes are waiting for definition
        DESTINATION_NODE_ERROR
        CONTROLLER_ERROR
        SERVICE_UNSUPPORTED
        ROUTING_TABLE_ERROR
        COMMAND_FORMAT_ERROR
        PARAMETER_ERROR
        READ_NOT_POSSIBLE
        WRITE_NOT_POSSIBLE
        NOT_EXECUTABLE_IN_CURRENT_MODE
        NO_SUCH_DEVICE
        CANNOT_START_STOP
        UNIT_ERROR
        COMMAND_ERROR
        ACCESS_RIGHT_ERROR
        ABORT
        '''

