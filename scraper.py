import urllib.request
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def send_request(url):
    """sends get request to url and checks to see if the conten is html"""

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print(f'{url}:{str(e)}')
        return None


def is_good_response(resp):
    """returns true if response is html"""
    conten_type = resp.headers['content-Type'].lower()
    return (resp.status_code == 200
            and conten_type is not None
            and conten_type.find('html') > -1)


def save_to_file(html):
    """Save html to a file named index.html"""
    with open('index.html', 'w') as file:
        html = str(html).strip('\n')
        file.write(u"{}".format(html))


def open_file():
    """Get all the data from the file then return it"""
    try:
        f = open("index.html", "r")
        return f.read()
    except:
        print("ERROR OPENING FILE")
    finally:
        f.close()


def get_all_img_links():
    """Grab all the image links from the index.html"""
    try:
        html_content = open_file()
        soup = BeautifulSoup(html_content)
        images = []

        for img in soup.find_all("img"):
            img = img.get('src')
            if "jpg" in img:
                images.append(img)
            else:
                continue
        return images
    except:
        print("ERROR WHILE GETING IMAGE LINKS")


def download_images(image_url):
    """download all the images from there url to local file system"""
    try:
        counter = 0
        for i in image_url:
            urllib.request.urlretrieve(
                str(i), f"image_download/image{counter}.jpg")
            counter += 1
    except:
        print("ERROR while downloading images")


if __name__ == "__main__":
    # raw_html = send_request("https://www.crunchyroll.com/videos/anime")
    # print("LENGTH OF HTML", len(raw_html))
    # save_to_file(raw_html)
    img_links = get_all_img_links()
    download_images(img_links)
