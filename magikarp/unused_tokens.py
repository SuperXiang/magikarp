import numpy as np

GEMMA_UNUSED_TOKENS = np.arange(7, 106)  # <|unused_token
COHERE_UNUSED_TOKENS = np.arange(255029, 256000)  # above tokenizer size

GPT2_UNUSED_TOKENS = np.arange(177, 188)  # unused 245-255 fallback
TIKTOKEN_UNUSED_TOKENS = GPT2_UNUSED_TOKENS
LLAMA2_UNUSED_TOKENS = np.arange(58, 130)  # duplicate single byte
MISTRAL_UNUSED_TOKENS = np.arange(14, 131)  # duplicate single byte ascii 0x0B to 0x7F

NEOX_UNUSED_TOKENS = np.arange(50277, 50432)  # unused above vocab size
OLMO_UNUSED_TOKENS = np.arange(50280, 50304)  # unused above vocab size
NEOX_UNUSED_TOKENS = [173]  # TODO: which one?

STARCODER2_UNUSED_TOKENS = [23519, 12740, 27012]  # found after using L2 norm
YI_UNUSED_TOKENS = np.arange(145, 305)  #  <|unused_token
JAMBA_UNUSED_TOKENS = np.arange(4, 515)  # <|maskxxx|>

DEEPSEEK_LANG_UNUSED_TOKENS = np.arange(100002, 100015)  # unused utf8
DEEPSEEK_CODE_UNUSED_TOKENS = np.arange(171, 173)  # f1/f2

# Defines reference unused tokens for models
# optional for most models, but also functions as a kind of registry of models to process
UNUSED_TOKENS = {
    ## required: cohere
    "CohereForAI/c4ai-command-r-v01": COHERE_UNUSED_TOKENS,
    "CohereForAI/c4ai-command-r-plus": COHERE_UNUSED_TOKENS,
    # required: gemma
    "google/gemma-7b": GEMMA_UNUSED_TOKENS,
    "google/gemma-2b": GEMMA_UNUSED_TOKENS,
    "google/codegemma-7b": GEMMA_UNUSED_TOKENS,
    # gpt2 variants
    "openai-community/gpt2": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-medium": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-large": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-xl": GPT2_UNUSED_TOKENS,
    "EleutherAI/gpt-j-6b": GPT2_UNUSED_TOKENS,
    "microsoft/phi-2": GPT2_UNUSED_TOKENS,
    # llama2 and variants
    "meta-llama/Llama-2-13b-hf": LLAMA2_UNUSED_TOKENS,
    "meta-llama/Llama-2-7b-hf": LLAMA2_UNUSED_TOKENS,
    "meta-llama/Llama-2-70b-hf": LLAMA2_UNUSED_TOKENS,
    "152334H/miqu-1-70b-sf": LLAMA2_UNUSED_TOKENS,
    "microsoft/Phi-3-mini-128k-instruct": LLAMA2_UNUSED_TOKENS,
    # neox and variants
    "EleutherAI/pythia-6.9b": NEOX_UNUSED_TOKENS,
    "EleutherAI/gpt-neox-20b": NEOX_UNUSED_TOKENS,
    "allenai/OLMo-7B-hf": OLMO_UNUSED_TOKENS,  # required since we use secondary metric
    "allenai/OLMo-1.7-7B-hf": OLMO_UNUSED_TOKENS,  # required since we use secondary metric
    #    "allenai/OLMo-1.7-7B": OLMO_UNUSED_TOKENS,# required since we use secondary metric
    # mistral variants
    "mistralai/Mistral-7B-v0.1": MISTRAL_UNUSED_TOKENS,
    "mistralai/Mistral-7B-Instruct-v0.2": MISTRAL_UNUSED_TOKENS,
    "mistralai/Mixtral-8x7B-v0.1": MISTRAL_UNUSED_TOKENS,
    "HuggingFaceH4/zephyr-7b-beta": MISTRAL_UNUSED_TOKENS,
    "Rakuten/RakutenAI-7B": MISTRAL_UNUSED_TOKENS,  # extended tokenizer, same unused
    "upstage/SOLAR-10.7B-v1.0": MISTRAL_UNUSED_TOKENS,
    "h2oai/h2o-danube2-1.8b-base": MISTRAL_UNUSED_TOKENS,
    "Nexusflow/Starling-LM-7B-beta": MISTRAL_UNUSED_TOKENS,
    "microsoft/WizardLM-2-7B": MISTRAL_UNUSED_TOKENS,
    # tiktoken
    "Qwen/Qwen1.5-MoE-A2.7B": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen1.5-72B-Chat": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen1.5-32B": TIKTOKEN_UNUSED_TOKENS,
    "stabilityai/stablelm-2-12b": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3-8B": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3-70B": TIKTOKEN_UNUSED_TOKENS,
    # others
    "bigcode/starcoder2-15b": STARCODER2_UNUSED_TOKENS,
    "01-ai/Yi-9B": YI_UNUSED_TOKENS,
    "ai21labs/Jamba-v0.1": JAMBA_UNUSED_TOKENS,
    "deepseek-ai/deepseek-llm-7b-base": DEEPSEEK_LANG_UNUSED_TOKENS,
    "deepseek-ai/deepseek-coder-33b-base": DEEPSEEK_CODE_UNUSED_TOKENS,
}
