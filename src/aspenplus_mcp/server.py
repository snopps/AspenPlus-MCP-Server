"""Main MCP server implementation for Aspen Plus."""

import asyncio
import logging
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server

from .aspen_wrapper import AspenPlusWrapper
from .tools import register_tools
from .resources import register_resources

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Run the Aspen Plus MCP server."""
    server = Server("aspenplus-mcp")

    # Initialize Aspen Plus wrapper
    aspen = AspenPlusWrapper()

    # Register tools and resources
    register_tools(server, aspen)
    register_resources(server, aspen)

    logger.info("Starting Aspen Plus MCP server")

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
