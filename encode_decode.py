import base64

def encode_file(input_file, output_file):
    with open(input_file, "rb") as f:
        encoded_data = base64.b64encode(f.read())
    with open(output_file, "wb") as f:
        f.write(encoded_data)
    print(f"[+] File encoded successfully as '{output_file}'")

def decode_file(input_file, output_file):
    with open(input_file, "rb") as f:
        decoded_data = base64.b64decode(f.read())
    with open(output_file, "wb") as f:
        f.write(decoded_data)
    print(f"[+] File decoded successfully as '{output_file}'")

def main():
    print("=== Base64 Encode/Decode Tool ===")
    print("1. Encode a file")
    print("2. Decode a file")
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        infile = input("Enter file to encode: ")
        outfile = input("Enter output filename (encoded): ")
        encode_file(infile, outfile)
    elif choice == "2":
        infile = input("Enter base64-encoded file to decode: ")
        outfile = input("Enter output filename (decoded): ")
        decode_file(infile, outfile)
    else:
        print("[-] Invalid choice.")

if __name__ == "__main__":
    main()

