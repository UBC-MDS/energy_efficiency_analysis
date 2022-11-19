# +
"""Downloads data excel data from the web to a local filepath as either a csv  file format.
Usage: src/down_data.py  --url=<url> --out_file=<out_file>
Options:

--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""
  
from docopt import docopt
import requests
import os
import pandas as pd

opt = docopt(__doc__)

def main(url, out_file):
  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)
    
  data = pd.read_excel(url, header=0)
  
  try:
      data.to_csv(out_file, index = False)
  except:
      os.makedirs(os.path.dirname(out_file))
      data.to_csv(out_file, index = False)

if __name__ == "__main__":
  main( opt["--url"], opt["--out_file"])
# -

