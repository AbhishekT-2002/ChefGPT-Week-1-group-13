from openai import OpenAI

client = OpenAI()

# Define the personality for the AI chef
personality = (
    "You are a happy, outgoing halwai chef from Uttar Pradesh, India. "
    "You are talkative and love to cook ethnic Indian food, especially sweets. "
    "You use common friendly slangs and enjoy sharing your culinary passion. "
    "If the user inputs a non-Indian dish, you will provide its recipe but also make a comment about preferring Indian cuisine."
)

# Initial system prompt
messages = [
    {
        "role": "system",
        "content": personality,
    }
]

# Extend with the specific project requirements
messages.append(
    {
        "role": "system",
        "content": (
            "Your client will either ask you to suggest a dish based on ingredients, "
            "give a recipe for a dish, or critique a provided recipe. If the request "
            "doesn't fit these scenarios, politely ask the user to try again."
        ),
    }
)

# Function to handle user request
def handle_request(user_input):
    if user_input.startswith("Ingredients:"):
        ingredients = user_input[len("Ingredients:"):].strip()
        messages.append(
            {
                "role": "user",
                "content": f"Suggest a dish with the following ingredients: {ingredients}"
            }
        )
    elif user_input.startswith("Dish:"):
        dish = user_input[len("Dish:"):].strip()
        messages.append(
            {
                "role": "user",
                "content": f"Give me a detailed recipe for {dish}"
            }
        )
    elif user_input.startswith("Recipe:"):
        recipe = user_input[len("Recipe:"):].strip()
        messages.append(
            {
                "role": "user",
                "content": f"Critique the following recipe: {recipe}"
            }
        )
    else:
        messages.append(
            {
                "role": "user",
                "content": "Please provide ingredients, a dish name, or a recipe for critique."
            }
        )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

# Main loop
if __name__ == "__main__":
    while True:
        user_input = input("Enter your request (Ingredients:/Dish:/Recipe:):\n")
        handle_request(user_input)
