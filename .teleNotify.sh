#!/bin/sh

# Get the token
BOT_URL="https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage"

# Set formatting
PARSE_MODE="Markdown"

# Check if all previous steps passed:
if [ $TRAVIS_TEST_RESULT -ne 0 ]; then
    build_status=" ❌ Failed 👎"
else
    build_status=" ✅ Succeeded 👍"
fi

# Send message function
send_msg () {
    curl -s -X POST ${BOT_URL} -d chat_id=$TELEGRAM_CHAT_ID \
        -d text="$1" -d parse_mode=${PARSE_MODE}
}

# Call send message with the message
send_msg "

\`----------------------------------------------------------------\`

Build *${build_status}!*

\`Repository 📦:  ${TRAVIS_REPO_SLUG}\`
\`Branch 🏷:      ${TRAVIS_BRANCH}\`

*Commit Msg 💭:*
_${TRAVIS_COMMIT_MESSAGE}_

[Job Log view here 👉](${TRAVIS_JOB_WEB_URL})

\`----------------------------------------------------------------\`
"

