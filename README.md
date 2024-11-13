# WiFiBrute
This project is a Python script that uses the `pywifi` module to scan for available WiFi networks and attempt to connect to them using a list of passwords. The script leverages threading to speed up the process and provides a streamlined output in the terminal. 
## Features 
- **WiFi Scanning:** Lists all available WiFi networks with their SSID, BSSID, Signal strength, and Security type.
- **Brute Force Password Testing:** Attempts to connect to a selected WiFi network using a list of passwords.
- **Streamlined Output:** Displays the current password being tested in the terminal on the same line.
## Requirements - Python 3.x - `pywifi` module - WiFi adapter compatible with `pywifi`
## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wifi-brute-force.git
   cd wifi-brute-force
2. Install the required Python packages:
   ```bash
   pip install pywifi
3. Ensure your WiFi adapter is properly connected and recognized by your system.
## Usage
1. Prepare a text file containing a list of passwords (one per line), e.g., passwords.txt. Make changes for the file name in the program default password file name is 'rockyou.txt'.
2. Run the script:
   ```bash
   python wifi_attacker.py
3. Follow the on-screen prompts to:
   - Scan for available WiFi networks.
   - Select a network to target.
   - Provide the path to your password file. (Default not needed)
# Code Explanation
## Main Functions
- **scan_wifi():** Scans and lists available WiFi networks.
- **print_networks(networks):** Displays the scanned WiFi networks.
- **connect_to_wifi(ssid, password, result):** Attempts to connect to the WiFi network using the given password.
- **power_cycle_iface(iface, profile):** Power cycles the WiFi interface to reset the connection.
- **brute_force_passwords(ssid, password_file):** Iterate through passwords from a file and attempts to connect to the WiFi network.
# Example Output
  ```bash
  ###############################################################
  Network ID: 1 SSID: MyNetwork
  BSSID: xx:xx:xx:xx:xx:xx
  Signal: -50
  Security: [4]

  Enter the Network ID: 1
  Confirm the WiFi MyNetwork (y/n/r): y
  Trying password: 123456789 -----> Successfully connected to MyNetwork with password: 123456789
  ```
# Disclaimer
This tool is intended for educational purposes only. Unauthorized use of this tool to access networks is illegal and unethical. Always obtain permission from the network owner before using this tool.
# License
This project is licensed under the GNU General Public License. See the LICENSE file for more details.
# Contribute
Contributions are welcome! Please fork this repository and submit a pull request.
