# import base64

# Non-functional way:

# #Open input file and read the file
# input_file = "my_input.txt"
# with open(input_file, "r") as file:
#     names = file.readlines()
#
# #Generate output file
# output_file = "my_output.txt"
# with open(output_file, "w") as file:
#     #strip leading and trialing space
#     for name in names:
#         name = name.strip()
#         encoded_name = base64.b64encode(name.encode("utf-8")).decode("utf-8") + "@protonmail.com"
#         file.write(encoded_name + "\n")

#functional Way:

import base64

#encode a single name function
def encode_name(name):
    encoded_name = base64.b64encode(name.encode("utf-8")).decode("utf-8")
    return f"{encoded_name}@protonmail.com"

#process files and use encode_name function
def file_process(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            names = file.readlines()

        with open(output_file, "w") as file:
            for name in names:
                name = name.strip()
                encoded_name = encode_name(name)
                file.write(encoded_name + "\n")

        print(f"{input_file} is encoded and save in a {output_file}")

    except FileNotFoundError:
        print(f"{input_file} file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#input and output file path:
input_file = "my_input.txt"
output_file = "my_output.txt"

file_process(input_file, output_file)