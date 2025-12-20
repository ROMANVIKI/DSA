import math
import os
import random
import re
import sys


def acmTeam(topic, n, m):
    # Write your code here
    num_attendees, num_topics =  n, m

    max_topics_known = 0
    num_teams_with_max_topics = 0

    for i in range(num_attendees - 1):
        for j in range(i+1, num_attendees):
            # print(i, j)
            topics_known = sum(1 for k in range(num_topics) if topic[i][k] == '1')

            if topics_known > max_topics_known:
                max_topics_known = topics_known
                num_teams_with_max_topics = 1

            elif topics_known == max_topics_known:
                num_teams_with_max_topics += 1

    return [max_topics_known, num_teams_with_max_topics]    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic, n, m)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
