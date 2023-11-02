import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import desc

#Creating environment
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.config("spark.driver.host", "localhost").appName("VB_Base").getOrCreate()

#Creating important structure to read csv file
vb_schema = StructType(
    [
        StructField("Player", StringType(), True),
        StructField("Position", StringType(), True),
        StructField("Points", IntegerType(), True),
        StructField("BlockPoints", IntegerType(), True),
        StructField("Aces", IntegerType(), True),
        StructField("SpikePoints", IntegerType(), True),
        StructField("Receive", IntegerType(), True),
    ]
)

csv_path = 'VB_Base_CSV.csv'
df_vb = spark.read.csv(csv_path, schema=vb_schema, header=True)
rows = df_vb.count()
df_vb.createOrReplaceTempView('VB_Base')

def Choose_position(Chosen_position):
    Your_Position = spark.sql(f"SELECT * FROM VB_Base WHERE Position = '{Chosen_position}' ")
    All_From_One_Position = Your_Position.count()
    Your_Position.show(All_From_One_Position)

def Choose_element(Chosen_element):
    Your_Element = df_vb.select('*').sort(desc(Chosen_element))
    All_From_One_Element = Your_Element.count()
    Your_Element.show(All_From_One_Element)