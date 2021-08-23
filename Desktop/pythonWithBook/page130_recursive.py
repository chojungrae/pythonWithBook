def recursive_function() :
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# 재귀 함수란 자기 자신을 다시 호출하는 함수를 의미한다.

# 위 예제는 어느 정도 출력하다가 다음과 같은 오류 메시지를 출력하고 멈출 것이다.
# RecursionError: maximum recursion depth exceeded while pickling an object
# 이 오류 메시지는 재귀의 최대 깊이를 초과했다는 내용이다. 보통 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문이다.
