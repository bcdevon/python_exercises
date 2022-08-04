short_texts = ["hello there", "Good bye", "my name is"]
longer_text = ["my name is brady", "I love programming", "I love python Java not so much"]
sent_messages = []


def show_message(texts):
    for text in texts:
        print(text)


def send_messages(short_texts, sent_messages):
    while short_texts:
        sending_message = short_texts.pop()
        print(sending_message)
        sent_messages.append(sending_message)


send_messages(short_texts, sent_messages)
print(short_texts)
print(sent_messages)
