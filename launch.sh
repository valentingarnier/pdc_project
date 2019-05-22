#!/bin/bash
python3 createInput.py
python3 client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
python3 main.py
