import Foundation

func solution(_ s:String) -> Bool
{
    var flag: Int = 0
    var ans:Bool = true
    for i in s {
        if i == "(" {
            flag += 1
        } else if i == ")" {
            if flag <= 0 {
                return false
            }
            flag -= 1
        }
    }
    
    if flag > 0 {
        ans = false
    }
    return ans
}