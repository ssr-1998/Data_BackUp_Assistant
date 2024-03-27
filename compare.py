import os
import ast
import json
from datetime import datetime


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        super().__init__()
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


def timer(start_time=None):
    """Function to calculate total time taken:"""
    from datetime import datetime
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))


start_time = timer()

old_path = input("\nOld Scanned JSON File Path : ")
new_path = input("\nNew Scanned JSON File Path : ")

print("\nLoading Files...")

# old_path = "scanned_JSONs\D__Sample_for_Drive_Scan_26_03_2024__00_11_33.json"
# new_path = "scanned_JSONs\D__Sample_for_Drive_Scan_26_03_2024__00_35_01.json"

with open(old_path, "r") as f:
    old = ast.literal_eval(f.read())

with open(new_path, "r") as f:
    new = ast.literal_eval(f.read())

old_dict = my_dictionary()
for _path in old:
    old_dict.add(_path.get("path"), datetime.strptime(_path.get("last_modified_time"), "%d/%m/%Y %I:%M:%S"))

new_dict = my_dictionary()
for _path in new:
    new_dict.add(_path.get("path"), datetime.strptime(_path.get("last_modified_time"), "%d/%m/%Y %I:%M:%S"))

print("\nComparing File Entries...")

missing_paths = list(set(list(old_dict.keys())) - set(list(new_dict.keys())))
added_paths = list(set(list(new_dict.keys())) - set(list(old_dict.keys())))

updated_paths = []
for p in list(set(list(old_dict.keys())) - set(missing_paths)):
    old_m_time = old_dict.get(p)
    new_m_time = new_dict.get(p)
    if new_m_time > old_m_time:
        updated_paths.append(p)

comparison = my_dictionary()
comparison.add("MISSING", missing_paths)
comparison.add("ADDED", added_paths)
comparison.add("UPDATED", updated_paths)

file = "Comparison Results for:\n\tOld File - {}\n\tNew File - {}\n\n\n".format(
    old_path, new_path
)

print("\nResults (No. of Entries):\n\tMISSING - {}\n\tADDED - {}\n\tUPDATED - {}\n\nStoring Scanned Entries...".
      format(len(missing_paths), len(added_paths), len(updated_paths)))

file += str(json.dumps(comparison, indent=4)) + "\n"

now_time = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")

if not os.path.exists("comparison_results"):
   os.mkdir("comparison_results")

with open("comparison_results/cr_{}.txt".format(now_time), "w") as f:
    f.write(file)

# print("Missing - {}\n\nAdded - {}\n\nUpdated - {}".format(missing_paths, added_paths, updated_paths))
print("\nResults are Stored in `comparison_results/cr_{}.txt`".format(now_time))

timer(start_time)
