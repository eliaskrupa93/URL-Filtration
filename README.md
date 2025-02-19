# Filter Handles

This Python script filters a list of Instagram handles (or similar usernames) against specific criteria—such as business keywords, celebrity names, male/female names, previously used accounts, and excessive special characters—and writes only the valid handles to an output file.

## Files Included

- **filterhandles.py**  
  The main script that processes and filters handles.

- **businesswords.txt**  
  Contains keywords identifying business-related usernames (e.g., “store,” “shop,” “brand”).

- **celebrities.txt**  
  Contains keywords identifying celebrity-related usernames.

- **femalenames.txt**  
  Contains common female names to help filter or allow certain handles.

- **malenames.txt**  
  Contains common male names to help filter certain handles.

> **Note:** The script references additional files like `usedalready.txt` and outputs to a file named `OUTPOUT` by default. These are **not** included by default and must be created or renamed as needed.

## How It Works

1. **Reads Input File:**  
   The script reads account URLs from a file named `INPUT` (modify this in the script if you prefer a different name).

2. **Loads Keywords and Names:**  
   - Business keywords from `businesswords.txt`  
   - Celebrity keywords from `celebrities.txt`  
   - Female names from `femalenames.txt`  
   - Male names from `malenames.txt`  

3. **Applies Filtering Criteria:**  
   - Skips usernames shorter than 5 characters.  
   - Skips usernames already listed in `usedalready.txt` (if that file exists).  
   - Skips usernames containing celebrity or business keywords.  
   - Skips usernames identified as male.  
   - Skips usernames with excessive special characters.  

4. **Outputs Valid Handles:**  
   All handles that pass the above checks are written to an output file named `OUTPOUT` (modify as needed).

## Setup & Usage

1. **Place Files Together:**  
   Make sure `filterhandles.py` and the `.txt` files (e.g., `businesswords.txt`, `celebrities.txt`, `femalenames.txt`, `malenames.txt`) are in the same folder, or adjust the script paths as needed.

2. **Prepare Input File:**  
   Create a file named `INPUT` (or the name you specify in the script) with one handle (URL) per line.

3. **Install Python 3:**  
   Ensure you have Python 3.x installed on your system.

4. **Run the Script:**  
   ```bash
   python filterhandles.py
   ```
   - The script will read from `INPUT` and write valid handles to `OUTPOUT`.

5. **Check the Results:**  
   - View the terminal output for a summary of skipped and accepted accounts.
   - The valid handles will appear in the `OUTPOUT` file (you may rename this in the script).

## Customization

- **File Paths:**  
  Update the file paths in the script (`INPUT`, `OUTPOUT`, etc.) to match your file locations or preferred filenames.
- **Keywords & Names:**  
  Edit the `.txt` files to include or remove keywords and names based on your needs.
- **Additional Criteria:**  
  Modify or add your own filtering logic within `filterhandles.py` to meet specific requirements.

## Disclaimer

Use this script responsibly and in accordance with any applicable platform policies or legal requirements. The author is not responsible for any misuse or consequences arising from its usage.
