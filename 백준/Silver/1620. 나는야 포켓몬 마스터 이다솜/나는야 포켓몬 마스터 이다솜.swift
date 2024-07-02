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
풀이계획
1620 나는야 포켓몬 마스터 이다솜
1. 반복문을 통해서 포켓몬 정보를 딕셔너리로 입력받는다. (index, name) 배열또한 같이 입력받는다.
2. 반복문을 통해서 문제를 입력받은 다음 숫자가 오면 딕셔너리에서 해당 키값의 벨류값을 출력, 문자열이 오면 배열에서 firstIndex함수를 이용해서 index에 1을 더해서 출력한다.
 */

let arr = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = arr[0]
let M = arr[1]

var namedict: [String: Int] = [:]
var dict: [Int: String] = [:]

for i in 1...N {
    let tmp = readLine()!
    dict[i] = tmp
    namedict[tmp] = i
}

for _ in 0..<M {
    let tmp = readLine()!
    
    if tmp.allSatisfy({ $0.isNumber }) {
        print(dict[Int(tmp)!]!)
    } else {
        print(namedict[tmp]!)
    }
}
