import Foundation
// 외곽 둘레가 brown이 되면 된다.
// 넓이가 브라운과 옐로우의 합이면서 둘레가 브라운인 값을 찾자.
func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let area = brown + yellow
    var answer: [Int] = []
    for i in 1...area {
        if area % i == 0 && area / i <= i && ((area / i * 2) + (i * 2)) - 4 == brown {
            answer = [i, area / i]
        }
    }
    return answer
}