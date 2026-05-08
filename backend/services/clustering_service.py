import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from backend.services.embedding_service import (
    generate_embedding
)

from backend.database.db import SessionLocal

from backend.database.models import TopicCluster


SIMILARITY_THRESHOLD = 0.80


def normalize_topic(topic):

    db = SessionLocal()

    embedding = generate_embedding(topic)

    clusters = db.query(TopicCluster).all()

    # Compare with existing clusters
    for cluster in clusters:

        cluster_embedding = np.array(
            json.loads(cluster.embedding)
        ).reshape(1, -1)

        current_embedding = np.array(
            embedding
        ).reshape(1, -1)

        similarity = cosine_similarity(
            current_embedding,
            cluster_embedding
        )[0][0]

        if similarity >= SIMILARITY_THRESHOLD:

            db.close()

            return cluster.topic_name

    # Create new cluster
    new_cluster = TopicCluster(

        topic_name=topic,

        embedding=json.dumps(embedding)
    )

    db.add(new_cluster)

    db.commit()

    db.close()

    return topic