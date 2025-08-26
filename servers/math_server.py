from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MathServer", stateless_http=True)


@mcp.tool()
def add_two(a: int, b: int) -> int:
    """
    Use this tool for adding two integers together.

    Args:
        a: The first integer to add.
        b: The second integer to add.

    Returns:
        The sum of the two integers.
    """
    return a + b
