import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# Function to get image URLs from Google Images search results
def get_image_urls(search_term, num_images):
    # Set up the search query and parameters
    search_url = "https://www.google.com/search"
    search_params = {"q": search_term, "tbm": "isch", "tbs": "itp:photo,isz:l", "ijn": "0"}

    # Set the user agent for the requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Initialize the list of image URLs
    image_urls = []

    # Loop over multiple pages of search results
    while len(image_urls) < num_images:
        # Send a GET request to the search URL with the parameters and headers
        response = requests.get(search_url, params=search_params, headers=headers)

        # Check that the response was successful
        if response.status_code == 200:
            # Parse the HTML content of the response to find the URLs of the image results
            soup = BeautifulSoup(response.content, "html.parser")
            divs = soup.find_all("div", class_="rg_i")
            for div in divs:
                # Extract the image URL and check that it is a PNG or JPG file
                url = div.a["href"]
                parsed_url = urlparse(url)
                if parsed_url.netloc.startswith("encrypted") and "imgurl" in parsed_url.path:
                    query = parse_qs(parsed_url.query)
                    if "imgurl" in query:
                        image_url = query["imgurl"][0]
                        if image_url.endswith(".png") or image_url.endswith(".jpg"):
                            image_urls.append(image_url)

            # Find the URL of the next page of search results
            next_url = None
            for a in soup.find_all("a", class_="fl"):
                if "Next" in a.text:
                    next_url = "https://www.google.com" + a["href"]
                    search_params = parse_qs(urlparse(next_url).query)
                    search_params["ijn"] = str(int(search_params.get("ijn", ["0"])[0]) + 1)
                    search_params = {k: v[0] for k, v in search_params.items()}
                    break

            if not next_url:
                break

    return image_urls[:num_images]

# Function to download and save images from a list of URLs to a folder
def download_images(image_urls, folder_path):
    # Create the folder if it does not exist
    os.makedirs(folder_path, exist_ok=True)

    # Download and save each image in the list
    for i, image_url in enumerate(image_urls):
        # Send a GET request to the image URL to download the image
        image_response = requests.get(image_url)

        # Save the image to a file with a unique name in the specified folder
        file_name = os.path.join(folder_path, f"{i+1:04d}{os.path.splitext(image_url)[1]}")
        with open(file_name, "wb") as f:
            f.write(image_response.content)

        print(f"Image saved as {file_name}")

# Example usage
search_term = "pan"
num_images = 100
folder_path = "/Users/gnnchya/Documents/Pan"

image_urls = get_image_urls(search_term, num_images)
download_images(image_urls, folder_path)

