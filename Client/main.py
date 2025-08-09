from gui import Gui

def test():
    print("test")
def main():
    padding = {"x":5, "y": 5}
    ChatApp = Gui("darkly", (300,150), "Test App")
    name = ChatApp.entry()
    ChatApp.button("Show Name", lambda: print("Name entered:", name.get()))
    ChatApp.button("exit",command=ChatApp.root.destroy, padding=padding)
    ChatApp.run()

if __name__ == "__main__":
    main()