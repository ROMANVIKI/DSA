

def migratoryBirds(arr):
    frequency = {}
    # Count the frequency of each bird type
    for bird_type in arr:
        if bird_type in frequency:
            frequency[bird_type] += 1
        else:
            frequency[bird_type] = 1
    
    # Find the type with the highest frequency
    max_frequency = max(frequency.values())
    
    # Find the smallest type ID with the highest frequency
    most_frequent_type = min([bird_type for bird_type, freq in frequency.items() if freq == max_frequency])
    
    return most_frequent_type
    
    
    
    
    
    
    
    
    

        
    # Write your code here
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
