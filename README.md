# TV Episode Names

## Description

A simple and ligthweight script used to search and find all the names to a TV show with the use of the API provided at TVMaze. The user can then choose to save the episode names to a text file for future reference. There is also a renamer script that can be used to rename the episodes so that they can be used as a linux rename command to rename media files. The renaming is done very specifically based on a strict naming pattern, so the use case may be very limited. You can however modify it to fit your needs. 

## Getting Started

Download all the dependecies, then run the app from a terminal e.g.: ```python tvmaze_api_episodes.py```
To create the renameing, first get the names and store them in a text file named ```names.txt``` which the first app does if you choose to save the output. Then run e.g.: ```python renamer.py``` then on a linux machine run the text file as a script from a terminal e.g.: ```./names.txt``` the media files should, in this example case, be stored in the same directory as the "names.txt" file.

### Dependencies

* Python (developed with v. 3.10.5 might work in all version from 2.7 and up)
