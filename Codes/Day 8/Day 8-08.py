from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caeser(start_text, shift_amount, sipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if sipher_direction == "encoded":
            new_position = position + shift_amount
            end_text += position[new_position]
            print(f"The encoded text is {end_text}")
        elif sipher_direction == "decoded":
            new_position - position - shift_amount
            end_text += position[new_position]
            print(f"The decoded text is {end_text}")

    
    
    

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.3
caeser(start_text = text, shift_amount = shift, sipher_direction = direction)