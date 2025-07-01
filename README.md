# Project Setup and Execution Guide

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code and understand the expected behavior.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.

---

# 🐛 Bugs (Problem) and Solution
**Problem**: During the setup of this project, I encounterd version incompatibility errors when running ```pip install -r requirements.txt``` due to conflicting dependencies between various libraries.

**Solution**: 
- Removed Version Pins for Google Cloud Libraries: All google-* packages are unversioned, allowing pip to resolve the most compatible set of versions, especially to accommodate ```protobuf>=5.x```.

- OpenTelemetry Dependencies: Rather than pinning each exporter/instrumentation package, only ```opentelemetry-api>=1.30.0``` is versioned explicitly (to satisfy CrewAI requirements).

**Problem**: Tools were being passed to Task definitions as Python classes (e.g., BloodTestReportTool) instead of instantiated objects or top-level functions decorated with @tool.

**Solution**: 
- Refactored tools in tools.py: Converted the tool logic from methods within classes to top-level asynchronous - - functions, each decorated with ```@tool```.

- Updated task.py imports and tool lists: Changed Task definitions to import and use the new top-level tool functions.

**Problem**: The FastAPI application (served by Uvicorn) was configured to handle form data (likely for file uploads), but the ```python-multipart``` library, which is required for this functionality, was missing.

**Solution**: Installed ```python-multipart``` and added in ```requirements.txt```.

**Problem**: ```llm = llm``` This line was a placeholder and did not actually initialize an LLM instance. It would lead to a NameError or UnboundLocalError when llm was later used by agents.

**Solution**: Creating a llm object to resolve the error.

**Problem**: Missing LLM Import.

**Solution**: The ```crewai.LLM``` class, essential for defining the LLM to be used by agents, was not imported.

**Problem**: Incorrect Tool Instantiation and Method Access ```BloodTestReportTool().read_data_tool```.

**Solution**: Direct Reference to ```@tool``` Decorated Function ```read_data_tool```.

**Problem**: Missing Docstring, While Python functions don't strictly require docstrings to run, CrewAI's ```@tool``` decorator and underlying frameworks like LangChain heavily rely on them. 

**Solution**: Added docstrings for ```analyze_nutrition_tool``` and ```create_exercise_plan_tool``` functions.

---

# 🚀 Setup Instructions

1. Clone the Repository : git clone https://github.com/lakhoreJanvi/blood-test-analyzer.git
2. Create a virtual environment named venv : python3 -m venv venv
3. Activate the virtual environment : source venv/bin/activate
4. Install all required Python packages using the requirements.txt file : pip install -r requirements.txt
5. Configure API Keys: The project requires API keys for OpenRouter (for LLM access) and Serper (for web search).
- Create a .env file in the root directory of your project.
- OpenRouter API Key: Sign up at https://openrouter.ai/ and generate an API key.
6. Add Keys to .env : OPENROUTER_API_KEY="sk-or-v1-YOUR_OPENROUTER_API_KEY_HERE"

## 🚀 Running the Application

1. Ensure your virtual environment is active.
2. Start the Uvicorn server : python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 🧪 Usage Instructions
- Once the Uvicorn server is running, you can interact with the API. The primary endpoint for blood report analysis is '/analyze'.
- You will need to send a POST request to this endpoint, including a PDF file of a blood test report.

---

# 📄 API Documentation

## 🌐 Base URL

The API is designed to be hosted locally.
Local Base URL: http://0.0.0.0:8000/

## 🔐 Authentication

Authentication for this API is handled internally by the application using API keys loaded from environment variables. 
Ensure the following environment variables are set in your project's ```.env``` file and ```OPENROUTER_API_KEY``` Your API key for accessing LLMs via OpenRouter.

## Endpoints

1. GET / (Root Endpoint) : This endpoint serves as a simple health check to confirm that the API is running and accessible.
- Method: GET
- URL: /
- Description : A basic endpoint to verify the API's operational status. It returns a simple message indicating that the service is running.
- Request Body : nothing
- Responses : 200 OK - Successful Response
message (string): A confirmation message indicating the API is active.

2. POST /analyze : This is the primary endpoint for submitting a blood test report and a user query to the AI doctor crew for analysis.
- Method : POST
- URL: /analyze
- Description : Receives a user's natural language query and a PDF file containing a blood test report. The AI agent crew (consisting of an eccentric doctor, a lenient verifier, a sales-oriented nutritionist, and an extreme fitness coach) will then process this input to generate a detailed response.
- Request Body: multipart/form-data
1. query (string, required): A natural language query from the user (e.g., "Analyze this blood report for general health and provide nutrition and exercise recommendations.").
2. pdf_file (file, required): The blood test report in PDF format
- Responses : 200 OK - Successful Response
message (string): A confirmation message.