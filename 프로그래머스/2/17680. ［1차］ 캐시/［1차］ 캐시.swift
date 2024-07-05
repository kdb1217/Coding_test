func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    var arr = cities.map { $0.lowercased() }
    var cache: [String] = []
    var time = 0
    if cacheSize == 0 {
        return 5 * cities.count
    }
    arr.forEach { i in
        if cache.contains(i) {
            time += 1
            cache.remove(at: cache.firstIndex(of:i)!)
            cache.append(i)
        } else {
            time += 5
            if cache.count >= cacheSize {
                cache.removeFirst()
            }
            cache.append(i)
        }
    }
    return time
}