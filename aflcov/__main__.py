import logging
logging.getLogger('axt.aflcovexplorer').setLevel(logging.INFO)

from . import AflCovCFGExplorerCLI

def main():
    explorer = AflCovCFGExplorerCLI()
    explorer.run()
    
if __name__ == '__main__':
    main()
