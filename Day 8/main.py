alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(cipher_text, shift_amount, cipher_direction):
    if shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)
    # in case of decoding
    if cipher_direction == "decode":
        shift_amount = len(alphabet) - shift_amount
    text_out = ""
    for char in cipher_text:
        if char in alphabet:
            index_in = alphabet.index(char)
            index_out = index_in + shift_amount
            # if the new index would end up beyond the list, roll over to the beginning
            if index_out > len(alphabet) - 1:
                index_out -= len(alphabet)
            text_out += alphabet[index_out]
        else:
            text_out += char
    return text_out

while True:
    print("Type \"encode\" to encrypt, type \"decode\" to decrypt:")

    direction = ""
    while True:
        direction = input("> ").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("Invalid choice. Please enter \"encode\" or \"decode\".")
    print("Type your message:")
    text = input("> ").lower()

    print("Type the shift number:")
    shift = 0
    while True:
        shift_str = input("> ")
        if shift_str.isdigit():
            shift = int(shift_str)
            
            if shift % len(alphabet) == 0:
                print(f"Invalid choice. Shifting by {shift} would result in an identical message.")
            else:
                break
        else:
            print("Invalid choice. Please enter a positive integer.")

    result = caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)

    print(f"The message \"{text}\" {direction}d using a shift of {shift} is \"{result}\".")

    print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
    choice = input("> ").lower()
   
    if choice == "no":
        break

print("Goodbye.")
