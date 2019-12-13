def get_input():
    try:
        a=int(input('enter the value : '))
        b=int(input('enter the b value : '))
        return  a,b
    except ValueError as e:
        print(e)
        return  get_input()
    finally:
        print('finaly of get_input')

def div(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('finally of div')

def main():
    try:
        a,b=get_input()
        c=div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e:
        print(e)
        main()
    except:
        print('exception arised')
    finally:
        print('process completes successfully')

if __name__ == '__main__':
    print(main())















#
# def sample():
#     try:
#         return 5
#     except:
#         return 10
#     finally:
#         return 15
# print(sample())

