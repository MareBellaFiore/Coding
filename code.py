alphabet=["a", "b", "c", "d", "e", "f", "g","h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", " "]

def get():
        word = input("введите сообщение ")
        word = word.lower()
        num = int(input("введите число 1-26 "))
        if num < 1 or num > 26:
                while num < 1 or num > 26:
                        num = int(input("пожалуйста, введите корректное число 1-26 "))
        data = (word, num)
        return data

def code(word, num):
        new_word = ""
        for i in word:
                x = alphabet.index(i) + num
                if x > 26:
                        x = x-27
                char = alphabet[x]
                new_word += char
        print(new_word)
        print()

def decode(word, num):
        new_word = ""
        for i in word:
                x = alphabet.index(i) - num
                if x < 0:
                        x = x + 27
                char = alphabet[x]
                new_word += char
        print(new_word)
        print()


def main():
        while True:
                print("1.закодировать")
                print("2.раcкодировать")
                print("3.выход")
                print()
                n = int(input("введите число "))
                if n == 1:
                        (word, num) = get()
                        code(word, num)
                if n == 2:
                        (word, num) = get()
                        decode(word, num)
                if n == 3:
                        break



main()

