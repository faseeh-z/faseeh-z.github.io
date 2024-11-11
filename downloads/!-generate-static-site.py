import os
import yaml

sites_dir = "sites"

# To add tabs to a multi-line string
def add_tabs(content, number_of_tabs_to_add):
    tabs = '\t' * number_of_tabs_to_add
    return '\n'.join([tabs + line for line in content.splitlines()])



print("Scanning 'sites' dir")
for dir_name in os.listdir(sites_dir): # Loop through all sites folders
    dir_path = os.path.join(sites_dir, dir_name)

    print(f"Acquiring metadata for {dir_name}") # Acquiring metadata
    with open(os.path.join(dir_path, "metadata.yaml"), "r") as rawdata:
        data = yaml.safe_load(rawdata)

    print(f"Creating html file for {dir_name}") # Creating html file
    with open(data["filename"] + ".html", "w") as htmlfile:
        htmlfile.write(
            f"""
<!DOCTYPE html>
<html lang="en">
<head>
\t<meta charset="UTF-8">
\t<meta name="viewport" content="width=device-width, initial-scale=1.0">
\t<link rel="stylesheet" href="assets/styles.css">
\t<title>{data["title"]}</title>
</head>
<body>
\t<div class="container">
"""
        )

        print("Pasting content") # Pasting content from content.html
        with open(os.path.join(dir_path, "content.html"), "r") as content_file:
            content = add_tabs(content_file.read(), 2)
            htmlfile.write(content)
            htmlfile.write("\n")

        print("Creating downloads section")
        htmlfile.write(f"\t\t<div class='downloads-section'>\n") # Downloads section
        for link in data["download_links"]: # Create download button for each link
            htmlfile.write(f"""
\t\t\t<div class="item-div">
\t\t\t\t<p>{link[0]}</p>
\t\t\t\t<a href="{link[1]}" download><button class="download-btn">Download</button></a>
\t\t\t</div>
""")

        print("Closing file")
        htmlfile.write("""
\t\t</div>
\t</div>
</body>
</html>
"""
        )
