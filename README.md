
# Chat.py: YouTube Chat in Minecraft
### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Additional Documentation](#additional-documentation)
- [License](#license)
- [Issues and Improvements](#issues-and-improvements)
- [Contribution](#contribution)

## Overview
**Chat.py** is a Python script that bridges YouTube live chat with Minecraft chat. This integration allows players in Minecraft to view YouTube chat messages from a YouTube live stream in real-time.

## Features
- **Real-time Chat Integration:** Fetch live chat messages from YouTube and display them in Minecraft.
- **Command Filtering:** Automatically ignores messages starting with `!` to keep the chat relevant and clean.
- **Customizable:** Replace the default YouTube video ID with any live stream of your choice.

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

Note: Your video ID is found in the URL: www.youtube.com/live/**WRb7TC2k1cQ**

3. Download and install Minescript in your Minecraft modpack

https://modrinth.com/mod/minescript


## Usage
1. Make sure you put the script (chat.py) in the correct folder. Minescript will generate a folder once it is ran once with the mod installed. You will then place the scripts in the new minescript folder

2. You will need to run the script through Minecraft using Minescript. To run any script you will have to do a Backslash (**\**), then write the name of the script, excluding the file extention (**.py**)

This is what the command should look like to run the chat.py script in Minecraft

`/chat`

3. It should then say **Starting YouTube Chat...** and start being able to see YouTube live chat messages in Minecraft

## Additional Documentation

pytchat: https://github.com/taizan-hokuto/pytchat

Minescript: https://minescript.net/docs/

**Watch me code it live!**
https://www.youtube.com/watch?v=EorgBTJj_mc

## License
See the LICENSE file for more details.

## Issues and Improvements
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above.

## Contribution
Thank you for visiting this repository! Contributions are optional but always appreciated. You can help by finding bugs, suggesting improvements, opening issues, submitting pull requests, or starring the repository. Donations are also welcome to support the project. Your involvement means a lot—thank you!

**Ways to support projects like this by donating:**
https://cash.app/$MisterZen01
Become a YouTube Member for $0.99
Donate through YouTube Super Chat

# Thank you for using Chat.py!
