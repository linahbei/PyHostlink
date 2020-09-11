from enum import Enum

class UnitType(Enum):
    UNKNOWN = 'Unknown'
    SINGLE = 'Single Unit'
    MULTI = 'Multi Units'

    
class ProtocolType(Enum):
    UNKNOWN = 'Unknown'
    C_MODE = 'C-mode'
    FINS = 'FINS'


class DirectionType(Enum):
    UNKNOWN = 'Unknown'
    COMMAND = 'Command'
    RESPONSE = 'Response'


class HeaderCodeType(Enum):
    EXTENSION_4BYTES_HEADER_CODE = "Extension 4 bytes header codes"
    EXTENSION_HEADER_CODE = "Extension header codes"
    FINS_OVER_HOSTLINK = "Extension FINS protocol header code"
    IO_MEMORY_READING = "I/O memory reading"
    IO_MEMORY_WRITING = "I/O memory writing"
    TIMER_COUNTER_SV_READING = "Timer/counter SV reading"
    TIMER_COUNTER_SV_CHANGING = "Timer/counter SV changing"
    CPU_UNIT_STATUS = "CPU Unit status"
    FORCED_SET_RESET = "Forced set/reset"
    PLC_MODEL_CODE_READING = "PLC model code reading"
    TESTING = "Testing"
    PROGRAM_AREA_ACCESSING = "Program area accessing"
    IO_TABLE_CREATION = "I/O table creation"
    IO_MEMORY_AREA_REG_AND_READING = "I/O memory area registration and reading"
    HOST_LINK_COMMUNICATIONS_PROCESSING = "Host Link communications processing"
    
    
class EndCodeType(Enum):
    C_MODE_END_CODE = "Host Link C-mode end code"
    
    
class FinsCommandCodeType(Enum):
    IO_MEMORY_AREA_ACCESS = "I/O memory area access"
    PARAMETER_AREA_ACCESS = "Parameter area access"
    PROGRAM_AREA_ACCESS = "Program area access"
    OPERATING_MODE_CHANGES = "Operating mode changes"
    MACHINE_CONFIGURATION_0READING = "Machine configuration reading"
    STATUS_READING = "Status reading"
    TIME_DATA_ACCESS = "Time data access"
    MESSAGE_DISPLAY = "Message display"
    ACCESS_RIGHTS = "Access rights"
    ERROR_LOG = "Error log"
    FINS_WRITE_ACCESS_LOG = "FINS write access log"
    FILE_MEMORY = "File memory"
    DEBUGGING = "Debugging"
    SERIAL_GATEWAY_FUNCTIONS = "Serial Gateway functions"
    
    
class FinsEndCodeType(Enum):
    NORMAL_COMPLETION = "Normal completion"
    LOCAL_NODE_ERROR = "Local node error"
    DESTINATION_NODE_ERROR = "Destination node error"
    CONTROLLER_ERROR = "Controller error"
    SERVICE_UNSUPPORTED = "Service unsupported"
    ROUTING_TABLE_ERROR = "Routing table error"
    COMMAND_FORMAT_ERROR = "Command format error"
    PARAMETER_ERROR = "Parameter error"
    READ_NOT_POSSIBLE = "Read not possible"
    WRITE_NOT_POSSIBLE = "Write not possible"
    NOT_EXECUTABLE_IN_CURRENT_MODE = "Not executable in current mode"
    NO_SUCH_DEVICE = "No such device"
    CANNOT_START_STOP = "Cannot start/stop"
    UNIT_ERROR = "Unit error"
    COMMAND_ERROR = "Command error"
    ACCESS_RIGHT_ERROR = "Access right error"
    ABORT = "Abort"
    
    
class FinsUnitConnectionType(Enum):
    CONNECTED_DIRECTLY = "CPU Unit Directly Connected to the Host Computer"
    ON_A_NETWORK = "CPU Unit on a Network"

