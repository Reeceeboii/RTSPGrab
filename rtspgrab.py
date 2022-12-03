#!/usr/bin/env python3

import json
import os
import sys
import cv2

CONFIG_FILENAME = 'rtspgrab_config.json'

def main(username: str, password: str, cams: list[str]):
  pass

# config that is ran before the main script is kicked off
def pre_config():
  rootFolderPath = os.path.join(os.path.expanduser('~'), 'RTSPGrab')
  config = {}

  # make the root directory if it does not already exist
  if(not os.path.isdir(rootFolderPath)):
    os.mkdir(rootFolderPath)

  # read the config into memory. Exit with error if it does not exist
  if(os.path.isfile(f'.{os.sep}{CONFIG_FILENAME}')):
    with open(f'.{os.sep}{CONFIG_FILENAME}', 'r') as f:
      config = json.load(f)
  else:
    print(f'Could not find {CONFIG_FILENAME}. Exiting...')
    sys.exit()

  # check that output folder exists for each requested camera
  if(len(config.cameras)):
    for camera in config.cameras:
      if(os.pa)
  else:
    print("No cameras found in config. Exiting...")
  
if __name__ == '__main__':
  pre_config()
  main()