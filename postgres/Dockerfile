# Start with the official PostgreSQL 17 image.
FROM postgres:17


# apt-get update → Update the package list.
# apt-get install -y postgresql-17-pgvector → Install the pgvector extension.
# rm -rf /var/lib/apt/lists/* → Clean up package cache to keep the image smaller.

RUN apt-get update && \
    apt-get install -y postgresql-17-pgvector && \
    rm -rf /var/lib/apt/lists/*