import requests

class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def list_tools(self):
        response = requests.get(f"{self.server_url}/tools")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to list tools: {response.status_code}")

    def call_tool(self, tool_name, input_data):
        response = requests.post(f"{self.server_url}/tools/{tool_name}", json=input_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to call tool {tool_name}: {response.status_code}")

# 使用示例
if __name__ == "__main__":
    client = MCPClient("http://localhost:8200")

    try:
        # 列出可用工具
        tools = client.list_tools()
        print("Available tools:", tools)

        # 使用 readFile 工具
        tool_name = "readFile"
        input_data = {"filePath": "./example.txt"}

        result = client.call_tool(tool_name, input_data)
        print("Result:", result["content"])
    except Exception as e:
        print("Error:", str(e))