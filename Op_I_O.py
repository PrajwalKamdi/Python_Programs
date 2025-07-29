class Op_I_O:
  def open_file(self, file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: The file was not found."
    except IOError:
        return "Error: An I/O error occurred while accessing the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
  def close_file(self, file):
    try:
        file.close()
    except Exception as e:
        return f"An error occurred while closing the file: {e}"
    return "File closed successfully."
  

  def write_file(self, file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            return "File written successfully."
    except IOError:
        return "Error: An I/O error occurred while writing to the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
op = Op_I_O()
print(op.open_file(r"C:\Users\HP\OneDrive\Desktop\Practice\Files\Jokes.text"))
# print(op.write_file(r"C:\Users\HP\OneDrive\Desktop\Practice\Files\Jokes.text", "\n12. Abhi aaya na line pe is a new joke."))  # Writing to file
