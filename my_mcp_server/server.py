from mcp.server.fastmcp.server import MCPServer 

server = MCPServer(name="MyMCPServer")

@server.tool
def query_model(prompt: str) -> str:
    return f'Received prompt: {prompt}'

server.run()
