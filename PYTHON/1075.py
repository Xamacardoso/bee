def main():
    n = int(input())
    count = 1
    while count < 10000:
        print(count) if count%n == 2 else 1
        count+=1
    
main()