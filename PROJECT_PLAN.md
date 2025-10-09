# AspenPlusMCP Project Plan

## Overview
Build an MCP (Model Context Protocol) server to enable AI assistants to interact with Aspen Plus chemical process simulations through a standardized interface.

## Project Scope

### Core Capabilities
1. **Process Simulation Control**
   - Open/close Aspen Plus simulation files (.bkp, .apw)
   - Run simulations and monitor execution status
   - Reinitialize and reset simulations

2. **Data Access & Manipulation**
   - Read stream properties (temperature, pressure, flow rates, compositions)
   - Read block/unit operation parameters
   - Modify input parameters and specifications
   - Access simulation results

3. **Analysis & Optimization**
   - Run sensitivity analyses
   - Perform parameter sweeps
   - Extract data for external optimization
   - Generate simulation reports

## Technical Architecture

### Technology Stack
- **Language**: Python (Windows-compatible for COM interface)
- **MCP SDK**: Python MCP SDK from Anthropic
- **Aspen Interface**: `win32com.client` (pywin32)
- **Transport**: stdio and HTTP with SSE support

### Project Structure
```
AspenPlusMCP/
├── src/
│   ├── aspenplus_mcp/
│   │   ├── __init__.py
│   │   ├── server.py          # Main MCP server
│   │   ├── aspen_wrapper.py   # COM interface wrapper
│   │   ├── tools.py           # MCP tool implementations
│   │   ├── resources.py       # MCP resource implementations
│   │   └── prompts.py         # MCP prompt templates
├── tests/
├── examples/
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

### MCP Components

**Tools** (executable functions):
- `run_simulation` - Execute Aspen Plus simulation
- `get_stream_data` - Retrieve stream properties
- `set_block_parameter` - Modify unit operation parameters
- `get_block_results` - Get unit operation results
- `export_results` - Export simulation data

**Resources** (data exposure):
- `simulation://status` - Current simulation state
- `simulation://streams` - All stream data
- `simulation://blocks` - All block/unit data
- `simulation://properties` - Physical properties

**Prompts** (templates):
- Optimize process parameters
- Troubleshoot convergence issues
- Generate process reports

## Implementation Phases

### Phase 1: Foundation
- Set up Python project with MCP SDK
- Implement basic Aspen Plus COM wrapper
- Create stdio transport MCP server

### Phase 2: Core Tools
- Implement file operations (open/close)
- Add simulation control (run/reset)
- Create basic data access tools

### Phase 3: Data Access
- Implement stream data retrieval
- Add block parameter access
- Create resource endpoints

### Phase 4: Advanced Features
- Add parameter modification capabilities
- Implement sensitivity analysis tools
- Create optimization helpers

### Phase 5: Production Ready
- Add HTTP/SSE transport support
- Implement comprehensive error handling
- Create documentation and examples
- Set up testing suite

## References

### MCP Resources
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-06-18)
- [MCP GitHub Organization](https://github.com/modelcontextprotocol)
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)

### Aspen Plus Automation
- [Aspen Plus Python Interface](https://github.com/YouMayCallMeJesus/AspenPlus-Python-Interface)
- [Aspen Plus Automation](https://github.com/zwang1995/Aspen-Plus-Automation)
- [ap-python package](https://github.com/bsha0/ap-python)
