import Foundation

func solution(_ dots:[[Int]]) -> Int {
    print(dots.sort())
    let width: Int = abs(dots[0][0] - dots[2][0])
    let height: Int = abs(dots[0][1] - dots[2][1])
    return width * height
}