n, m = map(int, input().split())
arr = sorted(map(int, input().split()))  # 정렬을 통해 중복을 그룹화
result = []  # 최종 결과를 저장할 리스트

def backtracking(depth, sequence):
    if depth == m:  # 길이가 m인 순열 완성
        result.append(sequence[:])  # 완성된 순열 저장
        return

    prev = -1  # 이전에 사용한 숫자 기록
    for i in range(len(arr)):
        # 중복 처리: 같은 depth에서 동일 숫자는 한 번만 사용
        if prev == arr[i]:
            continue
        prev = arr[i]  # 이전 숫자를 현재 숫자로 갱신
        sequence.append(arr[i])
        backtracking(depth + 1, sequence)
        sequence.pop()  # 백트래킹: 상태 복원

backtracking(0, [])
for seq in result:
    print(*seq)