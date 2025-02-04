import json
from typing import Dict, List, Any

# Mapping of categories to their titles and descriptions
CATEGORY_MAPPING = {
    "expressions": {"title": "Operaciones básicas", "description": "Operaciones básicas"},
    "conditionals": {"title": "Condicionales", "description": "Condicionales"},
    "methods": {"title": "Métodos", "description": "Métodos"},
    "loops": {"title": "Ciclos", "description": "Ciclos"},
    "arrays1": {"title": "Arrays1", "description": "Arrays1"},
    "arrays2": {"title": "Arrays2", "description": "Arrays2"}
}


def format_topics_json(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Formats the input JSON data into a structured list of topics with exercises.

    Args:
        data (Dict[str, Any]): The input JSON data containing exercises.

    Returns:
        List[Dict[str, Any]]: A list of topics, each containing related exercises.
    """
    # Cache for topics to avoid duplicates
    topics: Dict[str, Dict[str, Any]] = {}

    exercises = data.get("exercises", [])

    for exercise_data in exercises:
        topic = exercise_data["topic"]
        if topic not in topics:
            # Create a new topic if it doesn't exist
            topics[topic] = {
                "title": CATEGORY_MAPPING[topic]["title"],
                "description": CATEGORY_MAPPING[topic]["description"],
                "exercises": []
            }

        # Append the exercise to the corresponding topic
        topics[topic]["exercises"].append({
            "title": exercise_data["title"],
            "content": exercise_data["content"],
            "difficulty": exercise_data["difficulty"],
            "solution": exercise_data["solution"],
            "hints": []
        })

    # Convert the cache to a list of topics
    return list(topics.values())


def load_json_data(file_path: str) -> Dict[str, Any]:
    """
    Loads JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Dict[str, Any]: The loaded JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"The file {file_path} contains invalid JSON.", doc="", pos=0)


def save_json_data(file_path: str, data: Any) -> None:
    """
    Saves data to a JSON file.

    Args:
        file_path (str): Path to the output JSON file.
        data (Any): The data to save.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main() -> None:
    """
    Main function to execute the extraction and save to JSON.
    """
    # Path to the JSON file
    json_file_path = "exercises.json"

    try:
        # Load data from JSON
        data = load_json_data(json_file_path)

        # Format the data into topics
        topics = format_topics_json(data)

        # Save the formatted data to a new JSON file
        save_json_data("topics_raw.json", topics)

        print("Topics JSON file created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
