from networking import Server

def main():
    MyObj = Server()
    
    MyObj.event_loop()
    
if __name__ == "__main__":
    main()