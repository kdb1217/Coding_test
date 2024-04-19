import Foundation
// 6 * n 의 최소공배수를 구한다음 그걸 다시 6으로 나눈다.
func solution(_ n:Int) -> Int {
    return lcm(6, n) / 6
}

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a % b)
    }
}

func lcm(_ a: Int, _ b: Int) -> Int {
    return a * b / gcd(a, b)
}