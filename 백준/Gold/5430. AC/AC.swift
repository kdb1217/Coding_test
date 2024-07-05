func solution() {
    let p = readLine()!
    var tail = Int(readLine()!)!
    let array = readLine()!.dropFirst().dropLast().split(separator: ",").map { String($0) }
    var isReverse = false
    var head = 0
    for p in p {
        if p == "R" {
            isReverse.toggle()
            continue
        }
        if isReverse {
            tail -= 1
        } else {
            head += 1
        }
        if head > tail { break }
    }
    
    if head > tail {
        print("error")
    } else {
        if isReverse {
            print("[\(array[head..<tail].reversed().joined(separator: ","))]")
        } else {
            print("[\(array[head..<tail].joined(separator: ","))]")
        }
    }
}

let t = Int(readLine()!)!
for _ in 0..<t { solution() }