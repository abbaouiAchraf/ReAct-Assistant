# AI Agent for Windows Systems: An Implementation of the ReAct Framework

This project is an AI agent designed to assist users in performing various tasks on Windows systems, inspired by the _REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS_ paper. The agent is capable of extracting information from data, executing actions on the operating system, and responding to user queries, providing a seamless and intelligent user experience.

## Features

- Task execution on Windows systems
- Data extraction and manipulation
- Natural language processing and understanding
- Interactive user interface for querying and task submission (in development)

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/abbaouiAchraf/ai-agent.git
   cd ai-agent
   ```

2. **Create a Virtual Environment:**
   ```
   python -m venv env
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source env/bin/activate
     ```

4. **Install Requirements:**
   ```
   pip install -r requirements.txt
   ```

5. **Create `.env` File:**
   - Copy the `.env.example` file to create a new `.env` file.
   - Provide your OpenAI API key in the `.env` file.

6. **Update CSV Data:** (Optional)
   - Navigate to the `data/` directory.
   - Update the CSV files with the relevant data as needed.

7. **Run the Project:**
   ```
   python main.py
   ```

8. **Interact with the AI Agent:**
   - Use the provided user interface to submit tasks or ask questions.

## Usage

Here are some examples of how to interact with the AI agent:

- Extract the top countries based on population:
  ```
  Extract the top 5 countries with the highest population from the data and save them as a note in the log file.
  ```

- Perform a Windows system task:
  ```
  Open File Explorer and navigate to the C:\Users\%username%\Documents directory.
  ```

- Query the AI agent:
  ```
  What is the current date?
  ```

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was inspired by the ReAct paper and utilizes the OpenAI API for natural language processing tasks. Special thanks to the authors of the ReAct paper and the developers of the OpenAI platform.

## Plannings

I am planning to add quantized open-source llm (maybe fine tuning it using qLora techniques to achieve better results) that can run on cpu instead of openAI models