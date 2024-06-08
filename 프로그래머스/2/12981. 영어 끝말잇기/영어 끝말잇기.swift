import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var count: Int = 0
    var firstChar: Character = words[0].first!
    var lastChar: Character = words[0].last!
    var usedWords: Set<String> = [words[0]]

    
    for i in 1..<words.count {
        firstChar = words[i].first!
        if firstChar == lastChar && !usedWords.contains(words[i]) {
            lastChar = words[i].last!
            usedWords.insert(words[i])
        } else {
            return [i % n + 1, i / n + 1]
        }
    }
    return [0,0]
}