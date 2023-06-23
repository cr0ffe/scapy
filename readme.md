Print VLANs present in PCAP (ascending output + count) Usage:

`python scapy_argparse_vlan1.py mypcap.pcap`

Outputs: 

```
WARNING: No IPv4 address found on en1 !
WARNING: No IPv4 address found on en2 !
WARNING: more No IPv4 address found on bridge0 !
VLAN ID: 10 - Count: 10
VLAN ID: 118 - Count: 10
```

Merge Multiple PCAPs into one PCAP, Usage:

`python3 scapy_merge_pcaps.py dsearch_2581_80_1686037547_1.pcap gfm_cyberdyne_20230516145419_7wgu9_1.pcap outputmerge.pcap`

Outputs:

Pre-merge
```
1035114 May 16 11:21 gfm_cyberdyne_20230516145419_7wgu9_1.pcap
914856 Jun  6 03:49 dsearch_2581_80_1686037547_1.pcap
```

Post-merge
```
1035114 May 16 11:21 gfm_cyberdyne_20230516145419_7wgu9_1.pcap
914856 Jun  6 03:49 dsearch_2581_80_1686037547_1.pcap
1949946 Jun 23 19:03 outputmerge.pcap
```
