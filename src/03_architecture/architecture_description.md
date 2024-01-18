## Architecture Description

This is a cloud-based architecture designed to ingest NFe files in JSON format and applying ETL processes to structure the data into frames. This frames are then stored, serving data analytics and data science teams across diverse business initiatives. breakdown of this architecture can be diveded in three parts: providing the essencial infrastructure, services and permissions; ingesting the files and transforming & sharing it's contents. This architecture was designed taking into account low prices and resource savings. You can find a more detailed information below:

### Providing the Essencial Infrastructure

First, in the IAM (Identity and Access Management) section, create an account that will be used to provide other components and create a service account and give it permissions to communicate between the services. This will ensure that only authorized users and services have access to these resources. With the service account correctly configured, start providing the other components.

### Ingesting Files

The Cloud Scheduler will be configured to recurrently active the Cloud Function that will communicate with the external API and collect NFe files in JSON format. The Cloud Function will communicate with the internal database, check the last NFe file stored to collect the delta information (with a limit that can be determinated as a parameter to prevent exceeding the specified CF memory). After that, the cloud function will store the raw data in BigQuery, for backup, logging and debug purpuses. Than, the function parses the JSON, transform it into a dataframe and store it on another table in BigQuery.


***Alternatives and Improvements***


The Cloud Scheduler could be replaced with a Web Hook, so when the client stores a new NFe file, automatically triggers the Cloud Function, no needing to await the Scheduler to run. A Pub/Sub could be placed between the API and the Cloud Function to prevent missing payload when Functions are offline for any reason. This is a Batch ingestion, but it could be ingested as a stream as well, using Pub/Sub + Dataflow.

### Transforming & Sharing

The stored data is available on BigQuery which is a high performance SQL database. The relational data can be accessed by the teams directly, using BigQuery. To structure the data to multi-dimensinal data warehouse structure, the Dataflow will consume and transform this information as needed, and store it again on BigQuery, making it available in different formats. Dataflow can also reprocess malparsed data, using the redundancy table that stores the raw payload of the API, without having to send HTTP requests again.


***Alternatives and Improvements***


The BigQuery was chosen to store the data because it's semi-structured in this scenario. It could be replaced by some Data Lake structure, like Cloud Storage, for example. A Data Catalog could be also added to this architecture to data exploration and metadata management.


## Estimated Architecture Price (https://cloud.google.com/products/calculator?hl=en)
**Total: ~ US$ 321,56/month** (*Estimated On: 01/18/24*)


#### Cloud Functions ~ $ 10,24

Memory Allocated: 256 MiB (.167 vCPU)
Requests per month (millions): 1 Million
Cloud Functions version: 2nd gen
Region: us-central1 (Iowa) - Tier 1
Average execution time per request (ms): 1000 ms
Concurrent requests per instance: 1

#### On-Demand (BigQuery) ~ $ 23,32

Service type: On-Demand
Amount of data queried: 1 TiB
Active logical storage: 1 TiB
Location type: Region
Location: Iowa (us-central1)

#### Cloud Scheduler ~ $288
US$ 0,10 per job/month
96 executions per day (every 15 minutes) * 30 = 2880.
Estimated Monthly Cost = 2,880 * $0.10 = $288


#### Dataflow ~ ?
Price estimative under request.