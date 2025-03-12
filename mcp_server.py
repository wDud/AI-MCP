from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class ToolInput(BaseModel):
    filePath: str

# 定义工具列表
tools = {
    "readFile": {
        "description": "Read the content of a file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filePath": {
                    "type": "string",
                    "description": "The path to the file to read.",
                },
            },
            "required": ["filePath"],
        },
    }
}

@app.get("/tools")
async def list_tools():
    return tools

@app.post("/tools/readFile")
async def read_file(input: ToolInput):
    file_path = input.filePath
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return {
            "content": f"The content of {file_path} is:\n{content}",
            "isError": False
        }
    except Exception as e:
        return {
            "content": f"Error reading file {file_path}: {str(e)}",
            "isError": True
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8200)