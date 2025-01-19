
# YouTube Chat in Minecraft
### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Additional Documentation](#additional-documentation)
- [License](#license)
- [Issues and Improvements](#issues-and-improvements)
- [Known Bugs](#known-bugs)
- [Contribution](#contribution)

## Overview
**Chat.py** is a Python script that bridges YouTube live chat with Minecraft chat. This integration allows players in Minecraft to view YouTube chat messages from a YouTube live stream in real time.

## Features
- **Real-time Chat Integration:** Fetch live chat messages from YouTube and display them in Minecraft.
- **Command Filtering:** Automatically ignores messages starting with `!` to keep the chat relevant and clean.
- **Customizable:** Replace the default YouTube video ID with any live stream you choose.

## Installation Guide
Before you begin, ensure you have the following installed:
- **Python 3.7** or higher.
- Libraries:
  - `pytchat`
  - `minescript`

1. Install missing libraries using `pip`:

`pip install pytchat minescript`

2. Replace the default **YouTube video ID** in the script with your live stream video ID on line 27:

`video_id = "your_video_id_here"`

- **Note**: Your video ID is found in the URL: youtube.com/live/**WRb7TC2k1cQ**

3. Download and install Minescript in your Minecraft modpack.

https://modrinth.com/mod/minescript

## Usage
1. Ensure your Minecraft has the Minescript mod installed and has at least run once to generate the mod folders.

2. Download and place the `chat.py` script in the newly generated `minescript` folder.

3. Start Minecraft, open the chat window, and type the following command to run the script: `\chat`

4. It should then say **"Starting YouTube Chat..."** and you'll be able to start seeing YouTube live chat messages in Minecraft.

## Additional Documentation

pytchat: https://github.com/taizan-hokuto/pytchat

Minescript: https://minescript.net/docs/

**Watch me code it live!**
https://www.youtube.com/watch?v=EorgBTJj_mc

## License
This project is licensed under the Creative Commons Attribution 4.0 International License.

**You are free to:**
- Share — copy and redistribute the material in any medium or format.
- Adapt — remix, transform, and build upon the material.

**Under the following terms:**
- Attribution — You must give appropriate credit and indicate if changes were made.

See the LICENSE file for more details.

## Issues and Improvements
If you find an issue or would like to submit an improvement to this project, please use the issues tab above to submit an issue.

## Known Bugs
After about 30-60 minutes of runtime, the code will timeout and stop running.

You can see this happen in my latest live stream test for this code: https://www.youtube.com/watch?v=qGGrQaWRiuM

## Contribution
Thank you for visiting this repository! Contributions are optional but always appreciated. You can help by finding bugs, suggesting improvements, opening issues, submitting pull requests, or starring the repository. Donations are also welcome to support the project. Your involvement means a lot—thank you!

**Support Options:**
- Send a donation via [Cash App](https://cash.app/$MisterZen01)
- Become a YouTube Member starting @ $0.99/mo
- Donate through YouTube Super Chat

### Thank you for using Chat.py!
