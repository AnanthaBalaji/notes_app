# Semantic Drift:
- Chunk contains mixed topics
- Embedding floats halfway between them
- Fetches data from unrelated paragraph
- Scores are similar for different contents
- Dosent understand the context


# Embedding Collapse:
- Every chunk looks similar
- embedding all cluster near the center
- consine distance becomes almost the same
- retrival dies


- Bad chunk size causes semantic collapse

## embedding space
- The vector space where we store the embedded chunks is called embedding space.
- Sentence in PDF -> Vectors -> embedding is a point with multiple dimensions(768-D MiniLM)
- points floating in a huge galaxy.
- 

## semantic cluster
- Words that occur often together are clustered together.
- The smaller the distance the larger the relation
- Larger th distance the lesser the relation


## Cosine Similarity:
- Lets consider each embedding as a arrow pointing to a direction.
- Smaller the angle between 2 arrows: meaning are similar, cosine distance is small, Good retrival
- Larger the angle between 2 arrows: meaning diverge, cosine distance is large, bad retrival


## drift(Semantic fragmentation -> embedding drift)
- Smaller chunks hold little meaning, vector becomes unstable
- Point jumps around depending on 1 or 2 words.
- Not enough context -> point unstable


## collapse(semantic collapse)
- When the chunk is too large, every chunk looks similar.
- They average out all meanings -> flatten direction.
- embedding cannot be segregated and clustered together.

## distance spread
- Term used to specify the distance between the embeddings in the cluster
- Smaller the distance larger the similarity
- Larger the distance lesser the similarity
- Example:
    - relevant documents have spread score: 0.1, 0.12, 0.2
    - irrelevent documents have score: 0.6, 0.7,0.81
    - this tells the spread is large, there is a clear gap between relavant and irrelavant information

- Smaller the spread harder it is to differnetiate
- Larger the spread easier to differentiate.