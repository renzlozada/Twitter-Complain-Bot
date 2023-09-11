# Internet Speed Complaint Bot

This Python script automates the process of checking your internet speed and sending a complaint to your Internet Service Provider (ISP) if the speed falls below a certain threshold. The script uses Selenium to run a speed test, collect the results, and tweet a complaint to your ISP on Twitter.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium: `pip install selenium`

## Usage

1. Clone this repository to your local machine.

2. Install the required dependencies mentioned in the "Prerequisites" section.

3. Set your Twitter login credentials as environment variables:
   - `my_email`: Your email address associated with your Twitter account.
   - `my_pass`: Your Twitter account password.
   - `my_phone`: Your phone number associated with your Twitter account.

4. Run the script:
   ```bash
   python main.py

- The script will:
  - Check your internet speed.
  - If the download and upload speeds are below a certain threshold (e.g., 100 Mbps), it will log in to your Twitter account and send a complaint tweet to your ISP.
  - If the speeds are above the threshold, it will indicate that your internet speed is fine.

## Configuration

You can customize the threshold speed in the script by modifying the condition in the `main.py` file:

```python
if complain_bot.down < 100 and complain_bot.up < 100:
    complain_bot.tweet_at_provider()
else:
    print("Internet speed is fine. No need to complain")
    exit()

## Disclaimer

**This script is for educational purposes only.** Use it responsibly and ensure compliance with Twitter's terms of service. Automated tweeting can violate Twitter's rules, so **exercise caution**.
