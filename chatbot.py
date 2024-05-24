import random

# Dictionary containing predefined responses
responses = {
    "hi": ["Hi!", "Hello!", "Hey!", "Hi there!"],
    "hi meedie":["Hi!", "Hello!", "Hey!", "Hi there!"],
    "how are you?": ["I'm doing well, thanks!", "Feeling great, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "anxiety": ["It's common to feel anxious. Remember to practice deep breathing or try mindfulness techniques.", "Anxiety can be tough. Have you tried talking to someone about it?"],
    "depression": ["Depression is draining, but you're not alone. vent to a journal or me your favorite bot friend!", "Depression can make things seem bleak, but there's hope. Have you considered therapy or counseling?"],
    "stress": ["Stress can take a toll on your well-being. It's important to find healthy coping mechanisms like exercise or meditation.", "Stress is a normal part of life, but finding ways to manage it is key. Have you tried journaling or relaxation techniques?"],
    "self-care": ["Self-care is important for mental health. Make time for activities you enjoy and prioritize your well-being.", "Remember to prioritize self-care. It's not selfish, it's essential for your mental health."],
    "gratitude": ["Practicing gratitude can improve your mood and overall well-being. Take a moment to reflect on the things you're grateful for.", "Gratitude can shift your focus from what you lack to what you have. What are you grateful for today?"],
    "therapy": ["Therapy can be beneficial for managing mental health challenges. Consider reaching out to a therapist for support.", "Therapy offers a safe space to explore your thoughts and feelings. Have you thought about giving it a try?"],
    "meditation": ["Meditation can help calm the mind and reduce stress. You should definitely give it a go.", "mhm ,Meditation has numerous benefits for mental health. Even just a few minutes a day can make a difference."],
}

# Examples triggering the depression response
depression_triggers = [
    "lately i've been feeling depressed",
    "i feel down all the time",
    "i'm struggling with depression",
    "depression has been weighing me down",
    "i'm feeling hopeless and sad",
    "i've lost interest in things i used to enjoy because of depression"
]
selfcare_triggers = [
    "I haven't been brushing my teeth or showering",
    "I havent done any hygiene today",
    "i havent showered today",
   # "i also havent done any hygiene today",
   # "i also haven't done any hygiene today"
]
meditation_triggers =[
    "ive been super anxious",
    "ive been feeling anxious",
    "lately ive been feeling anxious",
    "My head has been going in circles",
    "i can't think straight",
    "i cant focus on reality either"
]
# Function to generate bot response
def get_bot_response(user_input):
    user_input = user_input.lower()
    #print(user_input)
    
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    # Check if the input contains any of the depression triggers
    for trigger in depression_triggers:
        if trigger in user_input:
            return random.choice(responses["depression"])
        
    for trigger in selfcare_triggers:
        if trigger in user_input:
            return random.choice(responses["selfcare"])
        
    for trigger in meditation_triggers:
        if trigger in user_input:
            return random.choice(responses["meditation"])
        
        
    if "therapy" in user_input:
        return "Have you considered searching the internet for online therapy organizations or local therapy centers?"
    if "no" in user_input:
        return "It might also be helpful to consider searching the internet for online therapy organizations or local therapy centers."
    if "yes" in user_input:
        return "How has that been going?"
    if "good" in user_input:
        return "That's great to hear! Keep going and don't give up."
    if "bad" in user_input:
        return "I'm sorry to hear that. It might be beneficial to search for a different therapist."

    return "I'm here to support you. Feel free to talk to me about anything on your mind."

# Main function as the entry point for running the bop
#the for while loop continuosly prompts for user input until user enters exit
def main():
    print("Meebie: hey hey! I'm Meedie. Enter 'exit' to stop conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Take care of yourself. Goodbye!")
            break
        else:
            bot_response = get_bot_response(user_input)
            print("Meedie:", bot_response)

if __name__ == "__main__":
    main()
