import json
from typing import Dict, List, Any

# Mapping of categories to their titles and descriptions
CATEGORY_MAPPING = {
    "expressions": {
        "title": "Operaciones básicas",
        "description": "Las operaciones básicas son el punto de partida de la programación. Nos permiten realizar cálculos matemáticos, combinar valores y construir expresiones más complejas. Imagina que estás creando una calculadora, determinando descuentos en una tienda en línea o calculando la distancia entre dos puntos en un mapa. Sin estas operaciones, cualquier intento de hacer algo útil en programación sería imposible."
    },
    "conditionals": {
        "title": "Condicionales",
        "description": "Los condicionales nos permiten tomar decisiones en nuestro código. ¿Alguna vez has jugado un videojuego donde ganas puntos si superas un obstáculo? Detrás de eso hay una estructura condicional que dice: 'Si el jugador supera el obstáculo, entonces aumenta su puntuación'. También son clave en aplicaciones del mundo real, como sistemas de seguridad ('Si la contraseña es correcta, permite el acceso') o recomendaciones personalizadas ('Si la temperatura es baja, sugiere ropa abrigada'). Sin condicionales, los programas serían rígidos y no podrían responder a diferentes situaciones."
    },
    "methods": {
        "title": "Métodos",
        "description": "Los métodos nos ayudan a organizar y reutilizar código. Piensa en cuando sigues una receta: en lugar de explicar cada paso cada vez que cocinas, simplemente dices 'preparar la masa' o 'hornear'. Un método en programación encapsula una serie de instrucciones para que podamos usarlas fácilmente sin repetirnos. Esto hace que nuestros programas sean más ordenados, más fáciles de entender y más eficientes. Sin métodos, el código sería un caos de repeticiones y sería difícil de mantener."
    },
    "loops": {
        "title": "Ciclos",
        "description": "Los ciclos nos permiten repetir acciones sin escribir el mismo código una y otra vez. Imagina que necesitas contar del 1 al 1000 en pantalla o procesar cada usuario en una lista de clientes. En lugar de escribir mil líneas de código, puedes usar un ciclo que haga el trabajo por ti. Son esenciales en videojuegos (mover personajes en cada cuadro de animación), análisis de datos (procesar millones de registros) y automatización de tareas. Sin ciclos, los programas serían tediosos y limitados a un tamaño fijo de entrada."
    },
    "arrays1": {
        "title": "Arrays 1",
        "description": "Un arreglo es una colección de elementos del mismo tipo almacenados juntos. En el mundo real, es como una lista de compras o un conjunto de respuestas en un examen. Nos permiten manejar datos de manera ordenada y eficiente. Si un programa necesita almacenar las calificaciones de los estudiantes o los productos en un carrito de compras, usar arreglos simplifica el proceso. Sin arreglos, tendríamos que crear una variable para cada elemento, lo que haría el código más complicado e ineficiente."
    },
    "arrays2": {
        "title": "Arrays 2",
        "description": "Los arreglos pueden ser multidimensionales o usarse junto con algoritmos para resolver problemas más complejos. ¿Cómo organizar una tabla de datos? ¿Cómo almacenar los píxeles de una imagen en una computadora? Los arreglos avanzados permiten manipular grandes volúmenes de información, optimizando la memoria y el tiempo de ejecución. Sin estas estructuras, muchas aplicaciones modernas, desde editores de imágenes hasta bases de datos, no funcionarían correctamente."
    }
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
