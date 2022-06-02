def to_camel_case(text):
    if text == "":
        return ""
    else:
        text = (text.replace('_', '-')).split('-')
        return text[0] + ''.join(x.title() for x in text[1:])