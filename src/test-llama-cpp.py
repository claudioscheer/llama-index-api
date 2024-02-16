import os
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    completion_to_prompt,
    messages_to_prompt,
)

# model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q3_K_M.gguf"

llm = LlamaCPP(
    # model_url=model_url,
    # # optionally, you can set the path to a pre-downloaded model instead of model_url
    model_path=os.path.join(os.getcwd(), "models/llama-2-7b-chat.Q3_K_M.gguf"),
    temperature=0.1,
    max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=3900,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 0},
    # transform inputs into Llama2 format
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)

text = """
what is a queen?
"""

response = llm.complete(text)
print(response.text)

# response_iter = llm.stream_complete("Can you write me a poem about fast cars?")
# for response in response_iter:
#     print(response.delta, end="", flush=True)
