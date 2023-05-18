from numpy import log2

def main():
  x = int(input("X: "))
  y = int(input("Y: "))

  print(f"X ^ Y = {x ** y}")
  print(f"log of X (base 2) = {log2(x)}")

if __name__ == "__main__":
  main()