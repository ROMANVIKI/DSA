def designerPdfViewer(h, word):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict_alphabets = {alphabets[i]: h[i] for i in range(len(alphabets))}

    max_val = 0
    for w in word:
        value_key = dict_alphabets[w]
        if value_key > max_val:
            max_val = value_key

    area = max_val * len(word)
    
    return area



    # Write your code here

if __name__ == '__main__':
    

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)


    print(result)