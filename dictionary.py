import sys
from CoreServices import DCSGetTermRangeInString, DCSCopyTextDefinition

def main():
    try:
        searchword = sys.argv[1]
    except IndexError:
        errmsg = 'You did not enter any terms to look up.'
        print(errmsg)
        sys.exit()

    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    print(dictresult)


if __name__ == '__main__':
    main()

