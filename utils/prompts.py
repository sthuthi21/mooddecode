def mood_prompt(text):
    return f"Analyze the following text and identify the predominant emotion conveyed in a single word.Focus on the emotional tone, context, and any explicit or implicit cues within the text.Provide the emotion as a single word without any additional explanations or context.\n\n'{text}'"

def crisis_prompt(text):
    return f"Analyze the following sentence for indicators of a mental health crisis or self-harm risk.Provide a binary response: 'true' if the sentence suggests a potential crisis or risk, and 'false' if it does not.\n\n'{text}'"

def summarize_prompt(text):
    return (
        "Summarize the following paragraph in one simple sentence. "
        "Be concise and only include the main idea, avoiding opinions or extra interpretation:\n\n"
        f"{text}"
    )

