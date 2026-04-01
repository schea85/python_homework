# Write your code here.

#task1:
def hello():
    return "Hello!"

#task2:
def greet(name):
    return f"Hello, {name}!"

#task3:
def calc(num1, num2, operator="multiply"):
    
    #error handling:
    if num2 == 0 and operator == "divide":
        return "You can't divide by 0!"
    
    if not all(isinstance(num, (int, float)) for num in [num1, num2]):
        return "You can't multiply those values!"
    
    #calculate
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2
    elif operator == "modulo":
        return num1 % num2
    elif operator == "int_divide":
        return num1 // num2
    elif operator == "power":
        return num1 ** num2
    else:
        return "Error: Try again."
    
#task4:
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return "Error: unsupported data type"
    except (ValueError, TypeError):
            return f"You can't convert {value} into a {data_type}."
    
#task5:
def grade(*args):
    try:
        total = 0
    
        for nums in args:
            total += nums
    
        avg = total / len(args)
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
#task6:
def repeat(text, count):
    result = ""
    
    for chars in range(count):
        result += text
    
    return result

#task7:
def student_scores(*args, **kwargs):
    total = 0
    
    if args[0] == "mean":
        for key, value in kwargs.items():
            total += value
    elif args[0] == "best":
        return max(kwargs, key=kwargs.get)
    
    return total / len(kwargs)

#task8:
def titleize(text):
    words = text.split(" ")
    lowercase_list = ["a", "on", "the", "of", "and", "is"]
    
    for i, word in enumerate(words):
        if i == 0:
            words[i] = word.capitalize()
        elif i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in lowercase_list:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()
    
    return " ".join(words)
        
#task9:
def hangman(secret, guess):
    result = ""
    
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    
    return result

#task10:
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split(" ")
    result_words = []
    
    for chars in words:
        if chars[0] in vowels:
            pig_latin_words = chars + "ay"
        else:
            for i, letter in enumerate(chars):
                if letter in vowels:
                    if i > 0 and chars[i-1:i+1] == "qu":
                        i += 1
                    pig_latin_words = chars[i:] + chars[:i] + "ay"
                    break
        result_words += [pig_latin_words]

    return " ".join(result_words)
    
