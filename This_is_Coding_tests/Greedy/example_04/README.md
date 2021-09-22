# 숫자 카드 게임
- 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 
	- 숫자가 쓰인 카드들이 N x M 형태로 놓여있다. 이 때 N은 행의 개수를 의미하며 M은 열의 개수이다.
	- 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
	- 그 다음에 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
	- 따라서 처음 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
- 예를 들어 3x3 형태로 카드들이 놓여있다고 가정하자.

3 1 2
4 1 4
2 2 2
	- 여기서 카드를 골라낼 행을 고를 때, 첫 번째 혹은 두 번째 행을 선택하는 경우, 최종적으로 뽑는 카드는 1이다.
	- 하지만 세번 째 행을 선택하는 경우 최종적으로 뽑는 카드는 2이다. 따라서 이 예제에서는 세번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정답이다.
카드들이 N x M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.

## 입력 조건 
	- 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
	- 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.

## 문제 해설
문제 해결을 위한 아이디어를 떠올리면, 정담을 찾을 수 있다.
이 문제를 푸는 아이디어는 ::각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰수:: 를 찾는 것.
입력 조건에서 입력으로 들어오는 수는 모두 10,000이하 이므로 단순히 배열에서 가장 작은 수를 찾는 기본 문법을 이용하여 각 행에서 가장 작은 수를 찾은 다음, 그 수 중에서 가장 큰 수를 찾는 방식으로 문제를 해결할 수 있다.
