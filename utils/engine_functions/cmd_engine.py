from llama_index.legacy.tools import FunctionTool
import subprocess


def run_command(command: str) -> str:
    try:
        output = subprocess.check_output(command, shell=True)
        return f'command has been run successfully, output: {output}'
    except Exception as e:
        print(f'CMD error: {e}')
        return f'command faced an error {e}'


cmd_engine = FunctionTool.from_defaults(
    fn=run_command,
    name="command_running",
    description="""this tool can run command on the shell of the windows operation system so you can do various 
    operations mainly WINDOWS""",
)