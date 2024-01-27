import dns.resolver

# Getting a domain from outside
domain = input("Add your domain name: ")

def get_dns_records(domain, record_type):
    result = dns.resolver.resolve(domain, record_type)
    records = [record.to_text() for record in result]
    return records

# Usage
nameservers = get_dns_records(domain, 'NS')

if nameservers:
    print("The nameservers are:")
    for ns in nameservers:
        print(ns)
else:
    print(f"Cannot get nameservers for {domain}.")

a_records = get_dns_records(domain, 'A')

if a_records:
    print(f"A records:")
    for a_record in a_records:
        print(a_record)
else:
    print(f"Cannot get A records for {domain}.")
