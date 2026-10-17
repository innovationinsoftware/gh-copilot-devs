def normalize_text(text: str) -> str:
	"""Normalize text by trimming and collapsing internal whitespace to single spaces."""
	if text is None:
		return ""

	return " ".join(str(text).strip().split()).lower()


def normalize_username(name: str) -> str:
	"""Backward-compatible wrapper for username normalization."""
	return normalize_text(name)