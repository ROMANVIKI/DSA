def  reportSpam(message, bannedWords):
    total_occurances = 0
    banned_set = set(bannedWords)
    for message_str in message:
        if message_str in banned_set:
            total_occurances += 1

        if total_occurances >= 2:
            return True
    return  False  


print(reportSpam(message=["hello","world","leetcode"], bannedWords=["hello","world","leetcode"]))

