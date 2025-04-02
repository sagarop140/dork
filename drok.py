import webbrowser

def generate_dork(query, domain_type, dork_type):
    dork_patterns = {
        "SQL Injection": [
            "\"SELECT * FROM users WHERE\"",
            "' OR '1'='1",
            "intitle:index.of?admin"
        ],
        "GitHub Dorks": [
            "filename:.env DB_PASSWORD",
            "filename:wp-config.php",
            "extension:sql"
        ]
    }
    
    base_url = "https://www.google.com/search?q="
    
    if domain_type:
        query = f"site:{query}{domain_type}"
    
    dork_queries = dork_patterns.get(dork_type, [])
    
    if not dork_queries:
        print("Invalid dork type selected.")
        return
    
    for dork in dork_queries:
        final_query = f"{query} {dork}"
        webbrowser.open(base_url + final_query)

def main():
    print("\nGoogle Dorking Automation Tool")
    site = input("Enter target site or keyword: ")
    domain_type = input("Enter domain type (e.g., .com, .gov, .edu) or press Enter to skip: ")
    
    print("\nSelect Dork Type:")
    print("1. SQL Injection")
    print("2. GitHub Dorks")
    choice = input("Enter choice (1/2): ")
    
    dork_type = "SQL Injection" if choice == "1" else "GitHub Dorks" if choice == "2" else None
    
    if dork_type:
        generate_dork(site, domain_type, dork_type)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
