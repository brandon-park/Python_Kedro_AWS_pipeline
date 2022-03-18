from kedro.pipeline import Pipeline, node

from .nodes import preprocessed_mercedes, preprocessed_hyundai, create_car_input_table


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocessed_hyundai,
                inputs="hyundai",
                outputs="preprocessed_hyundai",
                name="preprocessed_hyundai_node",
            ),
            node(
                func=preprocessed_mercedes,
                inputs="mercedes",
                outputs="preprocessed_mercedes",
                name="preprocessed_mercedes_node",
            ),
            node(
                func=create_car_input_table,
                inputs=["audi", "preprocessed_hyundai", "preprocessed_mercedes"],
                outputs="car_input_table",
                name="create_car_input_table_node",
            ),
        ]
    )
