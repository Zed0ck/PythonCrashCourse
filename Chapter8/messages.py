def show_messages(messages):
    """Show all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Send messages to sent_messages list."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['Hello there!', 'How are you?', 'What is your favorite color?']
sent_messages = []
show_messages(messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
