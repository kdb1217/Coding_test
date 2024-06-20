import Foundation

/* 
풀이계획
1. 왼쪽 숫자와 오른쪽 숫자를 각각 배열에 저장한다.
2. 반복문을 통해서 왼쪽 배열과 오른쪽 배열에 숫자가 있는지 확인하고 있다면 answer에 L 또는 R 을추가한다.
3.
*/
func solution(_ numbers:[Int], _ hand:String) -> String {
    var nums = numbers
    nums = nums.map { $0 == 0 ? 11 : $0 }
    var answer = ""
    let leftNumbers: [String] = ["1","4","7","10"]
    let rightNumbers: [String] = ["3","6","9","12"]
    let centerNubmers: [String] = ["2","5","8","11"]
    var lefthand = 10
    var righthand = 12
    for i in nums {
        if leftNumbers.contains(String(i)) {
            answer += String("L")
            lefthand = i
        } else if rightNumbers.contains(String(i)) {
            answer += String("R")
            righthand = i
        } else {
            let leftTmp = abs(lefthand / 3 - i / 3) + abs((lefthand-1 ) % 3 - (i-1) % 3)
            let rightTmp = abs(righthand % 3 == 0 ? ((righthand - 1) / 3) - (i / 3) : righthand  / 3 - i / 3) + abs(righthand % 3 == 0 ? (righthand-1) % 3 - (i-1) % 3 : righthand % 3 - i % 3)
            if leftTmp < rightTmp {
                lefthand = i
                answer += String("L")
            } else if leftTmp > rightTmp {
                righthand = i
                answer += String("R")
            } else if leftTmp == rightTmp {
                if hand == "right" {
                    righthand = i
                    answer += String("R")
                } else {
                    lefthand = i
                    answer += String("L")
                }
            }
        }
    }
    return answer
}