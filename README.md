# Service Monitor with Telegram Alerts

## Description
Simple service monitoring tool that checks website availability and sends alerts to Telegram when status changes.

Designed to prevent alert spam by tracking service state.

Even if Telegram API is unavailable, the monitor continues to work and logs status changes to console.

## Use Case

This tool can be used to monitor:
- websites
- APIs
- internal services

and receive instant alerts in case of downtime.

## Features
- HTTP status monitoring
- State-based alerts (no spam)
- Telegram notifications
- Error handling
- Works without Telegram API (fallback mode)

## Tech Stack
- Python
- requests
- python-dotenv
- Telegram Bot API

## How to run

1. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

2. Install dependencies:
pip install -r requirements.txt

3. Create .env file:

TOKEN=your_token
CHAT_ID=your_chat_id
URL=https://example.com

4. Run:
python monitor.py

## Example

If service goes down:
- 🚨 https://example.com is DOWN

If service recovers:
- ✅ https://example.com is BACK UP

## Demo

Console output:
2026-01-01 12:00:00 | STATUS: UP

On failure:
🚨 https://example.com is DOWN

On recovery:
✅ https://example.com is BACK UP
