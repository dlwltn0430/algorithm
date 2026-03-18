function solution(genres, plays) {
    const genrePlayCount = {}
    const genreSongs = {} 
    // { classic: [{id: 1, play: 400}, {id: 5, play: 100}], pop: [...] }
    
    genres.forEach((genre, i) => {
        genrePlayCount[genre] = (genrePlayCount[genre] || 0) + plays[i]
        
        if (!genreSongs[genre]) genreSongs[genre] = []
        genreSongs[genre].push({id: i, play: plays[i]})
    })
    
    const sortedGenres = Object.keys(genrePlayCount).sort((a, b) => {
        return genrePlayCount[b] - genrePlayCount[a]
    })
    
    const answer = []

    sortedGenres.forEach(genre => {
        genreSongs[genre].sort((a, b) => {
            if (a.play === b.play) return a.id - b.id
            return b.play - a.play
        })
        
        genreSongs[genre].slice(0, 2).map((item) => answer.push(item.id))
    })
        
    return answer
}