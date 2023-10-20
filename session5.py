import math

def main():
    print("x\tsin(x)")

    for x in [i / 1000 for i in range(1001)]:
        sin_x = math.sin(x)
        print(f"{x:.4f}\t{sin_x:.4f}")

if __name__=="__main__":
    main()
