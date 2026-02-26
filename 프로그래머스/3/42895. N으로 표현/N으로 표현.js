function solution(N, number) {
    const s = Array.from({ length: 9 }, () => new Set())
    let n = 0
    
    if (N === number) return 1

    for (let i = 1; i <= 8; i++) {
        n = N + n
        s[i].add(n)
        n = n * 10
        
        for (let j = 1; j <= i - 1; j++) {
            for (const k of s[j]) {
                for (const l of s[i - j]) {
                    s[i].add(k + l)
                    s[i].add(k - l)
                    s[i].add(k * l)
                    s[i].add(k / l)
                }
            }
            if (s[i].has(number)) return i
        }
    }
    
    return -1
}