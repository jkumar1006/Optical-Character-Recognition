#Libraries
import google.generativeai as genai
import PIL.Image
import os
import shutil
import pandas as pd
from config import configs

#configuring google gen ai api
genai.configure(api_key=configs['GOOGLE_API_KEY'])
model = genai.GenerativeModel(configs['model']) #loading gemini-1.5-flash

# declaring directories
untransformed_dir = 'images/un-transformed'
transformed_dir = 'images/transformed'
excel_file_path = 'transformed_images_responses.xlsx'
os.makedirs(transformed_dir, exist_ok=True)
# list to save responses
results = []
# Iterate through all files in the untransformed directory
for filename in os.listdir(untransformed_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Construct full file path
        untransformed_file_path = os.path.join(untransformed_dir, filename)
        transformed_file_path = os.path.join(transformed_dir, filename)
        
        # Open the image
        img = PIL.Image.open(untransformed_file_path)
        
        
        # Process the image using the model (this is a placeholder for your actual processing code)
        response = model.generate_content(["return output in JSON", img])
        #response = model.generate_content(img)
        response_text = response.text.replace('json', '').strip()
        print(response_text)
        
        # Append the result to the list
        results.append({'Image Name': filename, 'Response': response_text})
        
        # Move the transformed file to the transformed directory
        shutil.move(untransformed_file_path, transformed_file_path)

# convert to Data Frame
results_df = pd.DataFrame(results)

# if the Excel file exists
if os.path.exists(excel_file_path):
    # existing data
    existing_df = pd.read_excel(excel_file_path)
    # Append the new data to existing data
    combined_df = pd.concat([existing_df, results_df], ignore_index=True)
else:
    # the new data is the combined data
    combined_df = results_df

# Save the combined data to the Excel file
combined_df.to_excel(excel_file_path, index=False)

print("Processing complete. Results saved to", excel_file_path)