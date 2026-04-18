from obsidianize.config import Config


def summarize(content: str, file_path: str, config: Config) -> str:
    prompt = config.summary_prompt_template.format(
        file_path=file_path,
        content=content,
    )
    if config.llm_provider == "gemini":
        return _gemini(prompt, config)
    elif config.llm_provider == "ollama":
        return _ollama(prompt, config)
    elif config.llm_provider == "openai":
        return _openai(prompt, config)
    else:
        raise ValueError(f"Unknown LLM provider: {config.llm_provider!r}")


def _gemini(prompt: str, config: Config) -> str:
    import google.generativeai as genai  # type: ignore[import-untyped]

    genai.configure(api_key=config.llm_api_key)
    model = genai.GenerativeModel(config.llm_model)
    response = model.generate_content(prompt)
    return response.text


def _ollama(prompt: str, config: Config) -> str:
    import ollama as ol  # type: ignore[import-untyped]

    client = ol.Client(host=config.ollama_base_url)
    response = client.chat(
        model=config.ollama_model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.message.content


def _openai(prompt: str, config: Config) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=config.llm_api_key)
    response = client.chat.completions.create(
        model=config.llm_model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""
