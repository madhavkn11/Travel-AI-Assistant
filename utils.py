import os


def save_markdown(content):

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/travel_guide.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)