# Read the JSON that VS Code sends to the hook
$inputJson = [Console]::In.ReadToEnd()

# Get the tool name from the JSON, if available
$tool = ""
try { $tool = ($inputJson | ConvertFrom-Json).tool_name } catch {}

# Get the current time in ISO 8601 format
$ts = (Get-Date).ToString('o')

# Append a line to hook.log in the same folder as this script
Add-Content -Path (Join-Path $PSScriptRoot 'hook.log') -Value "[$ts] PostToolUse fired: $tool"