#!/usr/bin/env python3

import json
import os
import sys
import cv2
from time import sleep
from datetime import datetime

CONFIG_FILENAME = 'rtspgrab_config.json'


def main(username: str, password: str, address: str, cameras: list[str]):
    """
    Main script function. For each camera provided, this function takes a screenshot of the latest frame and saves
    it as a timestamped file in the correspondingly named folder in the user's home directory. These files and the
    named folders are nested inside the outer "RTSPGrab folder"

    :param username: The username to access the cameras
    :param password: The password to access the cameras
    :param address: The address of the remote camera server
    :param cameras: Array of camera names
    :return: Nothing
    """
    root_folder_path = get_root_directory()

    for c in cameras:
        cap = cv2.VideoCapture(f"rtsp://{username}:{password}@{address}:554/cam/realmonitor?channel={c}&subtype=0")

        # allow a short buffer period to account for network latency
        sleep(2)

        filename = f"cam_{c}_{datetime.now().day}-{datetime.now().month}"
        ret, img = cap.read()
        cv2.imwrite(os.path.join(os.path.join(root_folder_path, c), f"{filename}.jpg"), img)


def pre_checks() -> tuple[str, str, str, list[str]]:
    """
    This function runs a set of checks that need to pass before the main script runs. These checks include verifying
    that the correct folder structure exists, and that a username, password and camera server domain have been provided.

    If all checks pass, the data read from the config is returned in a tuple of the form:
        (username, password, camera address, cameras[])

    :return: A tuple containing verified config data
    """
    root_folder_path = get_root_directory()
    config = {}

    # make the root directory if it does not already exist
    if not os.path.isdir(root_folder_path):
        os.mkdir(root_folder_path)

    # read the config into memory. Exit with error if it does not exist
    if os.path.isfile(f'.{os.sep}{CONFIG_FILENAME}'):
        with open(f'.{os.sep}{CONFIG_FILENAME}', 'r') as f:
            config = json.load(f)
    else:
        print(f'Could not find {CONFIG_FILENAME}. Exiting...')
        sys.exit()

    username = config['username']
    password = config['password']
    address = config['camServerAddress']
    cameras = config['cameras']

    # check that an output folder exists for each requested camera
    if len(cameras):
        for camera in cameras:
            if not os.path.exists(os.path.join(root_folder_path, camera)):
                print(f"Output folder for camera {camera} does not exist. Creating...")
                os.mkdir(os.path.join(root_folder_path, camera))
            else:
                print(f"Output folder for camera {camera} exists. Skipping...")
    else:
        print("No cameras found in config. Exiting...")
        sys.exit()

    # check that a username, password and server address have been provided
    if len(username) and len(password) and len(address):
        return username, password, address, cameras
    else:
        print("Username, password or address not found in config. Exiting...")
        sys.exit()


def get_root_directory() -> str:
    """
    Gets the root directory for RTSBGrab to use to store its files
    :return: The user's home dir (~) followed by a folder named "RTSPGrab"
    """
    return os.path.join(os.path.expanduser('~'), 'RTSPGrab')


if __name__ == '__main__':
    """Entry point"""
    main(*pre_checks())
