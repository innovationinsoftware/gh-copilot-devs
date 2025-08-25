// client.mjs (ESM, Node 18+)
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["./server.mjs"], // adjust if your server is elsewhere
});

const client = new Client({ name: "tester", version: "1.0.0" });
await client.connect(transport);

const { tools } = await client.listTools();
console.error("TOOLS:", tools.map(t => t.name));

const result = await client.callTool({ name: "ping", arguments: {} });
console.error("RESULT:", JSON.stringify(result, null, 2));

process.exit(0);
