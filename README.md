# Service Monitor CLI

![License](https://img.shields.io/badge/license-MIT-green)

CLI tool for monitoring HTTP services with Telegram and Email notifications, retry logic, and configurable health checks.

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
- State-based alerts (anti-spam)
- Retry logic
- Configurable intervals and timeout
- Logging to file and console
- CLI interface with Click
- Graceful shutdown
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

- **monitoring/** — website checking logic
- **notifications/** — Telegram and email alerts
- **utils/** — logger configuration
- **monitor.py** — CLI entry point and orchestration

---

## Project Structure

```text
service-monitor/
├── logs/
│   └── monitor.log
├── monitoring/
│   └── checker.py
├── notifications/
│   ├── alerts.py
│   ├── telegram.py
│   └── email_alert.py
├── utils/
│   └── logger.py
├── .env.example
├── .gitignore
├── LICENSE
├── monitor.py
├── requirements.txt
└── README.md
```

---

## Installation

### 0. Requirements

- Python 3.10+
- Internet connection
- Telegram Bot Token
- SMTP email account

### 1. Clone repository

```bash
git clone https://github.com/D1tos/service-monitor.git

cd service-monitor
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file.

**Linux/macOS**

```bash
cp .env.example .env
```

**Windows PowerShell**

```powershell
Copy-Item .env.example .env
```

Then edit the `.env` file and replace the placeholder values with your own credentials.

> **Note:** Never commit your `.env` file or real credentials to the repository.

### 5. Edit the .env file

```env
TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=recipient@example.com
```

## Usage

### Monitor one website

```bash
python monitor.py --url https://google.com
```

### Monitor multiple websites

```bash
python monitor.py \
  --url https://google.com \
  --url https://github.com
```

### Custom interval

```bash
python monitor.py \
  --url https://google.com \
  --interval 5
```

### Custom timeout

```bash
python monitor.py \
  --url https://google.com \
  --timeout 3
```

### Disable Telegram alerts

```bash
python monitor.py \
  --url https://google.com \
  --no-telegram
```

## Retry Logic

Failed requests are retried automatically before marking a service as DOWN.

Default retry count: 3

## Logging

*Logs are automatically written to:*

```text
logs/monitor.log
```

*Example log output:*

```text
2025-08-05 12:00:00 | INFO | STATUS CHANGE: https://google.com -> DOWN
```

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

```text
CTRL + C
```

When stopped manually, the monitor writes a shutdown message to logs.

## Author

**Alexander Naumov**

GitHub: [D1tos](https://github.com/D1tos)

## License

This project is licensed under the [MIT License](LICENSE).
