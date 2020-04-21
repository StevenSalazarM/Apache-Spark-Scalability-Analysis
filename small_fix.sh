#!/bin/bash

# add SPARK_LOCAL_IP and SPARK_MASTER_HOST to conf/spark-env.sh
printf "SPARK_LOCAL_IP=" >> /home/ubuntu/Spark/conf/spark-env.sh; hostname -I >> /home/ubuntu/Spark/conf/spark-env.sh; echo "SPARK_MASTER_HOST=172.31.2.81" >> /home/ubuntu/Spark/conf/spark-env.sh

# add properties into conf/spark-defaults.conf
echo "spark.master                     spark://172.31.2.81:7077" > /home/ubuntu/Spark/conf/spark-defaults.conf
echo "spark.eventLog.enabled           true" >> /home/ubuntu/Spark/conf/spark-defaults.conf
echo "spark.eventLog.dir               file:///home/ubuntu/logs" >> /home/ubuntu/Spark/conf/spark-defaults.conf
echo "spark.history.fs.logDirectory    file:///home/ubuntu/logs" >> /home/ubuntu/Spark/conf/spark-defaults.conf
echo "spark.executor.memory            10g" >> /home/ubuntu/Spark/conf/spark-defaults.conf

