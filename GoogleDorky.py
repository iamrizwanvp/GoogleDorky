#!/usr/bin/env python3
import os

# ASCII Banner
banner = """
   █████████                             ████           ██████████                      █████                
  ███░░░░░███                           ░░███          ░░███░░░░███                    ░░███                 
 ███     ░░░   ██████   ██████   ███████ ░███   ██████  ░███   ░░███  ██████  ████████  ░███ █████ █████ ████
░███          ███░░███ ███░░███ ███░░███ ░███  ███░░███ ░███    ░███ ███░░███░░███░░███ ░███░░███ ░░███ ░███ 
░███    █████░███ ░███░███ ░███░███ ░███ ░███ ░███████  ░███    ░███░███ ░███ ░███ ░░░  ░██████░   ░███ ░███ 
░░███  ░░███ ░███ ░███░███ ░███░███ ░███ ░███ ░███░░░   ░███    ███ ░███ ░███ ░███      ░███░░███  ░███ ░███ 
 ░░█████████ ░░██████ ░░██████ ░░███████ █████░░██████  ██████████  ░░██████  █████     ████ █████ ░░███████ 
  ░░░░░░░░░   ░░░░░░   ░░░░░░   ░░░░░███░░░░░  ░░░░░░  ░░░░░░░░░░    ░░░░░░  ░░░░░     ░░░░ ░░░░░   ░░░░░███ 
                                ███ ░███                                                            ███ ░███ 
                               ░░██████                                                            ░░██████  
                                ░░░░░░                                                              ░░░░░░   
"""

# Credits
credits = "Dorks credits go to CoffinXP\n"

def generate_dorks(domain):
    dorks = [
        "site:example.com -www -shop -share -ir -mfa",
        "site:example.com ext:php inurl:?",
        "site:example.com inurl:api | site:*/rest | site:*/v1 | site:*/v2 | site:*/v3",
        "site:'example.com' ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess | ext:json",
        "inurl:conf | inurl:env | inurl:cgi | inurl:bin | inurl:etc | inurl:root | inurl:sql | inurl:backup | inurl:admin | inurl:php site:example.com",
        "inurl:'error' | intitle:'exception' | intitle:'failure' | intitle:'server at' | inurl:exception | 'database error' | 'SQL syntax' | 'undefined index' | 'unhandled exception' | 'stack trace' site:example.com",
        "inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:example.com",
        "inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:& inurl:http site:example.com",
        "inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:example.com",
        "inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:& site:example.com",
        "inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:& site:example.com",
        "inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:& site:example.com",
        "site:s3.amazonaws.com 'example.com'",
        "site:blob.core.windows.net 'example.com'",
        "site:googleapis.com 'example.com'",
        "site:drive.google.com 'example.com'",
        "site:dev.azure.com 'example.com'",
        "site:onedrive.live.com 'example.com'",
        "site:digitaloceanspaces.com 'example.com'",
        "site:sharepoint.com 'example.com'",
        "site:s3-external-1.amazonaws.com 'example.com'",
        "site:s3.dualstack.us-east-1.amazonaws.com 'example.com'",
        "site:dropbox.com/s 'example.com'",
        "site:box.com/s 'example.com'",
        "site:docs.google.com inurl:'/d/' 'example.com'",
        "site:jfrog.io 'example.com'",
        "site:firebaseio.com 'example.com'",
        "site:pastebin.com 'example.com'",
        "site:jsfiddle.net 'example.com'",
        "site:codebeautify.org 'example.com'",
        "site:codepen.io 'example.com'",
        "inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:'example.com'",
        "site:openbugbounty.org inurl:reports intext:'example.com'",
        "site:groups.google.com 'example.com'",
        "site:example.com 'choose file'",
        "inurl:login | inurl:signin | intitle:login | intitle:signin | inurl:secure site:example.com",
        "inurl:test | inurl:env | inurl:dev | inurl:staging | inurl:sandbox | inurl:debug | inurl:temp | inurl:internal | inurl:demo site:example.com",
        "site:example.com ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx",
        "intext:'confidential' | intext:'Not for Public Release' | intext:'internal use only' | intext:'do not distribute'",
        "inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:& site:example.com"
    ]
    # Replace 'example.com' with the user's input domain
    return [dork.replace("example.com", domain) for dork in dorks]

def save_to_file(dorks, output_file):
    with open(output_file, "w") as f:
        for dork in dorks:
            f.write(dork + "\n\n")  # Add a blank line between dorks for clarity

def main():
    # Display banner and credits
    print(banner)
    print(credits)

    # Prompt user for inputs
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    if not domain:
        print("[Error] No domain entered. Exiting.")
        return

    output_file = input("Enter the output file name (e.g., dorks.txt): ").strip()
    if not output_file:
        print("[Error] No output file name entered. Exiting.")
        return

    # Generate and save dorks
    dorks = generate_dorks(domain)
    save_to_file(dorks, output_file)

    print(f"\nDorks successfully generated and saved to {output_file}")

if __name__ == "__main__":
    main()
