import Foundation
/*
풀이계획
1. 순열을 통해 모든 경우의 수를 구한다.
2. 이를 정렬하여 가장 큰 값을 구한다.- > 시간초과
3. 십의 자리 이상인 숫자들은 첫번째 숫자들로 비교한다.
4. 만약 첫번째 글자가 같고 자리수가 차이가나면, 무조건 자리수가 더 작은걸 기준으로 비교한다.
5. 반복문에서 리턴이 되지 않았을 경우 ex(369, 36) 9와 6을 비교하여 처리한다.
*/
func solution(_ numbers:[Int]) -> String {
    var arr = numbers.map { String($0) }
    
    arr.sort { ( n1, n2) -> Bool in 
        return n1 + n2 > n2 + n1
    }
    
    if arr.first == "0" {
        return "0"
    }
    else {
        return arr.joined()
    }
}


