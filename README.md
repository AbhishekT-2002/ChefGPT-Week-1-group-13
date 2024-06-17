# Weekend Project: Chef GPT

## Overview
This project is a collaborative effort to enhance the Chef GPT script by giving it various unique personalities. Each group member has created a script with a distinct personality for the AI chef. The main script allows users to interact with any of these chefs based on their preferences. The AI chefs can suggest dishes based on ingredients, provide recipes, or critique user-provided recipes.

## Group Members

- **bOEXwz** - [@Ruchida (Fai)](https://github.com/Fai/)
- **MCn2Bp** - [@rparthas](https://github.com/rparthas/)
- **mIOHa2** - [@Abhi](https://github.com/AbhishekT-2002)
- **wAcaPj** - @junius
- **KLvOfB** - [@prasanth007](https://github.com/prasanth-ntu)


## Project Structure

- `main.py`: The main script that allows users to select and interact with different AI chefs.
- `default_chef.py`: The default Chef GPT script.
- `Abhi_mIOHa2.py`: A happy outgoing halwai chef from Uttar Pradesh, India.
- `Ruchida_bOEXwz.py`: A polite and create Thai cuisine chef
- `rparthas_MCn2Bp.py`: An expert South Indian chef
- `D.py`: (Placeholder for script D)
- `E.py`: (Placeholder for script E)

## How to Run

1. **Clone the repository**: Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/AbhishekT-2002/ChefGPT-Week-1-group-13
   ```
   ```bash
   cd https://github.com/AbhishekT-2002/ChefGPT-Week-1-group-13
   ```
2. **Run the script**: Run the `main.py` script using the following command:

   ```bash
   python main.py
   ```
3. **Interaction Flow**:
- Select Chef: Choose one of the available chefs.
- Enter Request: Provide ingredients, a dish name, or a recipe for critique.
- Receive Response: The selected chef will handle the request and provide a response.
## Example
```plaintext
0. Default
1. Indian
2. Thai
3. South Indian
4. Exit
Choose a chef to interact with: 2

Type the name of the dish you want a recipe for: Tom Yum
```
The Thai chef will provide the recipe for Tom Yum.
## Error Handling
The main script includes basic error handling to ensure smooth interactions. If an invalid chef is selected or an unexpected error occurs, the user will be prompted to try again.

## Contribution
Each group member has contributed a unique script representing a different personality for the AI chef. Please refer to individual script files for detailed implementation.
