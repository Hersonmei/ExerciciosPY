"""Progress Bar Simulation, by Al Sweigart al@inventwithpython.com
A sample progress bar animation that can be used in other programs.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, module"""

import random, time

BAR = chr(9608)

def main():
    #Simular o download.
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # "Download" a random amount of "bytes":
        bytesDownloaded += random.randint(0, 100)

        # Get the progress bar string for this amount of progress:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # Don't print a newline at the end, and immediately flush the
        # printed string to the screen:
        print(barStr, end='', flush=True)


        time.sleep(0.2)
        # Print backspaces to move the text cursor to the line's start:
        print('\b' * len(barStr), end='', flush=True)
        print('\b' * len(barStr), end='', flush=True)

def getProgressBar(progress, total, barWidth=40):
    """Returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of a total amount."""

    progressBar = '' # The progress bar will be a string value.
    progressBar += '[' # Create the left end of the progress bar.

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'

    # Calculate the percentage complete:
    percentComplete = round(progress / total * 100)
    progressBar += ' ' + str(percentComplete) + '%' 

    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # Return the progress bar string.

if __name__ == '__main__':
    main()