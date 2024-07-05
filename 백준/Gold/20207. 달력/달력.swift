import Foundation

//final class FileIO {
//    private var buffer:[UInt8]
//    private var index: Int
//    
//    init(fileHandle: FileHandle = FileHandle.standardInput) {
//        buffer = Array(fileHandle.readDataToEndOfFile())+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
//        index = 0
//    }
//    
//    @inline(__always) private func read() -> UInt8 {
//        defer { index += 1 }
//        
//        return buffer.withUnsafeBufferPointer { $0[index] }
//    }
//    
//    @inline(__always) func readInt() -> Int {
//        var sum = 0
//        var now = read()
//        var isPositive = true
//        
//        while now == 10
//                || now == 32 { now = read() } // 공백과 줄바꿈 무시
//        if now == 45{ isPositive.toggle(); now = read() } // 음수 처리
//        while now >= 48, now <= 57 {
//            sum = sum * 10 + Int(now-48)
//            now = read()
//        }
//        
//        return sum * (isPositive ? 1:-1)
//    }
//    
//    @inline(__always) func readString() -> String {
//        var str = ""
//        var now = read()
//        
//        while now == 10
//                || now == 32 { now = read() } // 공백과 줄바꿈 무시
//        
//        while now != 10
//                && now != 32 && now != 0 {
//            str += String(bytes: [now], encoding: .ascii)!
//            now = read()
//        }
//        
//        return str
//    }
//}
let n = Int(readLine()!)!
var arr: [Int] = Array(repeating: 0, count: 366)
var arr2: [[Int]] = []
var answer = 0
for _ in 0..<n {
    arr2.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

arr2.sort(by: { $0[0] == $1[0] ? $0[1] > $1[1] : $0[0] < $1[0] })

for i in 0..<arr2.count {
    for j in arr2[i][0]...arr2[i][1] {
        arr[j] += 1
    }
}

var tmpArr: [Int] = []
for i in 1..<arr.count {
    if arr[i] != 0 {
        tmpArr.append(arr[i])
    }
    if arr[i - 1] != 0 && arr[i] == 0 {
        answer += tmpArr.max()! * tmpArr.count
        tmpArr.removeAll()
    }
}

if !tmpArr.isEmpty {
    answer += tmpArr.max()! * tmpArr.count
}

print(answer)
