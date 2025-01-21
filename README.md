This is a simple Google Dork generator script that uses dorks from CoffinXP and makes your target domain-specific for efficient reconnaissance

Dork made by **CoffinXP**.

---

## 🔍 Overview
GoogleDorky is a simple Google Dork generator script that takes a set of advanced dorks, replaces the default `example.com` domain with your target domain, and outputs a customized list of reconnaissance-ready dorks.  
Dorks are based on contributions from **CoffinXP**.

## 🚀 Features
- **Effortless Domain Customization**: Replace `example.com` with your domain of interest.
- **Advanced Dorks Included**: Search for sensitive files, error pages, vulnerable parameters, cloud storage, and more.
- **Time-Saving**: Automates dork customization to save time during reconnaissance.
- **Output File**: Saves results to `updated_dorks.txt`.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/googledorky.git

2. Navigate to the directory:

3. cd googledorky

Ensure Python 3.6+ is installed.

## Usage

Run the script:

python3 generate_dorks.py

Enter your target domain (e.g., yourtarget.com) when prompted.
View the output dorks in the terminal and the updated_dorks.txt file.


## How it Works



    The script reads a pre-defined set of Google dorks containing example.com.
    It replaces example.com with the user-specified domain.
    Displays the updated dorks and writes them to an output file for easy access.

## 📝 Example of Usage

    Input:

google.com

Output:

    site:google.com -www -shop -share -ir -mfa
    site:google.com ext:php inurl:?
    site:google.com inurl:api | site:*/rest | site:*/v1 | site:*/v2 | site:*/v3
    ...

    The output will also be saved in updated_dorks.txt.

## 📂 Features of Included Dorks

    Sensitive Files: Find files like .env, .log, .conf, etc.
    Error Messages: Search for pages revealing backend errors.
    Cloud Services: Identify exposed cloud storage and services.
    Vulnerable Parameters: Pinpoint URLs prone to exploitation.



Special thanks to CoffinXP for contributing the dorks and supporting the security community.
