import multiprocessing, time, json, os
import threads.Varzesh3Thread as Varzesh3Th


class Varzesh3Process(multiprocessing.Process):
    id = 0

    def __init__(self, id, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.id = id


    # open Fararu urls file
    def open_links_file(self):
        with open("./links/varzesh3.json", "r") as f:
            urls = f.read()
            urls = json.loads(urls)
            f.close()
        return urls

    def run(self):
        print('process id :', self.id)

        if os.path.exists("links/varzesh3/"):
            urls = self.open_links_file()
            threads = []
            th_id = 1
            for url in urls:
                thread = Varzesh3Th.Varzesh3Thread(th_id, url, Varzesh3Th.TYPES.IMAGE)
                thread.start()
                threads.append(thread)
                th_id+=1
                time.sleep(1)
            for thread in threads:
                thread.join()
        else:
            Varzesh3Th.Varzesh3Thread(0, "https://www.varzesh3.com/", Varzesh3Th.TYPES.URLS)
            return