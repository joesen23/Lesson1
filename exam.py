def add_single_data(data):
  """Adds a single data entry to the array."""
  new_data = input("Enter the data to add: ")
  data.append(new_data)
  print("Data added successfully!")

def add_multiple_data(data):
  """Adds multiple data entries to the array."""
  num_entries = int(input("Enter the number of data entries to add: "))
  for i in range(num_entries):
    new_data = input(f"Enter data entry {i+1}: ")
    data.append(new_data)
  print("Data added successfully!")

def display_data(data):
  """Displays all data entries in the array."""
  if not data:
    print("No data available.")
  else:
    for i, entry in enumerate(data):
      print(f"Data entry {i+1}: {entry}")

def delete_data(data):
  """Deletes a data entry from the array."""
  if not data:
    print("No data available.")
  else:
    display_data(data)
    index = int(input("Enter the index of the data entry to delete: ")) - 1
    if 0 <= index < len(data):
      del data[index]
      print("Data deleted successfully!")
    else:
      print("Invalid index.")

def update_data(data):
  """Updates a data entry in the array."""
  if not data:
    print("No data available.")
  else:
    display_data(data)
    index = int(input("Enter the index of the data entry to update: ")) - 1
    if 0 <= index < len(data):
      new_data = input("Enter the new data: ")
      data[index] = new_data
      print("Data updated successfully!")
    else:
      print("Invalid index.")

def reverse_data(data):
  """Reverses the order of data entries in the array."""
  data.reverse()
  print("Data reversed successfully!")

data = []

while True:
  print("Menu:")
  print("1. Add single data")
  print("2. Add multiple data")
  print("3. Display data")
  print("4. Delete data")
  print("5. Update data")
  print("6. Reverse data")
  print("7. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    add_single_data(data)
  elif choice == '2':
    add_multiple_data(data)
  elif choice == '3':
    display_data(data)
  elif choice == '4':
    delete_data(data)
  elif choice == '5':
    update_data(data)
  elif choice == '6':
    reverse_data(data)
  elif choice == '7':
    break
  else:
    print("Invalid choice.")
