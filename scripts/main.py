from extract_exercises_from_tex import extract_exercises_from_tex
from format_latex_content import get_llm, format_latex_content, save_json_data
from format_topics_json import format_topics_json


def main() -> None:
    """
    Main function to execute the extraction and save to JSON.
    """
    tex_file_path = "../src/exercises.tex"
    output_path = "topics.json"

    # Initialize Gemini LLM
    llm = get_llm()

    # Extract exercises from the .tex file
    exercises = extract_exercises_from_tex(tex_file_path)

    data = {"exercises": exercises}

    # Format the data into topics
    topics = format_topics_json(data)

    # Format the latex content into user-friendly text
    formatted_topics = format_latex_content(topics, llm)

    # Save the formatted data to a new JSON file
    save_json_data(output_path, formatted_topics)


if __name__ == "__main__":
    main()
