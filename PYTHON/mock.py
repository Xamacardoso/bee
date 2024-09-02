def main():
    ma = len(str(1000))
    for i in range(5):
        print("%{}d".format(ma) %i, end= '')

main();