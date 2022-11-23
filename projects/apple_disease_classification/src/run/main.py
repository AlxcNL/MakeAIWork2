#!/usr/bin/env python

# IMPLEMENT RUNNABLE CODE INSIDE THIS MAIN 
def main():
    if __name__ == "__main__": 
        print("File_run is being run directly")
    else: 
        print("File_run is being imported")

print("File_run __name__ = %s" %__name__)

# DO NOT IMPLEMENT ANYTHING HERE
if __name__ == "__main__":
    main()  