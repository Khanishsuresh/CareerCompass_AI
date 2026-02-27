import re

def parse_score(response_text):
    """
    Parses a match score from a given response text.
    """
    match = re.search(r"Match Score:\s*(\d+)(?:/\d+)?", response_text)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            pass
    return 0