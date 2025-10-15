# 🐳 Docker MCP Server

This project implements a **Model Context Protocol (MCP)** server that exposes Docker management capabilities as MCP tools.  
You can connect it to **Amazon Q**, **Claude Desktop**, or any other MCP-compatible client.

---

## 🚀 Features

| Tool Name           | Description |
|----------------------|-------------|
| `list_containers`    | Lists all running and stopped containers |
| `start_container`    | Starts a stopped container |
| `stop_container`     | Stops a running container |
| `restart_container`  | Restarts a container |
| `get_logs`           | Fetches logs from a container |
| `container_stats`    | Displays CPU, memory, and network stats |
| `run_container`      | Runs a new container from an image (with optional ports) |
| `delete_container`   | Deletes (removes) a container, with optional `force` flag |

---

## 🧰 Prerequisites

- **Python 3.10+**
- **Docker Engine** installed and running
- **Amazon Q** desktop app (or another MCP client)
---

## ⚙️ Installation

```bash
# Clone the repository into ~/mcp (replace <repo_url>)
git clone <repo_url> ~/mcp && cd ~/mcp

# Create Project Folder (if you are not cloning)
mkdir -p ~/mcp && cd ~/mcp

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
---
## 🧠 Adding the Docker MCP Server to Your Client
Add the following configuration to your client’s MCP configuration file 
```json
{
  "mcpServers": {
    "docker-mcp": {
      "command": "mcp/venv/bin/python",
      "args": ["mcp/docker-mcp.py"]
    }
  }
}
```
---
## 👨‍💻 Author

**Ramesh Indrajith Kumar**  
🌍 [rameshindrajith.com](http://rameshindrajith.com)  
📧 me@rameshindrajith.com  