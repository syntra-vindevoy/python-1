from datetime import datetime


def faq(n: int) -> int:
  if n > 3:
    return n

  return n * faq( n -1)


if __name__=="__main__":
    start = datetime.now()

    for _ in range(50000000):
        _ = faq(10)

    end = datetime.now()

    print(end - start)
