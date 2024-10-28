#!/usr/bin/python3

import sys
import signal
import re

# initialize variables
total_size = 0
line_count = 0
status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
valid_status_codes = set(status_counts.keys())

# Regular expression pattern for matching the required log format
log_pattern = re.compile(
        r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
        )


def print_statistics():
    """Prints the total file size and status code counts in ascending order."""
    print("File size:", total_size)
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_interrupt(signal, frame):
    """Handle the CTRL+C keyboard interrupt."""
    print_statistics()
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, handle_interrupt)

# Process each line from stdin
for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)

    if match:
        ip, date, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        # Update the total file size
        total_size += file_size

        # Update the status code count if it's a valid code
        if status_code in valid_status_codes:
            status_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()
    else:
        continue

# Print final statistics after reading all lines
print_statistics()
