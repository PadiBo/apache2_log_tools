import ipaddress

def read_ip_list_from_file(filename):
    ip_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                ip_list.append(line)
    return ip_list

def read_ip_ranges_from_file(filename):
    ip_ranges = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                ip_ranges.append(line)
    return ip_ranges

def check_ip_in_ranges(ip, ip_ranges):
    for ip_range in ip_ranges:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(ip_range):
            return False
    return True

def main():
    ip_list = read_ip_list_from_file("ip.txt")
    ip_ranges = read_ip_ranges_from_file("ranges.txt")
    
    ips_not_in_ranges = []
    for ip in ip_list:
        if check_ip_in_ranges(ip.strip(), ip_ranges):
            ips_not_in_ranges.append(ip.strip())

    if ips_not_in_ranges:
        print("Folgende IPs liegen nicht in den angegebenen IP-Bereichen:")
        for ip in ips_not_in_ranges:
            print(ip)
    else:
        print("Alle IPs liegen in den angegebenen IP-Bereichen.")

if __name__ == "__main__":
    main()
input("")