func factorial(_ n: Int) -> Int {
    if n < 2 {
        return 1
    }
    return n * factorial(n - 1)
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], k = input[1]

print(factorial(n) / (factorial(k) * factorial(n - k)))