import os
from typing import Dict, List, Any
from langchain_google_genai import GoogleGenerativeAI  # Use the non-chat model
from dotenv import load_dotenv
import logging
from format_topics_json import load_json_data, save_json_data

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Load environment variables
load_dotenv()

# Validate API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


def get_llm() -> GoogleGenerativeAI:
    """
    Initializes and returns a Gemini LLM instance for text generation.

    Returns:
        GoogleGenerativeAI: An instance of the Gemini text generation model.
    """
    try:
        llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, api_key=api_key)
        logging.info("Gemini LLM initialized successfully.")
        return llm
    except Exception as e:
        logging.error(f"Error initializing Gemini LLM: {e}")
        raise


def call_llm(llm: GoogleGenerativeAI, content: str) -> str:
    """
    Calls the Gemini LLM to format LaTeX content into plain text.

    Args:
        llm (GoogleGenerativeAI): The Gemini text generation model instance.
        content (str): The LaTeX content to format.

    Returns:
        str: The formatted plain text.
    """
    try:
        prompt = "Necesito convertir este código LaTeX en un texto en un que se vea bien en un mensaje de Telegram. Los lstlistings sustitúyelos por ```csharp  ```.  Solo convierte, no añadas nada extra:\n\n" + content
        response = llm.generate([prompt])
        return response.generations[0][0].text
    except Exception as e:
        logging.error(f"Error calling Gemini LLM: {e}")
        raise


def format_topics_json(topics: List[Dict[str, Any]], llm: GoogleGenerativeAI) -> List[Dict[str, Any]]:
    """
    Formats the input JSON data into a structured list of topics with exercises.

    Args:
        topics (List[Dict[str, Any]]): The input list of topics containing exercises.
        llm (GoogleGenerativeAI): The Gemini text generation model instance.

    Returns:
        List[Dict[str, Any]]: A list of topics, each containing related exercises.
    """
    for topic in topics:
        for exercise in topic.get("exercises", []):
            try:
                # Format the exercise content using the LLM
                formatted_content = call_llm(llm, exercise["content"])
                formatted_solution = call_llm(llm, exercise["solution"]) if exercise["solution"] is not None else None
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
    json_file_path = "topics_raw.json"
    output_path = "topics.json"

    try:
        # Load data from JSON
        data = load_json_data(json_file_path)

        # Initialize Gemini LLM
        llm = get_llm()

        # Format the data into topics
        topics = format_topics_json(data, llm)

        # Save the formatted data to a new JSON file
        save_json_data(output_path, topics)

        logging.info(f"Topics JSON file created successfully at {output_path}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
