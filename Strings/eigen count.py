#def test(my_string, letter):
#   sum(char == ''letter'' for char in my_string)

#print (test ('bananaa' ,a))
def count (word, letter):
           c = 0

           for w in word:
               if letter == w:
                   c += 1
            return c
print ("banana" .count("a"))

#replace leter with blank string


def one_liner_count(word, letter):
    return len(word) - len(word.replace (letter , ""))

assert one_liner_count("banana, "a"") == 3
assert oneliner_count("banana", "n") ==2