"""
Mapping AVR32protocol error codes to more human friendly strings
"""
AVR32_ERRORS = {}

AVR32_ERRORS[0x00] = "AVR32_FAILURE_OK: All OK"
AVR32_ERRORS[0x01] = "AVR32_FAILURE_NACK: NACK received from target"
AVR32_ERRORS[0x02] = "AVR32_FAILURE_LENGTH: Incorrect packet length"
AVR32_ERRORS[0x03] = "AVR32_FAILURE_RECEIVE_TIMEOUT: Receive function timeout"
AVR32_ERRORS[0x04] = "AVR32_FAILURE_RECEIVE_SYNC: Receive did not sync"
AVR32_ERRORS[0x05] = "AVR32_FAILURE_RECEIVE_LENGTH: Incorrect packet length"
AVR32_ERRORS[0x06] = "AVR32_FAILURE_TRANSMIT_OVERFLOW: Transmit buffer overflow"
AVR32_ERRORS[0x07] = "AVR32_FAILURE_INVALID_MEMTYPE: Invalid memtype given"
AVR32_ERRORS[0x08] = "AVR32_FAILURE_WRITE_ERROR: A write error occurred "
AVR32_ERRORS[0x09] = "AVR32_FAILURE_WRITE_BUSY: Busy signal received"
AVR32_ERRORS[0x0A] = "AVR32_FAILURE_READ_SHORT: Short-packet received"
AVR32_ERRORS[0x0B] = "AVR32_FAILURE_ERASE_TIMEOUT: Erase command timeout "
AVR32_ERRORS[0x0C] = "AVR32_FAILURE_FLASHREADY_TIMEOUT: Flash controller busy"
AVR32_ERRORS[0x0D] = "AVR32_FAILURE_ILLEGAL_STATE: Illegal state specified"
AVR32_ERRORS[0x0E] = "AVR32_FAILURE_NOT_SUPPORTED: Feature not supported"
AVR32_ERRORS[0x0F] = "AVR32_FAILURE_PROGE: Programming error"
AVR32_ERRORS[0x10] = "AVR32_FAILURE_LOCKE: Lock error"
AVR32_ERRORS[0x11] = "AVR32_FAILURE_STEP_TIMEOUT: Single stepping timeout"
AVR32_ERRORS[0x12] = "AVR32_FAILURE_READ_BUSY: Busy bit was set"
AVR32_ERRORS[0x13] = "AVR32_FAILURE_READ_ERROR: Error bit was set"
AVR32_ERRORS[0x14] = "AVR32_FAILURE_HARDWARE_ERROR: aWire hardware init error"
AVR32_ERRORS[0x15] = "AVR32_FAILURE_NO_CONTACT: No response from aWire "
AVR32_ERRORS[0x16] = "AVR32_FAILURE_NO_TARGET_POWER: No target power "
AVR32_ERRORS[0x17] = "AVR32_FAILURE_NOT_IMPLEMENTED: Command not implemented"
AVR32_ERRORS[0x18] = "AVR32_FAILURE_UNSUPPORTED_HARDWARE: Hardware not supported"
AVR32_ERRORS[0x19] = "AVR32_FAILURE_JTAGM_INIT_ERROR: JTAG master init error"
AVR32_ERRORS[0x1A] = "AVR32_FAILURE_NO_DEVICE_FOUND: devices == 0!"
AVR32_ERRORS[0x1B] = "AVR32_FAILURE_JTAGM_ERROR: JTAG master error"
AVR32_ERRORS[0x1D] = "AVR32_FAILURE_INVALID_SIZE: Too many or too few bytes"
AVR32_ERRORS[0x1E] = "AVR32_FAILURE_INVALID_ADDRESS: Bad address requested"
AVR32_ERRORS[0x1F] = "AVR32_FAILURE_AWIRE_SET_BAUD_ERROR: Failure setting baud"
AVR32_ERRORS[0x20] = "AVR32_FAILURE_INVALID_DATA: Data invalid, discard it"
AVR32_ERRORS[0x21] = "AVR32_FAILURE_INVALID_PHYSICAL_MODE: Physical mode not valid  "
AVR32_ERRORS[0x22] = "AVR32_FAILURE_INVALID_CLOCK_SPEED: The clock is not valid"
AVR32_ERRORS[0x23] = "AVR32_FAILURE_AWIRE_ERROR_RESPONSE: Error response received"
AVR32_ERRORS[0x24] = "AVR32_FAILURE_AWIRE_OVERFLOW: Overflow data RX overflow"
AVR32_ERRORS[0x24] = "AVR32_FAILURE_AWM_ERROR: aWire master error"
AVR32_ERRORS[0x25] = "AVR32_FAILURE_AWIRE_CRC: aWire CRC error"
AVR32_ERRORS[0x26] = "AVR32_FAILURE_AWIRE_TUNE: aWire TUNE error"
AVR32_ERRORS[0x29] = "AVR32_FAILURE_JTAGM_WAS_BUSY: JTAG master busy "
AVR32_ERRORS[0x2A] = "AVR32_FAILURE_JTAGM_TIMEOUT: JTAG master timeout"
AVR32_ERRORS[0x2B] = "AVR32_FAILURE_BAD_VALUE: Invalid parameter value"
AVR32_ERRORS[0x2C] = "AVR32_FAILURE_ERASE_ERROR: Erase error"
AVR32_ERRORS[0x2D] = "AVR32_FAILURE_CONFIG_ERROR: Insufficient config info"
AVR32_ERRORS[0x2E] = "AVR32_FAILURE_INVALID_EMULATOR_MODE: Mode is not valid "
AVR32_ERRORS[0x2F] = "AVR32_FAILURE_CPU_DIRTY_TIMEOUT: CPU wait timeout"
AVR32_ERRORS[0x30] = "AVR32_FAILURE_CPU_MODE: CPU not in debug mode "
AVR32_ERRORS[0x31] = "AVR32_FAILURE_CPU_DEBUG_MODE_TIMEOUT: CPU debug mode timeout"
AVR32_ERRORS[0x32] = "AVR32_FAILURE_AWIRE_RW_STATUS: Unexpected status"
AVR32_ERRORS[0x33] = "AVR32_FAILURE_TRANSMIT_TIMEOUT: Data TX timeout"
AVR32_ERRORS[0xFE] = "AVR32_FAILURE_INTERNAL_RESPONSE_ERROR: Near disaster"
AVR32_ERRORS[0xFF] = "AVR32_FAILURE_UNKNOWN: Disaster"
