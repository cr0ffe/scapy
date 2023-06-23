import argparse
from scapy.all import *

def merge_pcaps(input_files, output_file):
    # We'll keep all the packets from all the files in this list
    packets = []

    # Go through each file we're given
    for file in input_files:
        # Read the packets from the current file
        pcap = rdpcap(file)

        # Add the packets to our list
        packets.extend(pcap)

    # Write all the packets to the output file
    wrpcap(output_file, packets)

def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description='Merge PCAP files.')
    parser.add_argument('input_files', type=str, nargs='+', help='The input PCAP files.')
    parser.add_argument('output_file', type=str, help='The output PCAP file.')

    # Parse arguments
    args = parser.parse_args()

    # Merge the PCAP files
    merge_pcaps(args.input_files, args.output_file)

if __name__ == '__main__':
    main()
