import json
import re
import os
import logging
from typing import Dict, List, Optional, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Mapping of sections to categories
CATEGORY_MAPPING = {
    "Operaciones básicas": "expressions",
    "Condicionales": "conditionals",
    "Métodos": "methods",
    "Ciclos": "loops",
    "Arrays 1": "arrays1",
    "Arrays 2": "arrays2"
}


def read_file(file_path: str) -> Optional[str]:
    """
    Reads the content of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[str]: The content of the file, or None if the file doesn't exist.
    """
    if not os.path.exists(file_path):
        logging.warning(f"File not found: {file_path}")
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return None


def extract_exercises_from_tex(tex_file_path: str) -> List[Dict[str, Any]]:
    """
    Extracts exercises from a .tex file.

    Args:
        tex_file_path (str): Path to the .tex file.

    Returns:
        List[Dict[str, Any]]: A list of extracted exercises.
    """
    exercises = []
    current_section = None
    current_difficulty = None
    title = None

    # Read the .tex file content
    tex_content = read_file(tex_file_path)
    if tex_content is None:
        return exercises

    for line in tex_content.splitlines():
        # Match section headers
        section_match = re.match(r'\\section\{(.+?)\}', line)
        if section_match:
            current_section = section_match.group(1)
            continue

        # Match difficulty comments
        difficulty_match = re.match(r'\s*%\s*(Basic|Advanced|Intermediate)', line)
        if difficulty_match:
            current_difficulty = difficulty_match.group(1)
            continue

        # Match exercise titles
        item_match = re.match(r'\s*\\item\s*\\textbf\{(.+?)\}', line)
        if item_match:
            title = item_match.group(1)
            continue

        # Match exercise file paths
        path_match = re.match(r'\s*\\input\{(.+?)\}', line)
        if path_match and title:
            path = path_match.group(1)
            exercise_path = os.path.join(os.path.dirname(tex_file_path), path)
            solution_path = exercise_path.replace("exercises", "solutions")

            # Read exercise content
            content = read_file(exercise_path) or ""
            solution = read_file(solution_path) or ""

            # Get categories for the current section
            topic = CATEGORY_MAPPING.get(current_section, None)

            # Append the exercise to the list
            exercises.append({
                "title": title,
                "path": path,
                "content": content.strip() or None,
                "difficulty": current_difficulty,
                "topic": topic,
                "solution": solution.strip() or None
            })

            # Reset title for the next exercise
            title = None

    return exercises


def save_to_json(data: Dict[str, Any], output_path: str) -> None:
    """
    Saves data to a JSON file.

    Args:
        data (Dict[str, Any]): The data to save.
        output_path (str): Path to the output JSON file.
    """
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logging.info(f"Data saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving to {output_path}: {e}")


def main() -> None:
    """
    Main function to execute the extraction and save to JSON.
    """
    tex_file_path = "src/exercises.tex"  # Replace with your .tex file path
    output_path = "exercises.json"

    # Extract exercises from the .tex file
    exercises = extract_exercises_from_tex(tex_file_path)

    # Save the extracted exercises to a JSON file
    save_to_json({"exercises": exercises}, output_path)


if __name__ == "__main__":
    main()
