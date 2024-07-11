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

let n = Int(readLine()!)!

var arr: [Int] = [1,2]

if n == 1 {
    print(1)
} else if n == 2 {
    print(2)
} else {
    for i in 2..<n {
        arr.append((arr[i - 1] + arr[i - 2]) % 10007)
    }
    print(arr[n - 1])
}
