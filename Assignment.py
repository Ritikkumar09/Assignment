
# import pandas as pd 

# def csv_to_excel(csv_file, excel_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_file)  # Load data from CSV

#     # Save the data into an Excel file
#     df.to_excel(excel_file, index=False)  # Write to Excel
#     print(f"File converted: {excel_file}")

# def read_excel_file(excel_file):
#     # Read the Excel file into a DataFrame
#     df = pd.read_excel(excel_file)
#     print("Excel file contents are :")
#     print(df.to_string())

# # Call the function with file names
# csv_file = 'Products.csv'      # Use 'Product.csv' as the input file
# excel_file = 'Product.xlsx'    # Set the desired output file name create new file if not find 

# # Convert CSV to Excel
# csv_to_excel(csv_file, excel_file)

# # Read and display the file contents
# read_excel_file(excel_file) #Excel  file read from function call
# csvfile=pd.read_csv("Products.csv") #Csv file read
# print("Csv file content")
# print(csvfile.to_string())







# # Function to read and print the contents of the CSV file
# def read_csv_file(csv_file):
#     print("Contents of the CSV file:")
#     with open(csv_file, 'r') as csv_f:
#         for line in csv_f:
#             # Print each line
#             print(line.strip())  # Strip the newline character
# # Function to convert CSV to XLS format without any third-party libraries
# def csv_to_xls(csv_file, excel_file):
#     with open(csv_file, 'r') as csv_f:
#         with open(excel_file, 'w') as xls_f:
#             for line in csv_f:
#                 # Replace commas with tabs for a basic XLS format
#                 xls_f.write(line.replace(',', '\t'))
#     print(f"File converted successfully: {excel_file}")
# # Function to read the basic XLS file after converting it
# def read_xls_file(excel_file):
#     print("Contents of the XLS file:")
#     with open(excel_file, 'r') as xls_f:
#         for line in xls_f:
#             # Print each line, with tabs separating the values
#             print(line.strip().replace('\t', ' | '))  # Replace tabs with ' | ' for easier reading

# csv_file = 'Products.csv' #input as csv file
# excel_file = 'Products1.xls' #create excel file
# # Convert CSV to basic XLS format
# csv_to_xls(csv_file, excel_file)
# #read an display csv file
# read_csv_file(csv_file)
# # Read and display the XLS file
# read_xls_file(excel_file)





import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

def scrape_data(url, element, class_name):
    """
    Generic function to scrape data from any website based on element and class name.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    try:
        # Send GET request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements
    data = []
    elements = soup.find_all(element, class_=class_name)
    for elem in elements:
        data.append(elem.get_text(strip=True))

    return data

def save_to_json(data, filename):
    """
    Save scraped data to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def start_scraping():
    """
    Start the scraping process with user inputs from the GUI.
    """
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    # Get the HTML element and class name from user
    element = simpledialog.askstring("Input", "Enter the HTML element (e.g., div, h1, p):")
    class_name = simpledialog.askstring("Input", "Enter the class name (leave blank if none):")

    try:
        # Scrape the data
        scraped_data = scrape_data(url, element, class_name)
        if not scraped_data:
            messagebox.showinfo("No Data", "No data found for the given element and class name.")
            return

        # Ask user where to save JSON
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            save_to_json(scraped_data, file_path)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI
root = tk.Tk()
root.title("Generic Web Scraper")

# Create and place widgets
tk.Label(root, text="Enter URL to scrape:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
scrape_button = tk.Button(root, text="Scrape and Save", command=start_scraping)
scrape_button.pack(pady=20)
# Start the GUI event loop
root.mainloop()