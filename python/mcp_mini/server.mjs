// server.mjs
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({ name: "hello-mcp", version: "1.0.1" });

server.registerTool(
  "ping",
  {
    title: "Ping",
    description: "Returns pong.",
    // Minimal JSON Schema: no inputs
    inputSchema: { type: "object", properties: {}, additionalProperties: false }
  },
  async () => ({ content: [{ type: "text", text: "pong" }] })
);

await server.connect(new StdioServerTransport());
