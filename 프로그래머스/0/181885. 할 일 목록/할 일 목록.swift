import Foundation

func solution(_ todo_list:[String], _ finished:[Bool]) -> [String] {
    var answer: [String] = []
    for i in stride(from: 0, to: finished.count, by: 1) {
        if !finished[i] {
            answer.append(todo_list[i])
        }
    }
    return answer
}