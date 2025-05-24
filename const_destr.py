class logger:
    def __init__(self):
        print("object created")

    def __del__(self):
        print("object destroyed")

if __name__ == "__main__":
    log = logger()
    