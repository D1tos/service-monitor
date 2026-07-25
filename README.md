# Service Monitor CLI

## Description

CLI-based service monitoring tool for tracking website and API availability with Telegram and Email alerts, retry logic, logging, and modular architecture.

The application monitors multiple services, detects status changes, and sends notifications only when service state changes.

Built as a modular Python application with separated monitoring, notification, and logging layers.

---

## Features

- HTTP status monitoring
- Multiple URL monitoring
- Telegram notifications
- Email notifications
- Multi-channel alert system
- Retry logic for failed requests
- Logging to file and console
- CLI interface with Click
- Configurable intervals and timeout
- State-based alerts (anti-spam logic)
- Graceful shutdown support
- Environment-based configuration
- Modular architecture

---

## Use Cases

This tool can be used to monitor:

- websites
- APIs
- internal services
- development environments
- self-hosted services

and receive instant alerts in case of downtime.

---

## Tech Stack

- Python
- requests
- click
- python-dotenv
- logging
- smtplib
- EmailMessage
- Telegram Bot API

---

## Architecture

Project uses modular architecture with separated responsibilities:

- monitoring/ → website checking logic
- notifications/ → Telegram and Email alerts
- utils/ → logger configuration
- monitor.py → CLI entry point and orchestration

---

## Project Structure

service-monitor/

├── logs/
│   └── monitor.log
│
├── monitoring/
│   └── checker.py
│
├── notifications/
│   ├── alerts.py
│   ├── telegram.py
│   └── email_alert.py
│
├── utils/
│   └── logger.py
│
├── .env
├── .gitignore
├── monitor.py
├── requirements.txt
└── README.md

---

## Installation

### 1. Clone repository

git clone https://github.com/D1tos/service-monitor.git

cd service-monitor

### 2. Create virtual environment

python3 -m venv .venv

source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt


### 4. Copy .env.example file
#### Bash
cp .env.example .env

#### PowerShell
Copy-Item .env.example .env

#### fill in a file
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

### Disable Telegram alerts

python monitor.py \
  --url https://google.com \
  --no-telegram

## Retry Logic

Failed requests are retried automatically before marking a service as DOWN.

Default retry count: 3

## Logging

*Logs are automatically written to:*

logs/monitor.log

*Example log output:*

2025-08-05 12:00:00 | INFO | STATUS CHANGE: https://google.com -> DOWN

## Notifications

Supported notification channels:

- Telegram Bot API
- Email (SMTP)

Alerts are sent only when service status changes.

## Alert Examples

### Service is down

🚨 https://example.com is DOWN

### Service recovered

✅ https://example.com is BACK UP

## Graceful Shutdown

The application supports safe shutdown using:

CTRL + C

When stopped manually, the monitor writes a shutdown message to logs.

## Version

Current version: v1.0.0

## Author

GitHub:

https://github.com/D1tos
