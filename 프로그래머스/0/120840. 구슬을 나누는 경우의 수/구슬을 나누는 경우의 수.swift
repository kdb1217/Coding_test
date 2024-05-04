import Foundation

func solution(_ balls:Int, _ share:Int) -> Double {
    
    return balls == share ? 1 : round(factorial(balls) / (factorial(share) * factorial(balls - share)))
}

func factorial (_ num: Int) -> Double {
    var arr: [Double] = []
    for i in 1...num {
        arr.append(Double(i))
    }
    return Double(arr.reduce(1, *))
}