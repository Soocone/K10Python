'''
문제 5
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.(트리모양)
   *
  **
  ***
 ****
 *****
'''

for i in range(5):
    for j in range(5):
        if i+j>=4:
            print('*', end=' ')
        else:
            print(' ', end='')
    print()
