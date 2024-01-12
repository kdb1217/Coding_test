import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}


var answer: [String] = []
private func findRoomNum(H: Int, W: Int, N: Int) {
    var cnt: Int = 0
    for i in 1...W {
        for j in 1...H {
            let roomNumber = j * 100 + i
            cnt += 1
            if cnt == N {
                print(roomNumber)
            }
        }
    }
}


let InputNum: Int = Int(readLine()!)!

for _ in 0...InputNum - 1 {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    findRoomNum(H: input[0], W: input[1], N: input[2])
}

