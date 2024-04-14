from bs4 import BeautifulSoup
import requests
import os
import threading

web = requests.get("https://fararu.com")
soup = BeautifulSoup(web.content, "html.parser")
images = soup.find_all("img")

extensions = ["jpg", "bmp", "png", "jpeg"]

with open("links.txt", "wt", encoding="utf8") as f1:
    for image in images:
        src = str(image["src"])
        ext = src.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        if ext in extensions and "http" in image['data-src']:
            f1.write(image["data-src"] + "\n")



if not os.path.exists("files/"):
    os.mkdir("files")
if not os.path.exists("files/fararu/"):
    os.mkdir("files/fararu/")


class Thread_web(threading.Thread):
    link = ""

    def __init__(self, link, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.link = link

    def run(self):
        ext = self.link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        name = self.link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[0]
        content = requests.get(self.link.strip()).content
        # name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        with open(n := "files/fararu/" + name + "." + ext, "wb") as file:
            file.write(content)
            print(n)
        print(self.link)


with  open('links.txt', "rt") as links:
    threads = []
    for link in links:
        th = Thread_web(link.strip())
        th.start()
        threads.append(th)
    for thread in threads:
        thread.join()
