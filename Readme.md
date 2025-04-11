# Browser Use

A Python project that uses the [browser-use](https://github.com/browser-use/browser-use) library to automate web browser tasks.

## Prerequisites

- Python 3.x installed on your system
- Git for cloning the repository
- Google AI Studio API key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd browserUse
   ```

2. Create a virtual environment:

   ```bash
   python -m venv myenv
   ```

3. Activate the virtual environment:

   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source myenv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Install Chromium for Playwright:

   ```bash
   playwright install chromium
   ```

6. Set up environment variables:
   - Copy `.env-sample` to `.env`
   - Replace `your-api-key` in `.env` with your Google AI Studio API key

## Usage

1. First, activate the virtual environment:

   ```bash
   myenv\Scripts\activate
   ```

2. Then run the main script:

   ```bash
   python main.py
   ```

## Dependencies

- langchain-google-genai - For Google AI integration
- browser-use - For browser automation
- python-dotenv - For environment variable management
- pydantic - For data validation

## Troubleshooting

- If you encounter issues with the virtual environment, make sure it's properly activated
- Verify that your API key is correctly set in the `.env` file
- Ensure all dependencies are installed by running `pip install -r requirements.txt`
