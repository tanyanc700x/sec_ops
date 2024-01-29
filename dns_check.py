import dns.resolver

def get_dns_records(domain, record_type):
    result = dns.resolver.resolve(domain, record_type)
    records = [record.to_text() for record in result]
    return records

# Usage
domain = input("Add your domain name: ")

record_types = ['NS', 'A', 'MX']

for record_type in record_types:
    records = get_dns_records(domain, record_type)

    if records:
        print(f"{record_type} records:")
        for record in records:
            print(record)
        print()  # Add an empty line between record types
    else:
        print(f"Cannot get {record_type} records for {domain}.")

