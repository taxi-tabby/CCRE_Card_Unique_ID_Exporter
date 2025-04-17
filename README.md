# CCRE

## Overview

This is a simple Python library for reading smart cards and extracting their unique card serial numbers (CSN). It provides basic functionality to interact with smart card readers and perform operations like selecting AID files and retrieving card serial numbers.

---
Please note that the latest updates and information about this library are maintained on GitHub.


> This card! IC chip attached this thing is compatible one. maybe
![itsme.png](./___itsme.png)




## Installation
```bash
pip install CCRE-Card-Unique-ID-Exporter
```

## Method
```python

# Return reader objects
get_card_reader_list() -> [object]
find_card_reader() ->  object contained list


# Receive a reader object and create a connection.
# - param [protocol]
# 'T0' : T0 APDU communication
# 'T1' : T1 APDU communication
# 'RAW' : raw~
create_new_reader_connection(reader, protocol)

# selc
# - param [aid_type]
# financial : credit card
# direct_cash_card : debit card
# cyber_cash_card : [Cards present in the card protocol design (not identified)]
# sign : Certificates in Smart card type
# distribute : [Cards present in the card protocol design (not identified)]
select_network_aid(connection, aid_type)


# Recognized card's CSN is returned via the APDU protocol
get_card_serial_number(connection) -> list or something 
```


## Example Usage

```python
from ccre_card_unique_id_exporter import find_card_reader, create_new_reader_connection, select_network_aid, get_card_serial_number

# FIND card reader
reader = find_card_reader()  # or find card reader by get_card_reader_list()

if reader:
    # MAKE a connection
    connection = create_new_reader_connection(reader, 'T0')

    # SELECT aid file of financial
    select_network_aid(connection, 'financial')

    # GET card serial number
    csn = get_card_serial_number(connection)
    print(f"Card serial number: {csn}")

else:
    print("No reader found.")
```

#### Response
```console
Card serial number: [n, n, n, n, n, n, n]"
```
The card serial number (CSN) returned is an 8-byte list value. This format adheres to international standards for smart card identification, ensuring compatibility across various systems and applications.

## Dependencies

This library requires the following dependencies:

- `pyscard`: For interacting with smart card readers.

## Features

- Detect available smart card readers.
- Establish a connection with a smart card reader.
- Select specific AID files on the card.
- Retrieve the unique card serial number (CSN).

## License

This project is licensed under the MIT License.