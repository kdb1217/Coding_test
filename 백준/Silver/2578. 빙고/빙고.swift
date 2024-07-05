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

var userBoard: [[(Int, Bool)]] = []
var answerBoard: [[Int]] = []
var answer = 0
func checkBingo(with bingoBoard: [[(Int, Bool)]]) -> Bool{
    var count = 0
    for i in 0..<userBoard.count {
        var tmp = 0
        if userBoard[i].filter({ $0.1 == true }).count == 5 {
            count += 1
        }
        for j in 0..<userBoard.count {
            if userBoard[j][i].1 == true {
                tmp += 1
            }
        }
        if tmp == 5  {
            count += 1
        }
        if count >= 3 {
            return true
        }
    }
    
    var tmp = 0
    for i in 0..<userBoard.count {
        if userBoard[i][i].1 == true {
            tmp += 1
        }
    }
    if tmp == 5 {
        count += 1
    }
    
    if count >= 3 {
        return true
    }
    tmp = 0
    
    for i in stride(from: userBoard.count - 1, to: -1, by: -1) {
        if userBoard[(userBoard.count-1) - i][i].1 == true {
            tmp += 1
        }
    }
    
    if tmp == 5 {
        count += 1
    }
    
    if count >= 3 {
        return true
    }
    
    return false
}


for _ in 0..<5 {
    let tmp = readLine()!.split(separator: " ").map { Int(String($0))! }
    let arr = tmp.map { ($0,false) }
    userBoard.append(arr)
}

for _ in 0..<5 {
    answerBoard.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}
let flatBoard = userBoard.flatMap({ $0 })

answerBoard.flatMap({ $0 }).forEach { i in
    answer += 1
    if let tmp = flatBoard.firstIndex(where: { $0.0 == i }) {
        userBoard[tmp/5][tmp % 5].1 = true
        if checkBingo(with: userBoard) {
            print(answer)
            exit(0)
        }
    }
   
    
}

