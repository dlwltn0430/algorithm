function solution(array, commands) {
    let answer = []
    let n = []
    
    commands.forEach(([i, j, k]) => {
        n = array.slice(i - 1, j)
        n.sort((a, b) => a - b)
        answer.push(n[k -1])
    })
    
    return answer
}