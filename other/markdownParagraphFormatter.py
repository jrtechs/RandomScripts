"""
Jeffery Russell
2019-4-21

Simple program to reformat paragraphs in markdown text files
to follow a specific col limit.
"""

import os
import sys


def formatChunk(stringContent, charLimit):
    """
    Formats a markdown section with with a specific
    col limit. This only makes changes if the section is a
    paragraph and nothing else.

    The only guarantee for the input is that there
    are no lines which only contain a new line or space.

    :param stringContent: string of markdown chunk
    :param charLimit: max character limit
    :return: formatted string
    """
    if len(stringContent.strip(" ")) == 0:
        return ""
    elif not stringContent[0].isalpha():
        return stringContent
    result = ""
    line = ""
    stringContent = stringContent.replace("\n", " ")
    words = stringContent.split(" ")

    for word in words:
        if len(line) == 0 or len(line) + len(word) < charLimit:
            if not len(line) == 0:
                line = line + " "
            line = line + word
        else:
            result = result + line + "\n"
            line = word
    if line != "":
        result = result + line + "\n"
    return result


def writeToFile(fileName, content):
    """
    Writes to a file, overwriting the existing
    output.
    :param fileName:
    :param content:
    :return:
    """
    f = open(fileName, "w+")
    f.write(content)
    f.close()


def wrapMarkdownParagraphsToColLimit(fileName, charLimit):
    """
    Breaks apart a markdown file into chunks. A chunks are
    separated by a blank lines. Each chunk is then
    rendered according to our 80 char rules defined
    in the formatChunk section.
    :param fileName:
    :param charLimit:
    :return:
    """
    result = ""
    tempResult = ""
    inCodeBlock = False

    with open(fileName) as file:
        for line in file:

            if line.startswith("```"):
                inCodeBlock = not inCodeBlock
                result = result + line
            elif inCodeBlock:
                result = result + line
            elif line.strip(" ") == "\n":
                result = result + formatChunk(tempResult, charLimit)
                tempResult = ""
                result = result + "\n"
            else:
                tempResult = tempResult + line

    if tempResult != "":
        result = result + formatChunk(tempResult, charLimit)
    return result


def print_usage():
    """
    Prints script usage.
    :return:
    """
    print("Usage: file name -t (optional)")
    print("\t-p simply prints the formatted output.")
    print("\tfile name -- runs the command overwriting the existing file.")


def main():
    """
    Checks command line input and calls the proper formatting
    functions.
    :return:
    """
    if len(sys.argv) > 1:
        fileName = os.getcwd() + "/" + sys.argv[1]
        if len(sys.argv) == 3 and sys.argv[2].lower() == "-p":
            print(wrapMarkdownParagraphsToColLimit(fileName, 70))
        else:
            writeToFile(fileName,
                        wrapMarkdownParagraphsToColLimit(fileName, 70))
    else:
        print_usage()


"""
Makes sure that other scripts don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        panic()
