from random import randint

def get_random_pks(count, range):
  i = count;
  pks = []
  while i > 0:
    print(i);
    pks.append(randint(*range))
    i -= 1

  print(pks)
  return pks
