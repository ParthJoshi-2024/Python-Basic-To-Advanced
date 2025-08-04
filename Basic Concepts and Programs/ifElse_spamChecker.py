"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams and print "Spam detected" if any of these keywords are found in the text.
"""

def is_spam(comment):
    spam_keywords = [
        "make a lot of money",
        "buy now",
        "subscribe this",
        "click this"
    ]
    
    comment_lower = comment.lower()
    
    for keyword in spam_keywords:
        if keyword in comment_lower:
            return True
    return False

def main():
    print("Welcome to the Spam Checker!")
    while True:
        user_input = input("\nEnter a comment to check for spam (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if is_spam(user_input):
            print("Spam detected")
        else:
            print("No spam detected")

