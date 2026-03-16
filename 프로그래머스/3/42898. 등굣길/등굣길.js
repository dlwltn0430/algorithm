function solution(m, n, puddles) {
    let map = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0))
    
    puddles.forEach(([x, y]) => {
        map[y][x] = -1 
    })
    
    map[1][1] = 1
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (i === 1 && j === 1) continue
            
            if (map[i][j] === -1) {
                map[i][j] = 0
                continue
            }
            
            map[i][j] += (map[i - 1][j] + map[i][j - 1]) % 1000000007
        }
    }
    
    return map[n][m]
}