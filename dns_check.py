import dns.resolver

# Getting a domain from outside
domain = input("Add your domain name: ")

def get_nameservers(domain):
    result = dns.resolver.resolve(domain, 'NS')
    nameservers = [ns.to_text() for ns in result]
    return nameservers


def get_a_records(domain):
    result = dns.resolver.resolve(domain, 'A')
    a_records = [record.to_text() for record in result]
    return a_records
   #Usage
nameservers = get_nameservers(domain)

if nameservers:
    print("The nameservers are:")
    for ns in nameservers:
        print(ns)
else:
    print(f"Cannot get nameservers for {domain}.")

a_records = get_a_records(domain)

if a_records:
    print(f"A record:")
    for a_record in a_records:
        print(a_record)
else:
    print(f"Cannot get A record for {domain}.")


