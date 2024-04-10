#!/usr/bin/env python3
import requests
import logging
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

# Configure logging
logging.basicConfig(filename='opendns_update.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_previous_ip(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.warning(f"Previous IP file '{filename}' not found")
        return None

def write_current_ip(filename, ip):
    try:
        with open(filename, 'w') as file:
            file.write(ip)
    except Exception as e:
        logging.error(f"Failed to write current IP to file '{filename}': {e}")

def update_opendns_ip(config_file, previous_ip_file):
    # Read configuration from file
    config = {}
    try:
        with open(config_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    value = value.strip().strip("'")  # Remove single quotes around the value
                    config[key.strip()] = value
    except FileNotFoundError:
        logging.error(f"Configuration file '{config_file}' not found")
        return

    # Check if required parameters are present
    required_keys = ['login', 'password', 'server', 'networkname']
    if not all(key in config for key in required_keys):
        logging.error("Missing required parameters in configuration file")
        return

    # Get current public IP address
    try:
        response = requests.get('https://api64.ipify.org')
        current_ip = response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching current IP address: {e}")
        return

    # Read previous IP address
    previous_ip = read_previous_ip(previous_ip_file)

    # If previous IP is different from current IP, update OpenDNS
    if current_ip != previous_ip:
        # Construct URL for updating IP address with OpenDNS
        auth_string = urlencode({'username': config['login'], 'password': config['password']})
        url = f"https://{config['server']}/nic/update?hostname={config['networkname']}&myip={current_ip}&{auth_string}"

        # Send GET request
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info("IP address updated successfully")
                # Write current IP to file
                write_current_ip(previous_ip_file, current_ip)
            else:
                logging.error(f"Failed to update IP address: {response.text}")
        except requests.RequestException as e:
            logging.error(f"Error updating IP address: {e}")
    else:
        logging.info("Current IP address matches previous IP, no update needed")

if __name__ == "__main__":
    config_file = "path/to/your/config/file/opendns.conf"
    previous_ip_file = "path/to/your/previous_ip/file/IP.txt"
    update_opendns_ip(config_file, previous_ip_file)
  
