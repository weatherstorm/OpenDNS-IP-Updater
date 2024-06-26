# OpenDNS IP Updater

This Python script updates your IP address with OpenDNS.

## Setup

### 1. Installation

1. **Python Installation**: Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Dependencies Installation**: Install the necessary Python packages by running the following command:
   ```
   pip install requests
   ```

### 2. Configuration

1. **Edit Configuration File**: Open the configuration file (`config_file`) in a text editor and fill in the required information:
   - `login`: Your OpenDNS login username.
   - `password`: Your OpenDNS account password.
   - `server`: The OpenDNS server URL (`updates.opendns.com`).
   - `networkname`: The name of the network to update (e.g., `Home`).

2. **Set Paths**: Set the paths to your configuration file (`config_file`) and the file to store the previous IP address (`previous_ip_file`) in the script.

## Usage

1. **Run the Script**: Open a terminal or command prompt, navigate to the directory where the script is saved, and run the script using the following command:
   ```
   python script_name.py
   ```
   Replace `script_name.py` with the name of the Python script file.

2. **Check Log File**: After running the script, check the log file (`opendns_update.log`) to verify the script's execution status and any updates made to the IP address.

## Additional Notes

- **Logging**: The script logs its actions to the `opendns_update.log` file in the same directory as the script. Check this file for detailed information about the script's execution.

- **Execution Frequency**: Depending on your needs, you may want to schedule the script to run periodically using a scheduler (e.g., cron on Linux, Task Scheduler on Windows) to ensure your IP address is updated regularly.

- **Security**: Keep your configuration file (`config_file`) secure, especially if it contains sensitive information such as your OpenDNS account password.

## Troubleshooting
- **Error fetching current IP address: HTTPSConnectionPool(host='api64.ipify.org', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x75e45250>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))**: If you encounter this error fetching the current IP address, follow these troubleshooting steps:
    1. Check your internet connection.
    2. Verify DNS configuration:
        - **Linux**: Check `/etc/resolv.conf` and make sure the DNS is properly set. If it isn't, edit the .conf with addresses to a DNS server.
        - **Windows**: Set IPv6 DNS in network settings.
    3. Restart DNS service or flush DNS cache:
        - **Linux**: Restart networking or `systemd-resolved` service.
        - **Windows**: Run `ipconfig /flushdns` and restart your computer.
    4. Test DNS resolution using `nslookup api64.ipify.org` again.
    5. Temporarily disable firewall or security software and test again.
    6. Check router DNS settings or try using a different DNS service.


