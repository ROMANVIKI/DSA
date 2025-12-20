import os
import math


#def squares(a, b):
#    sqrt_a = math.isqrt(a)
 #   sqrt_b = math.isqrt(b)
    
  #  if sqrt_a * sqrt_a < a:
   #     sqrt_a += 1
    
    #return max(0, sqrt_b - sqrt_a + 1)

def squares(a, b):
    v1=math.ceil(math.sqrt(a))
    v2=math.floor(math.sqrt(b))
    return v2-v1+1





if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')

    q = int(input().strip())

    for _ in range(q):
        a, b = map(int, input().split())
        result = squares(a, b)
        fptr.write(str(result) + '\n')

    fptr.close()
