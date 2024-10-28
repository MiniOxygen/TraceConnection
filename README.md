# IP Geolocation from Traceroute

This script performs a traceroute to `target`, extracts the IP addresses of each hop, and fetches their city locations using the IP-API service.

## Prerequisites

The script requires the following packages:
- `os` (Standard library, no need to install)
- `re` (Standard library, no need to install)
- `requests` (`pip install requests`)
