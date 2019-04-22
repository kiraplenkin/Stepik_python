with open('text.txt', 'r') as f, open('output.txt', 'w') as w:
    text = []
    for line in f:
        text.append(line.strip('\n'))

    new_text = text[::-1]
    for i in range(len(text)):
        w.write(new_text[i]+'\n')
