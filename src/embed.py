from llama_index.embeddings import resolve_embed_model
from llama_index.embeddings.base import Embedding

embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")


def get_text_embeddings(text: list[str]) -> list[Embedding]:
    return embed_model.get_text_embedding_batch(text)


def get_text_embedding(text: str) -> Embedding:
    return embed_model.get_text_embedding(text)
