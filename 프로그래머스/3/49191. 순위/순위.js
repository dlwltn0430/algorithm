function solution(n, results) {
    let t = Array.from({ length: n + 1 }, () => Array(n + 1).fill(false))
    let answer = 0
    
    results.forEach(([p1, p2]) => {
        t[p1][p2] = true
    })
    
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (t[i][k] && t[k][j]) t[i][j] = true
            }
        }   
    }
    
    for (let i = 1; i <= n; i++) {
        let count = 0
        
        for (let j = 1; j <= n; j++) {
            if (t[i][j] || t[j][i]) count++
        }
        
        if (count === n - 1) answer++
    }
    
    return answer
}