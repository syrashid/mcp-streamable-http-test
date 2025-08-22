import asyncio
import os
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

# Initialize FastMCP server
# stateless_http=True is a ok as long as we don't care about preserving state
# https://github.com/modelcontextprotocol/python-sdk/issues/808

PORT = os.environ.get("PORT", 10000)
mcp = FastMCP(name="physrisk", stateless_http=True)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool()
async def get_physrisk_hazards(query: str) -> str:
    """
    Use this tool for getting the hazards.

    Args:
        query: The query to get the hazards.

    Returns:
        A string of the hazards.

    """
    return f"RENDER ERVER -> Your hazard was: {query}"


@mcp.tool()
async def get_asset_vulnerability(query: str) -> str:
    """
    Use this tool for getting the asset vulnerability.

    Args:
        query: The query to get the asset vulnerability.

    Returns:
        A string of the asset vulnerability.
    """
    return f"RENDER SERVER ->Your asset vulnerability was: {query}"


@mcp.tool()
async def get_asset_risk(query: str) -> str:
    """
    Use this tool for getting the asset risk.

    Args:
        query: The query to get the asset risk.

    Returns:
        A string of the asset risk.
    """
    return f"RENDER SERVER ->Your asset risk was: {query}"


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=PORT, path="/mcp")
