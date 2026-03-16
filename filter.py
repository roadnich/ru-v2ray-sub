Python
import requests, base64, json

url = "https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.1.txt"

data = requests.get(url).text.strip()
decoded = base64.b64decode(data).decode().splitlines()

ru_nodes = []

for node in decoded:
    try:
        if node.startswith("vmess://"):
            j = json.loads(base64.b64decode(node[8:] + "==").decode())
            name = j.get("ps","").lower()
            if "ru" in name or "russia" in name or "moscow" in name:
                ru_nodes.append(node)
        elif "ru" in node.lower():
            ru_nodes.append(node)
    except:
        pass

result = base64.b64encode("\n".join(ru_nodes).encode()).decode()
open("ru.txt","w").write(result)
