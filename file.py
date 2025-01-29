try:
    input_filename = input("Enter the filename to read from: ")
    with open(input_filename, 'r') as infile:
        content = infile.read()
    
    modified_content = content.upper()
    output_filename = "modified_" + input_filename
    
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)
    
    print(f"Modified content written to {output_filename}")
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read or write to the file.")