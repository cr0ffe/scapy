# Import libraries: argparse for handling command line arguments, scapy for packet manipulation, 
# defaultdict for easily counting VLANs
import argparse
from scapy.all import *
from collections import defaultdict

# Define a function to analyze the pcap file
def analyze_pcap(input_file):
    # Use scapy's rdpcap function to read the pcap file and store the packets
    packets = rdpcap(input_file)
    
    # Create a defaultdict. It's like a regular dictionary, but it doesn't throw a KeyError 
    # if you try to access or modify a key that doesn't exist. Instead, it will create a 
    # new item with the provided default value, in this case, int() which defaults to 0.
    vlan_ids = defaultdict(int)

    # Loop through all the packets in the file
    for packet in packets:
        # As long as the packet has a Dot1Q (VLAN) layer...
        while 'Dot1Q' in packet:
            # ...increment the count for this packet's VLAN ID
            vlan_ids[packet['Dot1Q'].vlan] += 1
            # Then go deeper into the packet by setting packet to its payload. 
            # This allows us to handle QinQ VLAN stacking by looping until no more Dot1Q layers are found.
            packet = packet['Dot1Q'].payload

    # Loop through the VLAN IDs we found, in numerical order
    for vlan_id in sorted(vlan_ids):
        # Print each VLAN ID and its count
        print(f"VLAN ID: {vlan_id} - Count: {vlan_ids[vlan_id]}")

# Define the main function to handle arguments and call analyze_pcap
def main():
    # Create an ArgumentParser object to handle command line arguments
    parser = argparse.ArgumentParser(description='Extract VLAN IDs from a PCAP file.')
    # Add an argument for the input file. The user must provide this.
    parser.add_argument('input_file', type=str, help='The input PCAP file.')
    
    # Call parse_args to convert command line arguments into a namespace accessible via dot notation
    args = parser.parse_args()
    
    # Call analyze_pcap with the provided input file
    analyze_pcap(args.input_file)

# If this script is being run (as opposed to being imported), call the main function
if __name__ == '__main__':
    main()
