func solution(_ n:Int) -> Int {
    var arr: [Int] = [0, 1, 2]
    if n == 1 {
        return 1
    } else if n == 2{
        return 2
    } else {
        for i in 3...n {
            arr.append( (arr[i - 1] + arr[i - 2]) % 1234567 )
        } 
    }
    return arr.last!
}