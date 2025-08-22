import re

def parse_score(response_text):
    """
    Parses a match score from a given response text.
    """
    match = re.search(r'.*Match Score:.*(\d+)/\d+', response_text)
    print(match)
    if match:
        return int(match.group(1))
    return 0