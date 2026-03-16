import requests
import base64
import json

url = "https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.1.txt"

r = requests.get(url)
data = r.text.strip()

decoded = base64.b64decode(data + "==").decode(errors="ignore").splitlines()

ru_nodes = []

for node in decoded:
    try:
        if node.startswith("vmess://"):
            raw = node.replace("vmess://", "")
            j = json.loads(base64.b64decode(raw + "==").decode())
            name = j.get("ps", "").lower()

            if "ru" in name or "russia" in name or "moscow" in name:
                ru_nodes.append(node)

        elif "ru" in node.lower():
            ru_nodes.append(node)
    except:
        pass

result = base64.b64encode("\n".join(ru_nodes).encode()).decode()

with open("ru.txt", "w") as f:
    f.write(result)
