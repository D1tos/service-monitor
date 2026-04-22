# Service Monitor with Telegram Alerts

## Description
Simple service monitoring tool that checks website availability and sends alerts to Telegram when status changes.

## Features
- HTTP status monitoring
- State-based alerts (no spam)
- Telegram notifications
- Error handling

## Tech Stack
- Python
- requests
- Telegram Bot API

## How to run

1. Install dependencies:
pip install requests

2. Set your TOKEN and CHAT_ID in monitor.py

3. Run:
python monitor.py

## Example

If service goes down:
🚨 https://example.com is DOWN

If service recovers:
✅ https://example.com is BACK UP
