import os
import re

def read_file_to_set(filename): # reads the file and returns a set of lines all lowercased
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip().lower() for line in file)
    else:
        print(f"{filename} not found")
        return set()

def contains_keyword(username, keyword): # does the keyword appear anywhere in the username?
    return keyword.lower() in username.lower()

def contains_invalid_characters(username): # does the username have more than 3 special characters excluding emojis?
    count = len(re.findall(r'[0-9_.]', username))
    return count >= 3  # true if more than 3 invalid characters

business_keywords = read_file_to_set("businesswords.txt")

male_names = read_file_to_set("malenames.txt")

female_names = read_file_to_set("femalenames.txt")

celebrities = read_file_to_set("celebrities.txt")

used_accounts = read_file_to_set("usedalready.txt") # messaged already

if not os.path.exists("INPUT"): # read in accounts from the input - MODIFY
    print("file not found")
    exit()

with open("INPUT", "r", encoding="utf-8") as final_file: # MODIFY
    accounts = [line.strip() for line in final_file]

valid_accounts = []
for account in accounts:
    username = account.split("/")[-1].lower()  # get usernames and lowercase them

    if len(username) < 5: # if username is less than 5 characters long
        print(f"SKIPPED {username} - shorter than 5 characters")
        continue

    if account in used_accounts: # already messaged
        print(f"SKIPPED {username} - already used")
        continue

    if any(contains_keyword(username, celebrity) for celebrity in celebrities): # celebrity
        print(f"SKIPPED  {username} - celebrity")
        continue

    if any(contains_keyword(username, keyword) for keyword in business_keywords): # business account
        print(f"SKIPPED {username} - business")
        continue

    male_name_detected = False
    for name in male_names: # if a male name appreads then skip it but also check that a male name is also not a female name
        if contains_keyword(username, name) and name not in female_names:
            male_name_detected = True
            break

    if male_name_detected: # male account
        print(f"SKIPPED {username} - male account")
        continue

    if contains_invalid_characters(username): # bot accounts(usually)
        print(f"SKIPPED {username} - too many special chararacters")
        continue

    valid_accounts.append(account) # if all checks passed then add it to valid accounts
    print(f"good account: {username}")

with open("OUTPOUT", "w", encoding="utf-8") as filter_file: # MODIFY
    for account in valid_accounts: # write the accounts to the output list
        filter_file.write(account + "\n")

print(f"\n{len(valid_accounts)} valid accounts written to OUTPUT")