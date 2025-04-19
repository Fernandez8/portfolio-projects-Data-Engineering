import logging
import warnings
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.functions import round as spark_round
import traceback

###### Setup logs
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger = logging.getLogger("spark_structured_streaming")
warnings.simplefilter("ignore")

# JDBC configuration
jdbc_url = "jdbc:postgresql://postgres:5432/dev"
connection_properties = {
    "user": "root",
    "password": "root",
    "driver": "org.postgresql.Driver"
}

# ## SCHEMA 
def get_schema():
    return StructType([
        StructField("DateTime", StringType(), True),
        StructField("oil_temperature", StringType(), True),
        StructField("oil_pressure", StringType(), True),
        StructField("engine_power", StringType(), True),
        StructField("engine_speed", StringType(), True),
        StructField("engine_vibrations", StringType(), True)
    ])

def start_streaming():
    try:
        # ## Spark, Kafka + Postgres
        spark = SparkSession.builder \
            .appName("SparkStructuredStreaming") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2,org.postgresql:postgresql:42.2.22") \
            .getOrCreate()

        spark.sparkContext.setLogLevel("ERROR")
        logger.info("Spark session created")

        # ## read Kafka topic
        df = spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka1:19092") \
            .option("subscribe", "registered_user") \
            .option("startingOffsets", "earliest") \
            .load()

        ### Parsing JSON + cast
        schema = get_schema()
    
        parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
            .select(from_json(col("json"), schema).alias("data")) \
            .select("data.*") \
            .select(
                to_timestamp(col("DateTime"), "yy-MM-dd HH:mm:ss").alias("DATETIME"),
                spark_round(col("oil_temperature").cast("float"), 2).alias("oil_temperature"),
                spark_round(col("oil_pressure").cast("float"), 2).alias("oil_pressure"),
                spark_round(col("engine_power").cast("float"), 2).alias("engine_power"),
                spark_round(col("engine_speed").cast("float"), 2).alias("engine_speed")
            )

        ### write in PostgreSQL
        def write_to_postgres(batch_df, batch_id):
            try:
                batch_df.write.jdbc(
                    url=jdbc_url,
                    table="DATA_FLOW",
                    mode="append",
                    properties=connection_properties
                )
                logger.info(f"Batch {batch_id} written in PostgreSQL")
            except Exception as e:
                logger.error(f"Error when writing batch {batch_id}: {e}")
                traceback.print_exc()

        # ### Streaming
        query = parsed_df.writeStream \
            .outputMode("append") \
            .foreachBatch(write_to_postgres) \
            .start()

        query.awaitTermination()

    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    start_streaming()
