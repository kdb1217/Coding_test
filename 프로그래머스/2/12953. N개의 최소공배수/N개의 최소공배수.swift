/*
풀이계획
1. 배열의 총곱을 곱하고
2. while문 돌려서 탐색하기 시간초과 뜨면 다시 생각해보기
*/
func solution(_ arr:[Int]) -> Int {
    var sortedArr = arr.filter { arr.sorted().last! % $0 != 0 }
    sortedArr.append(arr.sorted().last!)
    var answer = arr.reduce(1, *)
    var flag = false

    for i in sortedArr.last!...answer {
        flag = false
        for j in sortedArr {
            if i % j != 0 {
                flag = false
                break
            } else {
                flag = true
            }
        }
        if flag == true {
            return i
        }
    }
    return answer
}
