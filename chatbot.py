def generate_response(prediction, explanation):
    label = "Fake" if prediction == 1 else "Real"

    words = [word for word, weight in explanation[:3]]

    response = f"This article is likely {label}.\n\n"

    if label == "Fake":
        response += "The model detected patterns often associated with misleading or sensational content. "
    else:
        response += "The content appears consistent with factual and reliable reporting. "

    response += "\n\nKey influencing terms: " + ", ".join(words)

    return response