import Foundation

let num = Int(readLine()!)!
var queue = Queue<Any>()

for _ in 1...num {
    let tmp = readLine()!.split(separator: " ").map {$0}
    if tmp[0] == "push" {
        queue.enqueue(Int(tmp[1]) ?? 0)
        
    } else if tmp[0] == "pop" {
        let num = queue.dequeue()
        print(num ?? -1)
    } else if tmp[0] == "size" {
        print(queue.count())
    } else if tmp[0] == "empty" {
        print(queue.isEmpty() ? 1 : 0)
    } else if tmp[0] == "front" {
        print(queue.front() ?? -1)
    } else if tmp[0] == "back" {
        print(queue.back() ?? -1)
    }
}

struct Queue <T> {
    // 빈 Array 선언
    private var elements: [Int] = []
    
    // Queue 내 원소 개수
    public func count() -> Int {
        return elements.count
    }
    
    // Quque가 비었는지 확인
    public func isEmpty() -> Bool {
        return elements.isEmpty
    }
    
    // 요소 추가 메서드
    public mutating func enqueue(_ element: Int) {
        elements.append(element)
    }
    
    // 삭제 메소드
    public mutating func dequeue() -> Int? {
        return isEmpty() ? nil : elements.removeFirst()
    }
    
    public mutating func front() -> Int? {
        return isEmpty() ? -1 : elements.first!
    }
    
    public mutating func back() -> Int? {
        return isEmpty() ? -1 : elements.last!
    }
    
    // elements 초기화
    public mutating func clear() {
        elements.removeAll()
    }
}
