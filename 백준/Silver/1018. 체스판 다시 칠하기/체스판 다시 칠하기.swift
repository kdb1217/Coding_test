import Foundation

//final class FileIO {
//    private let buffer:[UInt8]
//    private var index: Int = 0
//
//    init(fileHandle: FileHandle = FileHandle.standardInput) {
//        
//        
//        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
//    }
//
//    @inline(__always) private func read() -> UInt8 {
//        defer { index += 1 }
//
//        return buffer[index]
//    }
//
//    @inline(__always) func readInt() -> Int {
//        var sum = 0
//        var now = read()
//        var isPositive = true
//
//        while now == 10
//                || now == 32 { now = read() } // 공백과 줄바꿈 무시
//        if now == 45 { isPositive.toggle(); now = read() } // 음수 처리
//        while now >= 48, now <= 57 {
//            sum = sum * 10 + Int(now-48)
//            now = read()
//        }
//
//        return sum * (isPositive ? 1:-1)
//    }
//
//    @inline(__always) func readString() -> String {
//        var now = read()
//
//        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
//
//        let beginIndex = index-1
//
//        while now != 10,
//              now != 32,
//              now != 0 { now = read() }
//
//        return String(bytes: Array(buffer[beginIndex..<(index-1)]), encoding: .ascii)!
//    }
//
//    @inline(__always) func readByteSequenceWithoutSpaceAndLineFeed() -> [UInt8] {
//        var now = read()
//
//        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
//
//        let beginIndex = index-1
//
//        while now != 10,
//              now != 32,
//              now != 0 { now = read() }
//
//        return Array(buffer[beginIndex..<(index-1)])
//    }
//}

let board1: [[String]] = [["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"]]

let board2: [[String]] = [["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"],
                             ["B","W","B","W","B","W","B","W"],
                             ["W","B","W","B","W","B","W","B"]]
let arr = readLine()!.split(separator: " ").map { Int($0)! }

var board: [[String]] = []
var answers: [Int] = []

for _ in 0..<arr[0] {
    board.append(readLine()!.map { String($0) })
}

for y in 0...(arr[0] - 8) {
    for x in 0...(arr[1] - 8) {
        var diffCount1 = 0
        var diffCount2 = 0
        for i in y..<(y + 8) {
            for j in x..<(x + 8) {
                if board1[i - y][j - x] != board[i][j] {
                    diffCount1 += 1
                }
                
                if board2[i - y][j - x] != board[i][j] {
                    diffCount2 += 1
                }
            }
        }
        answers.append(diffCount1 > diffCount2 ? diffCount2 : diffCount1)
    }
}

print(answers.min()!)



