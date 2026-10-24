# Text Compression Using Character Runs

def compress_text(text):
    if not text:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    # Encode the final character run
    encoded += text[-1] + str(count)

    return encoded


# Main program
print("===== TEXT COMPRESSION USING CHARACTER RUNS =====")

text = input("Enter a string: ")

encoded_text = compress_text(text)

original_length = len(text)
encoded_length = len(encoded_text)

print("\nOriginal String:", text)
print("Encoded String:", encoded_text)
print("Original Length:", original_length)
print("Encoded Length:", encoded_length)

if encoded_length < original_length:
    print("Result: Compression is beneficial.")
    saved = original_length - encoded_length
    print("Characters Saved:", saved)
elif encoded_length == original_length:
    print("Result: Compression provides no length reduction.")
else:
    print("Result: Encoding is not beneficial.")
    extra = encoded_length - original_length
    print("Additional Characters:", extra)

print("=================================================")