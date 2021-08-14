with open("day19.in") as f:
    data = f.read()

input_rules, messages = (x.splitlines() for x in data.split('\n\n'))
rules = dict(rule.split(": ") for rule in input_rules)


def valid_messages(rule: str):
    if '"' in rule:
        return set(rule[1])

    if '|' in rule:
        return set(m for r in rule.split(' | ') for m in valid_messages(r))

    if ' ' in rule:
        left, right = [valid_messages(x) for x in rule.split(' ', 1)]
        return set(x + y for x in left for y in right)
    
    return valid_messages(rules[rule])

#part 1
all_valid_messages = valid_messages(rules['0'])
print(sum(message in all_valid_messages for message in messages))

# part 2
valid_messages_for_31 = valid_messages(rules['31'])
valid_messages_for_42 = valid_messages(rules['42'])

print(len(valid_messages_for_31))
print(len(valid_messages_for_42))
print(set.intersection(valid_messages_for_31, valid_messages_for_42))
print(set(len(x) for x in valid_messages_for_31))
print(set(len(x) for x in valid_messages_for_42))
# all valid messages in there are 8 chars long and the two sets are totally different

count = 0
for message in messages:
    sections = [message[i:i + 8] for i in range(0, len(message), 8)]
    pos = 0
    count_42 = 0
    count_31 = 0
    while pos < len(sections) and sections[pos] in valid_messages_for_42:
        pos += 1
        count_42 += 1
    while pos < len(sections) and sections[pos] in valid_messages_for_31:
        pos += 1
        count_31 += 1
    if pos == len(sections) and 0 < count_31 < count_42:
        count += 1
    
print(count)