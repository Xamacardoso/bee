def main():
    n = int(input())
    count = 1
    
    while count<=n:
        print(f'{count} {count**2} {count**3}')
        count+=1

main()