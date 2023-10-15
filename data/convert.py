import os
import shutil
import json
from datasets import load_dataset
# Existing data path
data_path = "."

# New structure path
new_data_path = "./hf_dataset"

# Create base folders
def transform_data():
    os.makedirs(os.path.join(new_data_path, "test"), exist_ok=True)

    with open(os.path.join(new_data_path, "test", "metadata.jsonl"), "w") as f:
        print('clear')
    # Loop through all files in the data path
    for file_name in os.listdir(data_path):
        # Get full file path
        file_path = os.path.join(data_path, file_name)
        if 'template.json' in file_path:
            continue
        # Check if it is a file
        if os.path.isfile(file_path):
            # Check if it is an image
            if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                # Move image to new structure
                shutil.copy(file_path, os.path.join(new_data_path, "test", file_name))
            # Check if it is a JSON
            elif file_name.lower().endswith(".json"):
                # Check if there is a corresponding image
                image_name = os.path.splitext(file_name)[0]  # Remove .json
                for ext in [".png", ".jpg", ".jpeg", ".JPG"]:
                    if os.path.exists(os.path.join(data_path, image_name + ext)):
                        # Load JSON data
                        print(file_path)
                        with open(file_path, "r") as f:
                            json_data = json.load(f)
                        conversations = []
                        for conv in json_data:
                            key = list(conv.keys())[0]
                            text = conv[key]
                            conversations.append({"from": key, "value": text})
                        # Create metadata entry
                        metadata_entry = {
                            "file_name": image_name + ext,
                            "conversations": json.dumps(conversations)
                        }
                        # Write to metadata.jsonl
                        with open(os.path.join(new_data_path, "test", "metadata.jsonl"), "a") as f:
                            f.write(json.dumps(metadata_entry) + "\n")
                        break

if __name__ == "__main__":
    transform_data()
    dataset = load_dataset('hf_dataset')
    dataset.push_to_hub("theblackcat102/gpt-4v-eval-samples")
    # dataset = load_dataset("theblackcat102/gpt-4v-eval-samples")['test']
    # print(dataset[2])
    # dataset[2]['image'].save('test/example.png')
