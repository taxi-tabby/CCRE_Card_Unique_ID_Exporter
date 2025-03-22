# CCRE

## Overview

This is a simple Python library for reading smart cards and extracting their unique card serial numbers (CSN). It provides basic functionality to interact with smart card readers and perform operations like selecting AID files and retrieving card serial numbers.

## Installation
```bash
pip install CCRE-Card-Unique-ID-Exporter
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