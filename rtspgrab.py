#!/usr/bin/env python3

import json
import os
import cv2

def main():
  # run file & folder check
  rootFolderPath = os.path.join(os.path.expanduser('~'), "RTSPGrab")
  if(not os.path.isdir(rootFolderPath)):
    os.mkdir(rootFolderPath)
  else:
    print('Folder exists')

if __name__ == '__main__':
    main()