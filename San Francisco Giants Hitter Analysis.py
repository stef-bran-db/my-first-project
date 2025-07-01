# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC SELECT Name, Batting_Average
# MAGIC FROM baseball.sfg.sfg_batting
# MAGIC WHERE At_Bats > 100 AND Year = '2023'
# MAGIC SORT BY Batting_Average DESC
# MAGIC LIMIT 16

# COMMAND ----------


