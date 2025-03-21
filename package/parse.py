def get_hex_description_of_apdu_protocol(p1: int, p2: int) -> str:
    """
    https://www.eftlab.com/knowledge-base/complete-list-of-apdu-responses
    """

    hex_table = {
        "6A00": "No information given (Bytes P1 and/or P2 are incorrect)",
        "6A80": "The parameters in the data field are incorrect.",
        "6A81": "Function not supported",
        "6A82": "File not found",
        "6A83": "Record not found",
        "6A84": "There is insufficient memory space in record or file",
        "6A85": "Lc inconsistent with TLV structure",
        "6A86": "Incorrect P1 or P2 parameter.",
        "6A87": "Lc inconsistent with P1-P2",
        "6A88": "Referenced data not found",
        "6A89": "File already exists",
        "6A8A": "DF name already exists.",
        "6AF0": "Wrong parameter value",
        "6B00": "Wrong parameter(s) P1-P2",
        "6C00": "Incorrect P3 length.",
        "6D00": "Instruction code not supported or invalid",
        "6E00": "Class not supported",
        "6F00": "Command aborted - more exact diagnosis not possible (e.g., operating system error).",
        "9000": "Command successfully executed (OK).",
        "9404": "FID not found, record not found or comparison pattern not found.",
        "9804": "Access conditions not satisfied, authentication failed.",
        "9D10": "Insufficient memory to load application",
        "9E00": "PIN not installed"
    }

    # Convert integers to 2-digit hex strings
    p1_hex = f"{p1:02X}"
    p2_hex = f"{p2:02X}"
    hex_code = f"{p1_hex}{p2_hex}"

    # Return the description if the hex code exists in the table
    return hex_table.get(hex_code, "Unknown hex code")

