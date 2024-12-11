# Introduction to SQL Queries: A Comprehensive Guide

SQL (Structured Query Language) is the standard language used to interact with relational databases. Whether you're retrieving data, modifying records, or analyzing large datasets, SQL provides a powerful and efficient way to manage and manipulate information stored in relational databases. 

In this tutorial, we will explore the core concepts of SQL, ranging from simple data retrieval to complex queries involving joins, aggregations, and subqueries. You’ll learn how to:

- Write basic queries to select, insert, update, and delete data
- Use filtering, grouping, and sorting to retrieve the exact data you need
- Combine multiple tables with JOINs to build more powerful queries
- Implement advanced SQL techniques such as subqueries, CTEs, window functions, and aggregate functions

By the end of this guide, you'll have a solid understanding of SQL and be equipped to write your own queries for a variety of real-world applications.

Let's start by installing these two libraries. We will use sqlalchemy only to be able to write raw SQL make updates to our tables. The reason for this, is because this tutorial is written in a Jupyter Notebook and we want the ability to also modify our database.

-- **NB**: Using Jupyter Notebook to modify the original source of the data is usually not a good idea. For this tutorial, the important thing to focus on is the actual SQL Queries. The database server used was **MariaDB**.

-- Why use Jupyter Notebook? Jupyter Notebook is an effective interactive environment for learning and exploration. 

--  I have included comments for further clarification.
