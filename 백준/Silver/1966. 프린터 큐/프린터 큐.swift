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
/*
1966 프린터 큐
 1. 튜플로 저장 해서 입력순서와 중요도를 저장한다.
 2. 큐를 활용헤서 i가 순서대로 정렬될까지 반복문을 돌린다.
 3. 정렬판단기준 ->
 */

func solution(from arr1: [Int], with arr2: [Int]) -> Int {
    var sortedArr: [(Int,Int)] = []
    for (index,i) in arr2.enumerated() {
        sortedArr.append((index,i))
    }
    var answer: [(Int,Int)] = []
    while arr2.sorted(by: { $0 > $1 }) != answer.map({ $0.1 }) {
        let first = sortedArr[0]
        if first.1 == sortedArr.map({ $0.1 }).max()! {
            sortedArr.removeFirst()
            answer.append(first)
        } else {
            sortedArr.removeFirst()
            sortedArr.append(first)
        }
    }
    return answer.map { $0.0 }.firstIndex(of: arr1[1])! + 1
}


let num = Int(readLine()!)!

for _ in 0..<num {
    let arr1 = readLine()!.split(separator: " ").map { Int(String($0))! }
    let arr2 = readLine()!.split(separator: " ").map { Int(String($0))! }
    print(solution(from: arr1, with: arr2))
}

