# Service Monitor with Telegram Alerts

## Description
CLI-based service monitoring tool for tracking website and API availability with Telegram alerts and fallback console logging.

Designed to prevent alert spam by tracking service state.

Even if Telegram API is unavailable, the monitor continues to work and logs status changes to console.

## Features

- HTTP status monitoring
- Multiple URL monitoring
- Telegram notifications
- State-based alerts (no spam)
- File logging
- Console logging
- Error handling
- Automatic logs directory creation
- Custom check interval
- Configurable request timeout
- CLI support with Click
- Works without Telegram API (fallback mode)
- Retry system
- Resilient monitoring behavior

##Use Cases

This tool can be used to monitor:

- websites
- APIs
- internal services
- development environments
- self-hosted services

and receive instant alerts in case of downtime.

## Tech Stack

- Python
- requests
- python-dotenv
- click
- logging
- Telegram Bot API

## Architecture

- CLI interface via Click
- HTTP monitoring with requests
- Telegram notification system
- Logging subsystem
- Fallback behavior when Telegram is unavailable
- Retry-based request handling

## Project Structure

service-monitor/
├── logs/
│ └── monitor.log
├── .env
├── .gitignore
├── monitor.py
├── requirements.txt
└── README.md

## Installation

### 1. Clone repository

git clone https://github.com/D1tos/service-monitor.git
cd service-monitor

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create .env file

TOKEN=your_telegram_token
CHAT_ID=your_chat_id

## Usage

### Monitor one website

python monitor.py --url https://google.com

### Monitor multiple websites

python monitor.py \
  --url https://google.com \
  --url https://github.com

### Custom interval

python monitor.py \
  --url https://google.com \
  --interval 5

### Custom timeout

python monitor.py \
  --url https://google.com \
  --timeout 3

### Disable Telegram alerts

python monitor.py \
  --url https://google.com \
  --no-telegram

## Logging

*Logs are automatically written to:*

logs/monitor.log

*Example log output:*

2025-08-05 12:00:00 | INFO | STATUS CHANGE: https://google.com -> DOWN

## Alert Examples

### Service is down

🚨 https://example.com is DOWN

### Service recovered

✅ https://example.com is BACK UP

## Author

GitHub: https://github.com/D1tos
