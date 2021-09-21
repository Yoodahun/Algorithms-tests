# 큰 수의 법칙
- 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다. 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
- 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때, M이 8이고 K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로, 큰 수의 법칙에 따른 결과는 `6+6+6+5+6+6+6+5` 인 46이 된다.
- 단 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 `3,4,3,4,3` 으로 이루어진 배열이 있을 때, M이고 K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 `4+4+4+4+4+4` 인 28이 도출된다.
- 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 떄의 큰 수의 법칙에 따른 결과를 출력하시오.

## 입력조건
- 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 공백으로 구분하며 각각의 자연수는 1이상 10,000 의 수가 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.


## 문제 해결 조건
- 입력값중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
- 연속으로 더할 수 있는 횟수는 최대 K번이므로, 가장 큰 수를 K번 더하고, 두 번째로 큰 수를 한 번 더하는 연산을 반복하면 된다.