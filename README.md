# RTSPGrab

This script is a small custom solution to wanting to grab a screenshot from a set of RTSP (Real Time Streaming Protocol) enabled CCTV cameras at given points during the day. The script itself does not handle the scheduling, as this is left to a more appropriate tool such as `crontab`.

The script expects `username`, `password`, `camServerAddress` and `cameras` variables to exist and be provided by an accompanying `rtspgrab_config.json` file (example provided).

For each provided camera in `cameras`, the script will generate a nested folder inside the outer `RTSPGrab` folder in the user's home directory if one does not already exist. To that folder, a timestamped screengrab will be added for every subsequent execution.

## Config file:

An example of the config file and its format:

```json
  {
    "username": "camera_username",
    "password": "camera_password123",
    "camServerAddress": "cameras.domain.example",
    "cameras": [
      "Garden",
      "Porch",
      "Garage"
    ]
  }
```
