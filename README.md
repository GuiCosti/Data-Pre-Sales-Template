# Data-Pre-Sales-Template
Pre-sales architecture template divided in three parts: an analytical insights module, data engineering module and architecture for the solution module.

### Project Content

This project is composed by 3 main parts and they are all under ther *src* (source) folder.

1. *01_anomaly_report*: In this part, there is an exploratory notebook, named *eda.ipynb*. There is also a markdown file with the final report, named *anomaly_report.md*
2. *02_engineering*: This folder contains a data engineering script called *json_to_df_transformer.py*. To execute this script, install de dependencies and proceed to startup instructions below.
3. *03_architecture*: This part contains a architecture template for this project. The *architecture.drawio* is the source architecture file, the *architecture.png* is the rendered image of the source file and the *architecture_description.md* is the breakdown comments.

**Other Parts:**

- *data*: This folder contains the datasets used on this project
- *img*: This folder constains the images used on this project


### Installing Dependencies

On the root directory of the project, execute the command below on the terminal

```bash
pip3 install -r requirements.txt
```

### Startup

To execute the *json_to_df_transformer.py* script, set the path to the engineering folder

```bash
cd src/02_engineering
```

and than execute the python script on the terminal


```bash
python3 json_to_df_transformer.py
```

### Output

The function returns two dataframes, one with the expanded json nested objects in the same frame and the other is a dataframe with the nested object only, with an index column to link the original frame (extracted)


##### Expanded

| CreateDate             | EmissionDate          | Discount | NFeNumber | ProductName   | Value | Quantity | NFeID |
|------------------------|-----------------------|----------|-----------|---------------|-------|----------|-------|
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 501       | Rice          | 35.55 | 2        | 1     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 501       | Flour         | 11.55 | 5        | 1     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 501       | Bean          | 27.15 | 7        | 1     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 502       | Tomate        | 12.25 | 10       | 2     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 502       | Pasta         | 7.55  | 5        | 2     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 503       | Beer          | 9.00  | 6        | 3     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 503       | French fries  | 10.99 | 2        | 3     |
| 2021-05-24T20:21:34.79 | 2021-05-24T00:00:00   | 0.0      | 503       | Ice cream     | 27.15 | 1        | 3     |

##### Extracted

| ProductName   | Value | Quantity | NFeID |
|---------------|-------|----------|-------|
| Rice          | 35.55 | 2        | 1     |
| Flour         | 11.55 | 5        | 1     |
| Bean          | 27.15 | 7        | 1     |
| Tomate        | 12.25 | 10       | 2     |
| Pasta         | 7.55  | 5        | 2     |
| Beer          | 9.00  | 6        | 3     |
| French fries  | 10.99 | 2        | 3     |
| Ice cream     | 27.15 | 1        | 3     |


### References

<a href="https://teaching.cornell.edu/teaching-resources/engaging-students/problem-based-learning#:~:text=Problem%2Dbased%20learning%20(PBL),the%20motivation%20and%20the%20learning.">Problem Based Learning</a>
- Examine and define the problem.
- Explore what they already know about underlying issues related to it.
- Determine what they need to learn and where they can acquire the information and tools necessary to solve the problem.
- Evaluate possible ways to solve the problem.
- Solve the problem.
- Report on their findings.

### Next Steps
- Add docstring, git pre-commit syntax reviewer, pep8 style guide
- Apply Outliers and Anomaly Detection Model
- Add Docker infrastrucute
- Add Unit/Integration tests to engineering part
- Add Build/CI/CD Pipeline