from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp")

@mcp.tool()
def ping() -> str:
    """Returns 'pong'."""
    return "pong"

if __name__ == "__main__":
    mcp.run(transport="stdio")
