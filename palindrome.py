def is_palindrome(text):
    # Convert to string, remove spaces, and convert to lowercase for uniform checking
    cleaned = "".join(str(text).split()).lower()
    return cleaned == cleaned[::-1]


# Example usage:
if __name__ == "__main__":
    user_input = input("Enter a word, phrase, or number: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")