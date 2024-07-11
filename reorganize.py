import json
import os

def sort_categories(data):
    return {k: data[k] for k in sorted(data)}

def main():
    # Define the path to the config.json file
    config_path = 'config.json'
    
    # Read the JSON data from config.json
    with open(config_path, 'r') as file:
        data = json.load(file)
    
    # Sort the categories
    sorted_data = sort_categories(data)
    
    # Write the sorted JSON data back to config.json
    with open(config_path, 'w') as file:
        json.dump(sorted_data, file, indent=2)
    
    print(f"Categories in '{config_path}' have been sorted alphabetically.")

if __name__ == "__main__":
    main()