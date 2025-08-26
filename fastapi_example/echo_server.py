from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="EchoServer", stateless_http=True)


@mcp.tool()
def echo(message: str) -> str:
    """
    Use this tool for echoing back a message.

    Args:
        message: The message to echo back.

    Returns:
        The echoed message with "Echo: " prefix.
    """
    return f"Echo: {message}"
