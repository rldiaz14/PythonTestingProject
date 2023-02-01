import os


#to make a create file to the doc
    
def create_file(file_name):
  if os.path.exists(file_path):
      raise Exception(f"File already exist: {file_path}")


  with open(file_name, 'w') as f:
        f.write("This is a new file.")

folder_name = "new_folder"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for i in range(1, 60):
    file_name = f"new_file_{i}.txt"
    file_path = os.path.join(folder_name, file_name)
    create_file(file_path)
    
    try:
      create_file(file_path)
    except Exception as e:
      print(f"Error: {e}")
      break