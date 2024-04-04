import csv
import requests
import gzip
import os

from ipaddress import IPv4Address, IPv4Network

def download_extract_file(url, download_path):
    response = requests.get(url)
    with open(download_path, 'wb') as f:
        f.write(response.content)

    # Entpacke die Datei
    with gzip.open(download_path, 'rb') as f_in, open(download_path[:-3], 'wb') as f_out:
        f_out.write(f_in.read())

def calculate_cidr(ip_start, ip_end):
    ip_start = int(IPv4Address(ip_start))
    ip_end = int(IPv4Address(ip_end))

    # Finde die Praefixlaenge durch die Anzahl der gemeinsamen Bits in den beiden IP-Adressen
    prefix_length = 32
    mask = 0xFFFFFFFF

    while (ip_start & mask) != (ip_end & mask):
        prefix_length -= 1
        mask <<= 1

    # Erstelle die CIDR-Notation
    network = IPv4Network((ip_start, prefix_length), strict=False)
    return str(network)

def process_ip2asn(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)

        # Neue Reihenfolge der Spalten
        header = ["CIDR", "Country", "ASN and ASN Name"]
        writer.writerow(header)

        for line in reader:
            ip_range = calculate_cidr(line[0], line[1])  # CIDR-Bereich berechnen
            asn = line[2]
            country = line[3]
            asn_name = line[4]

            # Die Spalten "ASN" und "ASN Name" zusammenführen und mit einem Leerzeichen trennen
            combined_asn = f"AS{asn} {asn_name}"

            # Die Reihenfolge der Spalten ändern
            writer.writerow([ip_range, country, combined_asn])

if __name__ == "__main__":
    download_url = "https://iptoasn.com/data/ip2asn-v4.tsv.gz"
    download_path = "ip2asn-v4.tsv.gz"
    output_file = "asn_ranges.csv"

    # Datei herunterladen und entpacken
    download_extract_file(download_url, download_path)

    # Verarbeite die heruntergeladene Datei
    process_ip2asn(download_path[:-3], output_file)

    # Lösche die heruntergeladene und entpackte Datei
    os.remove(download_path[:-3])
    os.remove(download_path)
    
    print("Verarbeitung abgeschlossen. Ergebnis wurde in output.csv gespeichert.")
