/* 
풀이 계획
1. 총 일수를 계산하여 cnt에 저장한다
2. 그 후 days와 총일수를 나머지 연산하여 days의 요일을 계산하여 Return한다.
*/
func solution(_ a:Int, _ b:Int) -> String {
    // 1월1일이 금요일이니깐 금요일부터 배열을 시작한다.
    let days: [String] = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    let months: [Int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    let date: [Int] = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    var cnt = date[0...a-1].reduce(0, +) + b
    print(cnt)
    return days[cnt % 7]
}