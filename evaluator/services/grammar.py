import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def evaluate_grammar(text):
    matches = tool.check(text)

    score = max(0, 100 - (len(matches) * 5))

    feedback = [match.message for match in matches]

    return {
        'score': score,
        'feedback': feedback
    }