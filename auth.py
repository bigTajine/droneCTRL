def func1():
    user_flag = False

    while user_flag != True:

        username = 'KStol1'
        password = 'KStol1'

        userInput = input("$ USERNAME: ")

        if userInput == username:
            a=input("# PASSWORD: ")
            if a == password:
                user_flag = True
                print("──────────────────")
                print("% WELCOME "+username+"!")
                print("──────────────────")
            else:
                print("^ WRONG PASSWORD")
                print("──────────────────")
        else:
            print("^ WRONG USERNAME")
            print("──────────────────")

if __name__ == '__main__':
    func1()
