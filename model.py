from ctransformers import AutoModelForCausalLM, AutoConfig, Config

"""
Download:`TheBloke/Mistral-7B-Instruct-v0.1-GGUF` 
Put it into: `models/mistral-7b-instruct-v0.1.Q4_K_M.gguf`
"""


def mistral_llm():
    return AutoModelForCausalLM.from_pretrained(
        "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        model_type="mistral",
        config=AutoConfig(
            Config(
                temperature=0.01,
                repetition_penalty=1.1,
                batch_size=52,
                max_new_tokens=1024,
                context_length=2048
            )
        )
    )


model = mistral_llm()

while (query := input('Query: ')) != 'q':
    print(
        'Mistral: ',
        model(
            f"<s>[INST] {query} [/INST]"
        )
    )
