import os
import json
from datetime import datetime


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


def scanner(path, now_time):
  """
  Scans specified Drive/Directory & Returns a List of JSON Objects representing the files and 
  sub-direcotries in the Drive/Directory.

  Paramerters:
    path: str
    now_time: str  (this value will only be used for storing the log file in logs directory in case the `scanner` faces any error during its runtime.)
  """

  files = []
  logs = []
  for root, dirs, file_names in os.walk(path):
    for file_name in file_names:
      file_path = os.path.join(root, file_name)
      if ".ipynb_checkpoints" in file_path:
        pass
      else:
        try:
          file_info = {
            "name": file_name,
            "path": file_path,
            "last_modified_time": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%d/%m/%Y %I:%M:%S")
          }
        except FileNotFoundError:
            logs.append(file_path)
        files.append(file_info)

  if len(logs) > 0:
    if not os.path.exists("logs"):
      os.mkdir("logs")
    
    log_content = {}
    log_content["FileNotFoundError"] = logs

    with open("logs/logs_{}.json".format(now_time), "w") as l:
       l.write(json.dumps(log_content, indent=4))
    
    print("\nEncountered Error for {} File Paths while Scanning.\nAll {} are skipped & thus you can find information about them from `logs/logs_{}.json`.".format(len(logs), len(logs), now_time))

  return json.dumps(files, indent=4)


start_time = timer()

now_time = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")

drive_path = input("\nDrive/Directory Path to Scan : ")

print("\nScanning...")

json_data = scanner(drive_path, now_time)

print("\nFile Paths Successfully Scanned - {}\n\nStoring Scanned Entries...".format(len(json_data)))

_filename = drive_path.replace(":", "").replace("/", "__")

if not os.path.exists("scanned_JSONs"):
   os.mkdir("scanned_JSONs")

with open("scanned_JSONs/{}_{}.json".format(_filename, now_time), "w") as f:
   f.write(json_data)

print("\nResults are Stored in `scanned_JSONs/{}_{}.json`".format(_filename, now_time))

timer(start_time)
