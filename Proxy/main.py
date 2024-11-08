# Wczytaj listę proxy z pliku
with open("proxy_list.txt", "r") as file:
    lines = file.readlines()

# Przygotuj listy do przechowywania podzielonych proxy
http_proxies = []
socks4_proxies = []
socks5_proxies = []

# Przetwórz każdą linię, usuwając prefix i sortując proxy do odpowiednich list
for line in lines:
    line = line.strip()
    if line.startswith("http://"):
        http_proxies.append(line.replace("http://", ""))
    elif line.startswith("socks4://"):
        socks4_proxies.append(line.replace("socks4://", ""))
    elif line.startswith("socks5://"):
        socks5_proxies.append(line.replace("socks5://", ""))

# Zapisz podzielone proxy do plików
with open("http.txt", "w") as file:
    file.write("\n".join(http_proxies))

with open("socks4.txt", "w") as file:
    file.write("\n".join(socks4_proxies))

with open("socks5.txt", "w") as file:
    file.write("\n".join(socks5_proxies))

print("Proxy zostały podzielone na pliki: http.txt, socks4.txt, socks5.txt")
