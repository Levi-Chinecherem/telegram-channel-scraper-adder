# Channel Scraper and Adder Bot

This Telegram bot allows you to scrape members from Telegram channels and add them to other channels using the Telegram API. It provides a convenient way to gather members from one channel and add them to another channel.

## Features

- Scrapes members from Telegram channels
- Adds scraped members to target channels
- Supports adding members by username or ID
- Handles flood errors and user privacy restrictions
- Easy-to-use CSV file integration


## Libraries Used

This bot is built using several powerful libraries:

### Telethon

- **Description**: Telethon is a powerful Python library for interacting with the Telegram API. It simplifies the process of automating Telegram-related tasks and provides extensive functionality for building Telegram bots and applications.
- **Features**: Telethon offers features such as Telegram API integration, user and chat management, message handling, scraping and data retrieval capabilities, and customization options.
- **Website**: [Telethon](https://github.com/LonamiWebs/Telethon)

### csv

- **Description**: The `csv` library in Python provides functionality for reading from and writing to CSV files. It simplifies the process of handling CSV data, making it easier to store and retrieve structured data.
- **Features**: The `csv` library offers functions for reading CSV files, writing data to CSV files, and manipulating CSV data using various options and parameters.
- **Documentation**: [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

### traceback

- **Description**: The `traceback` module in Python provides a convenient way to extract and format stack traces. It is commonly used for debugging purposes to print detailed information about exceptions and errors.
- **Features**: The `traceback` module offers functions to extract and format stack traces, including the ability to print the traceback to the console or store it in a variable for further processing.
- **Documentation**: [traceback — Print or Retrieve a Stack Trace](https://docs.python.org/3/library/traceback.html)

### time

- **Description**: The `time` module in Python provides functions for working with time-related operations, such as getting the current time, pausing the execution of a program, or measuring elapsed time.
- **Features**: The `time` module offers functions to retrieve the current time, delay program execution for a specified duration, and convert between different time representations.
- **Documentation**: [time — Time access and conversions](https://docs.python.org/3/library/time.html)

### random

- **Description**: The `random` module in Python provides functions for generating random numbers, selecting random elements, shuffling sequences, and other randomization operations.
- **Features**: The `random` module offers functions to generate random numbers within a specified range, select random elements from a sequence, shuffle the order of elements, and perform various randomization tasks.
- **Documentation**: [random — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)

These libraries play a crucial role in the functionality and implementation of the bot. They provide essential features for interacting with the Telegram API, handling CSV data, managing exceptions, working with time-related operations, and performing randomization tasks.


## Prerequisites

Before using the bot, make sure you have the following:

- Telegram API credentials (API ID and API Hash)
- Python 3 installed on your machine
- Necessary Python packages (specified in the requirements.txt file)

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/Levi-Chinecherem/telegram-channel-scraper-adder.git

2. Install the required Python packages using pip.
pip install -r requirements.txt

3. Update the configuration variables in the script.
Replace 'YOUR_API_ID' with your Telegram API ID.
Replace 'YOUR_API_HASH' with your Telegram API hash.
Replace 'YOUR_PHONE_NUMBER' with your phone number.

## Usage
1. Run the channel scraper to generate CSV files containing the scraped members. Make sure you have joined the target channel before running the scraper.

python scraper_channel.py

2. Run the channel adder to add the scraped members to the target channels. Select the CSV files and the target channel(s) to add members to.

python adder_channel.py

3. Follow the prompts to select the CSV files and target channel(s) based on the provided options.

4. The script will start adding members to the target channel(s) based on the selected mode (username or ID). It will handle errors such as flood errors and user privacy restrictions.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please submit an issue or a pull request.

## Disclaimer
This bot is provided as-is, without any warranty. Use it responsibly and at your own risk.

## Credits
The original scraper and adder bot code: @Levi-Chinecherem

## License
This project is licensed under the MIT License.


Hope this helps! Let me know if you need further assistance: telegram @SemanticDev.
