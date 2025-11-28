Why is it better to have a LLMClient interface instead of calling HuggingFace/Ollama directly inside summarize_note?
- <b> clearn seperation of concern</b>
- it decouples the summarization pipeline from the specific LLM implementation
- summarize_note only knows llm has a .generate(prompt) method
- LlamaLLMClient, GPTLLMClient, OllamaLLMClient can be plugged in without touching the pipeline.
- Avoids importing heavy LLM libraries. 

What happens to your summarization pipeline if the LLM changes from GPT → Llama → some other model?
- It dosent affect the pipeline. Except We will be using different class for different LLM models and plug it in the pipeline.
- Abstraction

Why do we limit max_chunks? What happens if you pass all chunks from a huge PDF directly?
- Every LLM has a context/ token limit. Passing too many chunks will exceed it leading to failure or truncation
- More chunks = more noise -> summary quality drops
- More chunks = more latency + more cost (for API LLM)
