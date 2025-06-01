import requests

# JSON-andmete URL
url = "https://metshein.com/kordamine/json/kasutajad.json"  # <-- veebilehe url

# Loeme JSON-andmed otse veebist
response = requests.get(url)
andmed = response.json()

# Võtame kasutajate nimekirja
kasutajad = andmed["kasutajad"]

# Kuvame kõik kasutajanimed
print("Kasutajanimed:")
for kasutaja in kasutajad:
    print(kasutaja["kasutajanimi"])

# Kuvame kasutajate koguarvu
print("Kokku kasutajaid:", len(kasutajad))

# Kuvame ainult peatatud kasutajad
print("Peatatud kasutajad:")
for kasutaja in kasutajad:
    if kasutaja["staatus"] == "peatatud":
        print(kasutaja["nimi"])
