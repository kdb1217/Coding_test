let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let a = input.reduce(0) { $0 + $1}
print(a)
