FROM postgres:15

RUN apt-get update && \
    apt-get install -y postgresql-15-cron && \
    echo "shared_preload_libraries = 'pg_cron'" >> /usr/share/postgresql/postgresql.conf.sample

# Pour être sûr que pg_cron est reconnu au lancement
CMD ["postgres", "-c", "shared_preload_libraries=pg_cron"]
