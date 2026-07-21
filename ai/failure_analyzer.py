import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


FAILURE_ANALYSIS_PROMPT = """
You are a senior QA Automation Engineer.

Analyze this pytest failure.

Provide:

1. Failed test summary
2. Root cause analysis
3. Possible fixes
4. Recommended next debugging steps

Consider possible causes:
- Automation framework issue
- Locator issue
- Timing/wait issue
- Test data issue
- Environment issue
- Application regression

Do not assume the test is wrong. Analyze the evidence.

Test output:

"""


def analyze_failure(test_output: str):

    response = client.responses.create(
        model="gpt-5-mini",
        input=FAILURE_ANALYSIS_PROMPT + test_output
    )

    return response.output_text