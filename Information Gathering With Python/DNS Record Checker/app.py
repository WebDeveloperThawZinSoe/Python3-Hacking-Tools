import dns
import dns.resolver

name = input("Enter Domain : ")

print("Choose Query Type ")
print("[1] A Record")
print("[2] AAAA Record")
print("[3] MX Record")
print("[4] NS Record")
print("[5] TXT Record")
print("[6] SOA Record")
print("[7] All Record")

option = input("Input : ")

if option == "1":
    option = a = dns.resolver.query(name,'A')
    print(a.rrset)

if option == "2":
    option = aaaa = dns.resolver.query(name,'AAAA')
    print(aaaa.rrset)

if option == "3":
    option = mx = dns.resolver.query(name,'MX')
    print(mx.rrset)

if option == "4":
    option = ns = dns.resolver.query(name,'NS')
    print(ns.rrset)

if option == "5":
    option = txt = dns.resolver.query(name,'TXT')
    print(txt.rrset)

if option == "6":
    option = soa = dns.resolver.query(name,'SOA')
    print(soa.rrset)

if option == "7":
    for qtype in 'A','AAAA','MX','NS','TXT','SOA':
        answer = dns.resolver.query(name,qtype,raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)