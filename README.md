# Service Monitor with Telegram Alerts

## Description
CLI-based service monitoring tool for tracking website and API availability with Telegram and Email alerts, retry logic, logging and fallback error handling.

Designed to prevent alert spam by tracking service state.

Even if Telegram API is unavailable, the monitor continues to work and logs status changes to console.

## Features

- HTTP status monitoring
- State-based alerts (no spam)
- Telegram notifications
- Email notifications
- Multi-channel alerts
- Retry system
- Error handling
- Works without Telegram API (fallback mode)
- Multiple URL monitoring
- Custom check interval
- CLI support with Click
- Logging to file and console
- Modular helper-based architecture
- Centralized alert handling

## Use Cases

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
- smtplib
- Telegram Bot API

## Architecture

- CLI interface via Click
- HTTP monitoring with requests
- Retry-based request handling
- Telegram notification system
- Email notification system
- Centralized alert dispatcher
- Helper-based monitoring architecture
- Logging subsystem
- Fallback behavior when notification services are unavailable

## Project Structure

service-monitor/
├── logs/
│   └── monitor.log
├── .env
├── .gitignore
├── monitor.py
├── requirements.txt
└── README.md

## Core Functions

| Function | Description |
|---|---|
| `check_website()` | Checks website availability with retry logic |
| `send_telegram_message()` | Sends Telegram alerts |
| `send_email()` | Sends email alerts |
| `send_alert()` | Centralized alert dispatcher |
| `build_status_message()` | Builds alert messages |
| `log_status_change()` | Logs service status changes |

## Reliability Features

- Retry logic for failed requests
- Graceful fallback when Telegram is unavailable
- Email notifications continue working independently
- Logging to both console and file

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

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=your_email@gmail.com

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

### Disable Telegram alerts (optional for alerts)

python monitor.py \
  --url https://google.com \
  --no-telegram

## Logging

*Logs are automatically written to:*

logs/monitor.log

*Example log output:*

2025-08-05 12:00:00 | INFO | STATUS CHANGE: https://google.com -> DOWN

## Notifications

The monitor supports:

- Telegram alerts
- Email alerts

Alerts are only sent when service status changes.

## Alert Examples

### Service is down

🚨 https://example.com is DOWN

### Service recovered

✅ https://example.com is BACK UP

## Author

GitHub: https://github.com/D1tos
