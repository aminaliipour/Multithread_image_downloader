import multiprocessing, time, json, os
import threads.TasnimThread as TasnimTh


class TasnimProcess(multiprocessing.Process):
    id = 0

    def __init__(self, id, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.id = id



    def open_links_file(self):
        with open("./links/tasnim.json", "r") as f:
            urls = f.read()
            urls = json.loads(urls)
            f.close()
        return urls

    def run(self):
        print('process id :', self.id)
        if os.path.exists("links/tasnim/"):
            urls = self.open_links_file()
            threads = []
            th_id = 1
            for url in urls:
                thread = TasnimTh.FararuThread(th_id, url, TasnimTh.TYPES.IMAGE)
                thread.start()
                threads.append(thread)
                th_id+=1
                time.sleep(1)
            for thread in threads:
                thread.join()
        # runs if Fararu urls file does not exists
        else:
            TasnimTh.TasnimThread(0, "https://www.tasnimnews.com/", TasnimTh.TYPES.URLS)
            return