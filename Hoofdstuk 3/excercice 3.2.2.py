word = 'test'

def do_twice(f, word):
   f(word)
   f(word)

def print_spam(word):
   print (word)

#iif statement is om te zorgen dat waneer het wordt opgeroepen de do_twice niet wordt uitgevoerd
if __name__ =="__main__":
   do_twice(print_spam, word)

