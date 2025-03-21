# CCRE

## Overview

This is a simple Python library for reading smart cards and extracting their unique card serial numbers (CSN). It provides basic functionality to interact with smart card readers and perform operations like selecting AID files and retrieving card serial numbers.

## Example Usage

```python
# FIND card reader
reader = find_card_reader()  # or find card reader by get_card_reader_list()

if reader:
    # MAKE a connection
    connection = create_new_reader_connection(reader, 'T0')

    # SELECT aid file of financial
    select_network_aid(connection, 'financial')

    # GET card serial number
    csv = get_card_serial_number(connection)
    print(f"Card serial number: {csv}")

else:
    print("No reader found.")
```

## Dependencies

This library requires the following dependencies:

- `pyscard`: For interacting with smart card readers.

Install dependencies using:

```bash
pip install pyscard
```

## Features

- Detect available smart card readers.
- Establish a connection with a smart card reader.
- Select specific AID files on the card.
- Retrieve the unique card serial number (CSN).

## License

This project is licensed under the MIT License.