#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))

def main():
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) == 9:
                ip, _, _, _, _, status, size = parts[:7]
                if status in status_counts:
                    total_size += int(size)
                    status_counts[status] += 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
