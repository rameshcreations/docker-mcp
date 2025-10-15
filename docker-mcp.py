import docker
from mcp.server.fastmcp import FastMCP

client = docker.from_env()
mcp = FastMCP("docker-server")

#TOOLS

@mcp.tool()
def get_logs(container_id: str, tail: int = 20) -> str:
    """Get last N lines of logs from a container"""
    try:
        container = client.containers.get(container_id)
        logs = container.logs(tail=tail).decode("utf-8")
        return logs if logs else "No logs available."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def start_container(container_id: str) -> str:
    """Start a stopped container."""
    try:
        container = client.containers.get(container_id)
        container.start()
        return f"Container {container.name} started"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def stop_container(container_id: str) -> str:
    """Stop a running container"""
    try:
        container = client.containers.get(container_id)
        container.stop()
        return f"Container {container.name} stopped"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def restart_container(container_id: str) -> str:
    """Restart a container"""
    try:
        container = client.containers.get(container_id)
        container.restart()
        return f"Container {container.name} restarted"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def container_stats(container_id: str) -> str:
    """Get CPU and memory usage of a container"""
    try:
        container = client.containers.get(container_id)
        stats = container.stats(stream=False)
        cpu = stats["cpu_stats"]["cpu_usage"]["total_usage"]
        mem = stats["memory_stats"]["usage"]
        return f"CPU Usage: {cpu}, Memory Usage: {mem} bytes"
    except Exception as e:
        return f"Error: {str(e)}"
    
@mcp.tool()
def list_containers() -> str:
    """List all Docker containers with ID, name, and status"""
    containers = client.containers.list(all=True)
    if not containers:
        return "No containers found."
    return "\n".join(f"{c.short_id} | {c.name} | {c.status}" for c in containers)

@mcp.tool()
def run_container(image_name: str, name: str = None, ports: dict = None, detach: bool = True) -> str:
    """
    Run a new Docker container.

    Args:
        image_name (str): Name of the Docker image to run.
        name (str, optional): Name of the container.
        ports (dict, optional): Port mappings, e.g., {"80/tcp": 8080}.
        detach (bool, optional): Run container in detached mode. Default is True.

    Returns:
        str: Container ID or error message.
    """
    try:
        container = client.containers.run(
            image=image_name,
            name=name,
            ports=ports,
            detach=detach
        )
        return f"Container {container.name} started with ID: {container.short_id}"
    except Exception as e:
        return f"Error running container: {str(e)}"

@mcp.tool()
def delete_container(container_id: str, force: bool = False) -> str:
    """
    Delete (remove) a Docker container.

    Args:
        container_id (str): The container ID or name.
        force (bool, optional): Force remove even if running. Default False.

    Returns:
        str: Success or error message.
    """
    try:
        container = client.containers.get(container_id)
        container.remove(force=force)
        return f"Container {container.name} removed successfully."
    except docker.errors.NotFound:
        return f"Container '{container_id}' not found."
    except docker.errors.APIError as e:
        return f"Docker API error: {str(e)}"
    except Exception as e:
        return f"Error removing container: {str(e)}"

# MAIN

if __name__ == "__main__":
    print("🚀 Docker MCP Server running...")
    mcp.run()
