from typing import Dict, List, Any
import re
import logging
from format_topics_json import load_json_data, save_json_data

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def escape_text(text: str) -> str:
    return text


def format_topics_json(topics: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for topic in topics:
        for exercise in topic.get("exercises", []):
            try:
                # Format the exercise content using the LLM
                formatted_content = escape_text(exercise["content"])
                formatted_solution = escape_text(exercise["solution"]) if exercise["solution"] is not None else None
                exercise["content"] = formatted_content
                exercise["solution"] = formatted_solution
            except Exception as e:
                logging.error(f"Error formatting exercise content: {e}")
    return topics


def main() -> None:
    """
    Main function to execute the extraction and save to JSON.
    """
    # Path to the JSON file
    json_file_path = "topics.json"
    output_path = "topics1.json"

    try:
        # Load data from JSON
        data = load_json_data(json_file_path)

        # Format the data into topics
        topics = format_topics_json(data)

        # Save the formatted data to a new JSON file
        save_json_data(output_path, topics)

        logging.info(f"Topics JSON file created successfully at {output_path}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
