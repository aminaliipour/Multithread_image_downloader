from processes import Varzesh3Process, FararuProcess, TasnimProcess


def main():
    process1 = Varzesh3Process()
    process2 = FararuProcess()
    process3 = TasnimProcess()

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()


if __name__ == "__main__":
    try:
        main()
    except:
        print("link not complete")
