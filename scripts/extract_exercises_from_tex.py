import json
import re
import os


# Function to extract exercises from a .tex file
def extract_exercises_from_tex(tex_file_path):
    # Define categories based on sections
    category_mapping = {
        "Operaciones básicas": ["expressions"],
        "Condicionales": ["conditionals"],
        "Métodos": ["methods"],
        "Ciclos": ["loops"],
        "Arrays 1": ["arrays1"],
        "Arrays 2": ["arrays2"]
    }

    exercises = []
    current_section = None
    current_difficulty = None

    with open(tex_file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    for line in data.splitlines():
        section_match = re.match(r'\\section\{(.+?)\}', line)
        if section_match:
            current_section = section_match.group(1)
            continue

        difficulty_match = re.match(r'\s*%\s*(Basic|Advanced|Intermediate)', line)
        if difficulty_match:
            current_difficulty = difficulty_match.group(1)
            continue

        item_match = re.match(r'\s*\\item\s*\\textbf\{(.+?)\}', line)
        if item_match:
            title = item_match.group(1)
            continue

        path_match = re.match(r'\s*\\input\{(.+?)\}', line)
        if path_match:
            path = path_match.group(1)
            # Read the content from the file specified in the path
            content = ""
            exercise_path = os.path.join(os.path.dirname(tex_file_path), path)
            if os.path.exists(exercise_path):
                with open(exercise_path, 'r', encoding='utf-8') as exercise_file:
                    content = exercise_file.read()

            categories = category_mapping.get(current_section, [])

            exercises.append({
                "title": title,
                "path": path,
                "content": content.strip(),
                "difficulty": current_difficulty,
                "categories": categories
            })

    return exercises


# Main function to execute the extraction and save to JSON
def main():
    tex_file_path = 'src/exercises.tex'  # Replace with your .tex file path
    exercises = extract_exercises_from_tex(tex_file_path)

    # Convert to JSON format
    json_output = json.dumps({"exercises": exercises}, ensure_ascii=False, indent=4)

    # Optionally, save to a file
    with open('exercises.json', 'w', encoding='utf-8') as f:
        f.write(json_output)


if __name__ == "__main__":
    main()
