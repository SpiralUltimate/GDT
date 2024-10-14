import os
import argparse
import sys
from GDLib import gdtInit


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("main_command", help="command for GDTools to use")
    parsed_args = argParser.parse_args()
    
    match parsed_args.main_command:
        case "init":
            gdtInit().initGodotEnvironment(os.path.abspath("."))
        
        case _:
            print("Error: invalid command entered\n")
            sys.exit(0)
            
if __name__ == "__main__":
    main()