# Data BackUp Assistant

## Overview

Data Backup Assistant is a Python-based script that assists with its capabilities of ***Scanning a Drive/Directory*** & providing a list of Files that are ***Added/Missing/Updated*** by ***Comparing*** the Old & New Scanned JSON files.

- ***scan.py***: For Scanning the specified Drive/Directory, it will return a `JSON` File that consists of a list of Python Dictionaries each containing the `name`, `path` & `last_modified_time` of each file present in the ***root or any level of sub-directory*** respectively.
- ***compare.py***: For Comparing the Old & New Scanned JSON Files, this script returns a `TXT` file containing both scanned file names with a Python Dictionary containing mainly 3 Keys i.e. `MISSING`, `ADDED` & `UPDATED` each consisting of a list of their respective file paths respectively.

Both files can directly be executed from the Terminal.

Sample Outputs from both the Files are available in their respective Output Directories i.e. `scanned_JSONs` & `comparison_results`.

## Inspiration

In today's fast growing world when we have adundance of data & for everyone the importance of their Personal System Data is something which is not measurable. It becomes extremely important for anyone to take Regular Backups for their Data.
We have plenty options of Platforms where we can keep our Data Backed Up Safely but still many prefer to keep Backups on their Other Personal Devices like External HDDs or SSDs, etc.
For them, it is difficult to keep a track of all the regular changes undergone in their System within the time spam of Backing Up.
So, for them ***Data BackUp Assistant*** can be quite helpful in creating a `Scanned JSON Image` of their `Drive/Directory` which will consist of all the available filepaths with their `Last Modified Date`.
Thus, helping them to create a JSON Image as soon as they complete a Backup such that the next time when they again want to take a backup they can simply again Scan the same Drive/Directory & then use `compare.py` to give a Comparison Result about all the latest changes which needs to be updated in the BackUp Drive.
Hope this helps & if there are any suggestions, then please do write them to me.
