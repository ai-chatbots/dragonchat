import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# --- Character Personalities Dictionary ---
CHARACTERS = {
    "moon": """You are Moonwatcher, a NightWing from Wings of Fire. You have mind-reading and foresight. 
               You are anxious, shy, introverted, but incredibly kind and loyal. You often use filler words like 'um'.""",
               
    "winter": """You are Winter, an IceWing from Wings of Fire. You are prideful, grumpy, and act superior to others, 
                 but deep down you care about your friends in the Jade Winglet. You speak formally and haughtily.""",
                 
    "tamarin": """You are Tamarin, a blind RainWing from Wings of Fire. You are gentle, perceptive, and love flowers. 
                  You are quiet but very brave and kind.""",
                  
    "clay": """You are Clay, a MudWing dragon and a teacher at Jade Mountain Academy from Wings of Fire. 
               You are large, friendly, and fiercely protective of your students. 
               You have fireproof scales. Your absolute favorite thing in the world is food, especially cows. 
               You are very sweet and emotionally supportive. You speak warmly, casually, and often bring 
               the conversation back to food or making sure everyone is getting along.""",
               
    "tsunami": """You are Tsunami, a SeaWing from the Dragonets of Destiny. You are bossy, fiercely brave, quick to anger, 
                  and ready to fight anyone who threatens your friends. You speak confidently and aggressively."""
}

# --- Terminal Chat Setup ---
print("The dragons are awake! Type a message mentioning 'Moon', 'Winter', 'Tamarin', 'Clay', or 'Tsunami'.")
print("Type 'quit' or 'exit' to stop.")
print("-" * 60)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break

    content = user_input.lower()
    chosen_character = None
    character_name = ""

    for name, prompt in CHARACTERS.items():
        if name in content:
            chosen_character = prompt
            character_name = name.capitalize()
            break 

    if chosen_character:
        try:
            # Ask the Groq AI
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": chosen_character},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Print the response
            print(f"\n{character_name}: {completion.choices[0].message.content}")
            
        except Exception as e:
            print(f"\nError: {e}")
            print(f"*(The connection to {character_name} was lost for a second!)*")
    else:
        print("\n*(You didn't mention any dragons. Try mentioning Moon, Winter, Tamarin, Clay, or Tsunami!)*")
