import Foundation
/*
풀이계획
1. A의 문자열을 왼쪽으로 돌린 문자열 배열을 만든다
2. A의 문자열을 오른쪽으로 돌린 문자열 배열을 만든다
3. 두 배열과 B를 비교해서 있으면 해당 배열의 인덱스에 1을 더해서 리턴한다.
4. 없으면 -1을 리턴한다.
*/
func solution(_ A:String, _ B:String) -> Int {
    var rightArr: [String] = []
    for i in 1...A.count - 1 {
        rightArr.append(String(A.suffix(i)) + String(A.prefix(A.count - i)))
    }
    if A == B {
        return 0
    } else if rightArr.contains(B) {
        return rightArr.firstIndex(of: B)! + 1
    }
    return -1
}