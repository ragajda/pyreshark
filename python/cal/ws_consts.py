'''
@summary: Auto Generated by generate_ws_consts.py. Sets all the required constants from Wireshark.
'''

############# FIELD TYPES ##############
FT_NONE = 0
FT_PROTOCOL = 1
FT_BOOLEAN = 2
FT_UINT8 = 3
FT_UINT16 = 4
FT_UINT24 = 5
FT_UINT32 = 6
FT_UINT64 = 7
FT_INT8 = 8
FT_INT16 = 9
FT_INT24 = 10
FT_INT32 = 11
FT_INT64 = 12
FT_FLOAT = 13
FT_DOUBLE = 14
FT_ABSOLUTE_TIME = 15
FT_RELATIVE_TIME = 16
FT_STRING = 17
FT_STRINGZ = 18
FT_UINT_STRING = 19
FT_ETHER = 20
FT_BYTES = 21
FT_UINT_BYTES = 22
FT_IPv4 = 23
FT_IPv6 = 24
FT_IPXNET = 25
FT_FRAMENUM = 26
FT_PCRE = 27
FT_GUID = 28
FT_OID = 29
FT_EUI64 = 30
FT_NUM_TYPES = 31

############ DISPLAY VALUES ############
BASE_NONE = 0
BASE_DEC = 1
BASE_HEX = 2
BASE_OCT = 3
BASE_DEC_HEX = 4
BASE_HEX_DEC = 5
BASE_CUSTOM = 6

######## DISPLAY VALUES (TIME) #########
ABSOLUTE_TIME_LOCAL  = 1000
ABSOLUTE_TIME_UTC = 1001
ABSOLUTE_TIME_DOY_UTC = 1002

############## COLUMN IDS ##############
COL_8021Q_VLAN_ID = 0
COL_ABS_DATE_TIME = 1
COL_ABS_TIME = 2
COL_CIRCUIT_ID = 3
COL_DSTIDX = 4
COL_SRCIDX = 5
COL_VSAN = 6
COL_CUMULATIVE_BYTES = 7
COL_CUSTOM = 8
COL_DCE_CALL = 9
COL_DCE_CTX = 10
COL_DELTA_TIME = 11
COL_DELTA_CONV_TIME = 12
COL_DELTA_TIME_DIS = 13
COL_RES_DST = 14
COL_UNRES_DST = 15
COL_RES_DST_PORT = 16
COL_UNRES_DST_PORT = 17
COL_DEF_DST = 18
COL_DEF_DST_PORT = 19
COL_EXPERT = 20
COL_IF_DIR = 21
COL_OXID = 22
COL_RXID = 23
COL_FR_DLCI = 24
COL_FREQ_CHAN = 25
COL_BSSGP_TLLI = 26
COL_HPUX_DEVID = 27
COL_HPUX_SUBSYS = 28
COL_DEF_DL_DST = 29
COL_DEF_DL_SRC = 30
COL_RES_DL_DST = 31
COL_UNRES_DL_DST = 32
COL_RES_DL_SRC = 33
COL_UNRES_DL_SRC = 34
COL_RSSI = 35
COL_TX_RATE = 36
COL_DSCP_VALUE = 37
COL_INFO = 38
COL_COS_VALUE = 39
COL_RES_NET_DST = 40
COL_UNRES_NET_DST = 41
COL_RES_NET_SRC = 42
COL_UNRES_NET_SRC = 43
COL_DEF_NET_DST = 44
COL_DEF_NET_SRC = 45
COL_NUMBER = 46
COL_PACKET_LENGTH = 47
COL_PROTOCOL = 48
COL_REL_TIME = 49
COL_REL_CONV_TIME = 50
COL_DEF_SRC = 51
COL_DEF_SRC_PORT = 52
COL_RES_SRC = 53
COL_UNRES_SRC = 54
COL_RES_SRC_PORT = 55
COL_UNRES_SRC_PORT = 56
COL_TEI = 57
COL_UTC_DATE_TIME = 58
COL_UTC_TIME = 59
COL_CLS_TIME = 60
NUM_COL_FMTS = 61

############## ENCODINGS ###############
ENC_BIG_ENDIAN = 0x00000000
ENC_LITTLE_ENDIAN = 0x80000000
ENC_TIME_TIMESPEC = 0x00000000
ENC_TIME_NTP = 0x00000002
ENC_CHARENCODING_MASK = 0x7FFFFFFE
ENC_ASCII = 0x00000000
ENC_UTF_8 = 0x00000002
ENC_UTF_16 = 0x00000004
ENC_UCS_2 = 0x00000006
ENC_EBCDIC = 0x00000008
ENC_NA = 0x00000000

####### DISPLAY VALUES (STRINGS) #######
BASE_DISPLAY_E_MASK = 0x0F
BASE_RANGE_STRING = 0x10
BASE_EXT_STRING = 0x20

################# MISC #################

if "ENC_ASCII" in dir():
    ENC_TEXT_DEFAULT = ENC_ASCII
elif "ENC_UTF8" in dir():
    ENC_TEXT_DEFAULT = ENC_UTF8
else:
    ENC_TEXT_DEFAULT = ENC_NA
    
HFILL = (0, 0, 0, 0, None, None)

DATA = "data"
REMAINING_LENGTH = -1
