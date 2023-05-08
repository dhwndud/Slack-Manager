import os

DEFAULT_SYSTEM_TEXT = """
You are a bot in a slack chat room. You might receive messages from multiple people.
[당신은 슬랙 채팅 방의 Bots 입니다. 여러 사람 으로 부터 messages를 받을 수 있습니다.]
Format bold text *like this*, italic text _like this_ and strikethrough text ~like this~.
Slack user IDs match the regex `<@U.*?>`.
Your Slack user ID is <@{bot_user_id}>.
Each message has the author's Slack user ID prepended, like the regex `^<@U.*?>: ` followed by the message text.
"""
SYSTEM_TEXT = os.environ.get("OPENAI_SYSTEM_TEXT", DEFAULT_SYSTEM_TEXT)

DEFAULT_OPENAI_TIMEOUT_SECONDS = 30
OPENAI_TIMEOUT_SECONDS = int(
    os.environ.get("OPENAI_TIMEOUT_SECONDS", DEFAULT_OPENAI_TIMEOUT_SECONDS)
)

DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)

USE_SLACK_LANGUAGE = os.environ.get("USE_SLACK_LANGUAGE", "true") == "true"

SLACK_APP_LOG_LEVEL = os.environ.get("SLACK_APP_LOG_LEVEL", "DEBUG")

TRANSLATE_MARKDOWN = os.environ.get("TRANSLATE_MARKDOWN", "false") == "true"
