import csv

def read_asns_from_file(filename):
    with open(filename, 'r') as file:
        asns = file.readlines()
    # Strip newlines and remove empty lines
    asns = [asn.strip() for asn in asns if asn.strip()]
    return asns

def read_asn_ranges(filename):
    asn_ranges = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            cidr_range = row[0]
            asn = row[3]
            if asn not in asn_ranges:
                asn_ranges[asn] = []
            asn_ranges[asn].append(cidr_range)
    return asn_ranges

def main():
    asns = read_asns_from_file('asn.txt')
    asn_ranges = read_asn_ranges('../asn_ranges/asn_ranges.csv')

    with open('ip_range.conf', 'w') as output_file:
        for asn in asns:
            output_file.write(f"#{asn}\n")
            if asn in asn_ranges:
                for cidr_range in asn_ranges[asn]:
                    output_file.write(f"Require not ip\t{cidr_range}\n")
            else:
                output_file.write("No CIDR ranges found\n")
            output_file.write("\n")

if __name__ == "__main__":
    main()
