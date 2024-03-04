from llama_index.legacy.tools import FunctionTool
import os


def save_log(note: str) -> str:
    try:
        note_file = os.path.join("outputs", "notes.txt")
        if not os.path.exists(note_file):
            open(note_file, "w")

        with open(note_file, "a") as f:
            f.writelines([note + "\n"])
        return "note saved"
    except Exception as e:
        print(f"note not saved, error: \n{e}")
        return "note not saved"


log_engine = FunctionTool.from_defaults(
    fn=save_log,
    name="log_saving_functionality",
    description="this tool can save a a provided string note into a log file for the user",
)
