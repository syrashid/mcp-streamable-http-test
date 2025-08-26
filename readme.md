# MCP Servers over Streamable HTTP

This repository demonstrates how to build and run **MCP (Model Context Protocol) servers** using Python, `mcp`, and `FastAPI` with streamable HTTP transport.

## What's Included

- **Echo Server** - Simple echo tool that returns messages
- **Math Server** - Basic math operations (addition)
- **PhysRisk Server** - Climate risk assessment tools
- **Combined FastAPI App** - Mounts all three servers

## Quick Start

1. **Install dependencies**
```bash
uv venv && source .venv/bin/activate
uv pip install -r pyproject.toml
```

2. **Run the combined server**
```bash
uv run servers/server.py
```

This starts a FastAPI app with three MCP servers mounted at:
- `http://localhost:10000/echo/mcp/`
- `http://localhost:10000/math/mcp/`
- `http://localhost:10000/physrisk/mcp/`

## Project Structure

```
.
├── servers/
│   ├── echo_server.py      # Echo tool server
│   ├── math_server.py      # Math operations server
│   ├── physrisk_server.py  # Climate risk tools server
│   └── server.py           # Combined FastAPI app
├── pyproject.toml          # Dependencies
└── readme.md               # This file
```
