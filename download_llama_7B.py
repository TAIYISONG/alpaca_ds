# Running "pip install -r requirements.txt"
# Using LlamaForCausalLM is assuming that you are using latest transformers built from https://github.com/huggingface/transformers.git, which is defined in requirements.txt.
from transformers import LlamaForCausalLM, LlamaTokenizer 

#########################################
# Please specify your own saving dir ####
SAVE_PATH_LLAMA_MODEL = "."          ####
#########################################

tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-7b-hf")
model = LlamaForCausalLM.from_pretrained("decapoda-research/llama-7b-hf")


tokenizer.save_pretrained(SAVE_PATH_LLAMA_MODEL)
model.save_pretrained(SAVE_PATH_LLAMA_MODEL)