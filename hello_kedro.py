from kedro.io import DataCatalog,MemoryDataSet
from kedro.pipeline import node,Pipeline
from kedro.runner import SequentialRunner

data_catalog =  DataCatalog({"my_salutation":MemoryDataSet()})

def return_greeting():
    return "Hello"

def join_statements(greeting):
    return f"{greeting} Kedro!"

pipeline = Pipeline([
        node(return_greeting,
            None,
            "my_salutation"
            ),
        node(join_statements,
            "my_salutation",
            "my_message"
            )
    ]
    )

runner = SequentialRunner()

print(runner.run(pipeline,data_catalog))


