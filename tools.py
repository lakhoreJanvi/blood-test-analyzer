## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
from crewai_tools import SerperDevTool

from pydantic import BaseModel, Field

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
@tool("Reads and parses a blood test report")
async def read_data_tool(self, path: str = 'data/sample.pdf') -> str:
    """Tool to read data from a pdf file from a path

    Args:
        path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

    Returns:
        str: Full Blood Test report file
    """

    docs = PyPDFLoader(file_path=path).load()

    full_report = ""
    for data in docs:
        # Clean up extra whitespaces and format
        content = data.page_content

        # Remove extra whitespaces and format properly
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")

        full_report += content + "\n"

    return full_report

## Creating Nutrition Analysis Tool
@tool("Analyzes blood report data to provide nutrition insights.")
async def analyze_nutrition_tool(self, blood_report_data: str) -> str:
    """
    A class that contains the logic for analyzing nutrition based on blood report data.
    """
    # Process and analyze the blood report data
    processed_data = blood_report_data

    # Clean up the data format (example, replace with actual logic)
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":  # Remove double spaces
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
    # TODO: Implement actual nutrition analysis logic here
    return "Nutrition analysis functionality to be implemented"

@tool("exercise planner")
async def create_exercise_plan_tool(self, blood_report_data: str) -> str:
    """
    A class that contains the logic for creating exercise plans.
    """
    # TODO: Implement actual exercise planning logic here
    return "Exercise planning functionality to be implemented"