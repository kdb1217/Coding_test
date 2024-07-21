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

//<main>
//    <div title="title_name_1">
//        <p>paragraph 1</p>
//        <p>paragraph 2 <i>Italic Tag</i> <br > </p>
//        <p>paragraph 3 <b>Bold Tag</b> end.</p>
//    </div>
//    <div title="title_name_2">
//        <p>paragraph 4</p>
//        <p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p>
//    </div>
//</main>
//<main><div title="title_name_1"><p>paragraph 1</p><p>paragraph 2 <i>Italic Tag</i> <br > </p><p>paragraph 3 <b>Bold Tag</b> end.</p></div><div title="title_name_2"><p>paragraph 4</p><p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p></div></main>
//title : title_name_1
//paragraph 1
//paragraph 2 Italic Tag
//paragraph 3 Bold Tag end.
//title : title_name_2
//paragraph 4
//paragraph 5 Italic Tag 2 end.

//let n = Int(readLine()!)!
//let m = Int(readLine()!)!
//let s = readLine()!.map { String($0) }
//var count = 0
//
//var N: String = ""
//
//for i in 0..<2 * n + 1 {
//    if i % 2 == 1 {
//        N += "O"
//    } else {
//        N += "I"
//    }
//}
//
//var start = 0
//var end = N.count-1
//
//
//for i in end..<s.count {
//    if s[start...i].joined() == N {
//        count += 1
//    }
//    start += 1
//}
//
//print(count)

//
//  main.swift
//  Day01
//
//  Created by 김다빈 on 7/15/24.
//
import Foundation

let arr = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = arr[0]
let M = arr[1]

var trees = readLine()!.split(separator: " ").map { Int(String($0))! }


//for i in 1...max {
//    let tmp = trees.map { $0 - i }.filter { $0 > 0}.reduce(0, +)
//    if tmp < M {
//        print(i - 1)
//        break
//    }
//}
var start = 0
var last = trees.max()!
var result = 0

while start <= last {
    let mid = (start + last) / 2
    let tmp = trees.map { $0 - mid }.filter { $0 > 0 }.reduce(0, +)

    
    if tmp >= M {
        result = mid
        start = mid + 1
    } else {
        last = mid - 1
    }
}

print(result)


