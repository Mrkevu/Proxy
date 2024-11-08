with open("proxy_list.txt", "r") as file:
    lines = file.readlines()

http_proxies = []
socks4_proxies = []
socks5_proxies = []

for line in lines:
    line = line.strip()
    if line.startswith("http://"):
        http_proxies.append(line.replace("http://", ""))
    elif line.startswith("socks4://"):
        socks4_proxies.append(line.replace("socks4://", ""))
    elif line.startswith("socks5://"):
        socks5_proxies.append(line.replace("socks5://", ""))

with open("http.txt", "w") as file:
    file.write("\n".join(http_proxies))

with open("socks4.txt", "w") as file:
    file.write("\n".join(socks4_proxies))

with open("socks5.txt", "w") as file:
    file.write("\n".join(socks5_proxies))

print("Proxy teraz są oddzielone do http/socks4/socks5.txt")
