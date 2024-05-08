import Foundation

/* 풀이계획
    1. 네주사위의 결과를 중복제거를 한 Array와 전부를 담는 Array로 선언
    2. 중복제거를 배열을 switch문으로 작성
    3. 모든 상황을 case화 시켜서 조건에 대입한다.
*/
func solution(_ a:Int, _ b:Int, _ c:Int, _ d:Int) -> Int {
    var tmp: Set<Int> = [a,b,c,d]
    var flag = Array(tmp)
    let arr: [Int] = [a,b,c,d]

    print(flag)
    switch flag.count {
        case 1:
            return 1111 * a
        case 2:
        if (arr.filter{$0 == flag[0]}.count == 3 ||  arr.filter{$0 == flag[1]}.count == 3) {
            let p = arr.filter{$0 == flag[0]}.count == 3 ? flag[0] : flag[1]
            let q = arr.filter{$0 == flag[0]}.count == 3 ? flag[1] : flag[0]
            return Int(pow(Double(10 * p + q) , 2))
        } else { // 두개씩 같은 값이 나온 경우
            return (flag[0] + flag[1]) * abs(flag[0] - flag[1])
        }   
        case 3:
        var answer: [Int] = []
        for i in flag {
            if arr.filter{$0 == i}.count == 1 {
                answer.append(i)
            }
        }
        return answer.reduce(1, *)
        default:
            return flag.min()!
    }
}