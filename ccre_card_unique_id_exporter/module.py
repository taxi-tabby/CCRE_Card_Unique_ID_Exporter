from ccre_card_unique_id_exporter.parse import get_hex_description_of_apdu_protocol
import smartcard
from smartcard.System import readers
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString





COMMAND_GET_CARD_SERIAL = [0x00, 0xCA, 0x01, 0x11]        # 카드 시리얼 요청 명령
COMMAND_GET_CARD_SERIAL_LENGTH = [0x08]                   # 명령 예상 길이



"""
공동망 AID 선택 명령어
명령 구성 [COMMAND_DO_SELECT_AID + NET_WORK_AID_DF_HEADER + NETWORK_AID_DF_OF_~~~ + COMMAND_DO_SELECT_AID_LENGTH]
"""
COMMAND_DO_SELECT_AID = [0x00, 0xa4, 0x04, 0x00, 0x07]    # 애플릿 선택 명령
COMMAND_DO_SELECT_AID_LENGTH = [0x2a]                     # 명령 예상 길이
NETWORK_AID_DF_HEADER = [0Xd4, 0x10, 0x65, 0x09, 0x90]    # 공동망 해더 바이너리 (각 종류 앞에 들어가는 바이너리리)
NETWORK_AID_DF_OF_FINANCIAL = [0x00, 0x10]                # 공동망 정의 - 1. 신용, 금융
NETWORK_AID_DF_OF_DIRECT_CASH_CARD = [0X30, 0x10]         # 공동망 정의 - 2. 직불
NETWORK_AID_DF_OF_CYBER_CASH_CARD = [0X00, 0x20]          # 공동망 정의 - 3. 전자화폐
NETWORK_AID_DF_OF_SIGN = [0x00, 0x30]                     # 공동망 정의 - 4. 인증서(서명용)
NETWORK_AID_DF_OF_DISTRIBUTE = [0X00, 0x40]               # 공동망 정의 - 5. 키 분배용


def get_card_reader_list():
    """Return a list of available smart card readers."""
    available_readers = readers()
    if available_readers:
        # print(f"Found readers: {available_readers}")
        return available_readers
    else:
        print("No smart card readers found.")
        return None


def find_card_reader():
    """Return the first available smart card reader."""
    list = get_card_reader_list()
    if list is not None:
        return list[0]
    else:
        return None






# 카드 리더기 연결 생성
def create_new_reader_connection(reader, protocol='T0'):
    """Creates a connection to the card reader.

    Args:
        reader: The card reader object.
        protocol: The connection protocol ('T0', 'T1', 'RAW').

    Returns:
        A CardConnection object or None (in case of an error).
    """
    protocol_mapping = {
        'T0': CardConnection.T0_protocol,
        'T1': CardConnection.T1_protocol,
        'RAW': CardConnection.RAW_protocol,
    }

    if protocol not in protocol_mapping:
        raise ValueError(f"Invalid protocol: {protocol}. Choose from 'T0', 'T1', or 'RAW'.")

    try:
        connection = reader.createConnection()
        connection.connect(protocol_mapping[protocol])
        return connection
    except smartcard.Exceptions.CardConnectionException as e:
        print(f"Error creating connection: {e}")
        return None




def select_network_aid(connection, aid_type):
    """ Function to select a network AID.
        Sends an APDU command to select the network AID.
        Args:
            connection: The card reader connection object.
            aid_type: The type of network AID to select. [financial | direct_cash_card | cyber_cash_card | sign | distribute]
        Returns:
            If the AID selection is successful, returns the response data; otherwise, returns None.
    """
    
    # AID 타입에 따라 적절한 AID를 선택
    aid_mapping = {
        "financial": NETWORK_AID_DF_OF_FINANCIAL,
        "direct_cash_card": NETWORK_AID_DF_OF_DIRECT_CASH_CARD,
        "cyber_cash_card": NETWORK_AID_DF_OF_CYBER_CASH_CARD,
        "sign": NETWORK_AID_DF_OF_SIGN,
        "distribute": NETWORK_AID_DF_OF_DISTRIBUTE,
    }

    if aid_type not in aid_mapping:
        print(f"Invalid AID type: {aid_type}")
        return None

    # AID 선택 APDU 명령어 생성
    select_aid_apdu = COMMAND_DO_SELECT_AID + NETWORK_AID_DF_HEADER + aid_mapping[aid_type] + COMMAND_DO_SELECT_AID_LENGTH

    # print(f"Selecting {aid_type.capitalize()} of [{toHexString(aid_mapping[aid_type])}] --- network AID: [{toHexString(select_aid_apdu)}]")

    try:
        # AID 선택 APDU 전송
        _, sw1, sw2 = connection.transmit(select_aid_apdu)

        # 응답 및 상태 코드 확인
        return sw1, sw2
    except smartcard.Exceptions.CardConnectionException as e:
        print(f"Error during APDU transmission: {e}")
        return None




# 카드의 CSN을 요청하는 함수
def get_card_serial_number(connection) ->  (list | set | None):
    """Sends an APDU command to request the unique card serial number (CSN)."""

    # AID 선택 APDU 명령어 생성
    get_csn_apdu = COMMAND_GET_CARD_SERIAL + COMMAND_GET_CARD_SERIAL_LENGTH


    try:
        # CSN 요청 APDU 전송
        response, sw1, sw2 = connection.transmit(get_csn_apdu)
        

        # 응답 및 상태 코드 확인
        # print(f"Response: {toHexString(response)}")
        # print(f"SW1 SW2: {hex(sw1)} {hex(sw2)}")

        responseStr = get_hex_description_of_apdu_protocol(sw1, sw2)

        if sw1 == 0x90 and sw2 == 0x00:
            # print("CSN retrieval successful.")
            return response  # CSN 데이터 반환
        else:
            print("CSN retrieval failed: ", responseStr)
            return {responseStr, sw1, sw2}  # 실패 사유 반환

    except smartcard.Exceptions.CardConnectionException as e:
        print(f"Error during APDU transmission: {e}")
        return None