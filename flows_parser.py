import json
from flow import Flow


class FlowParser:
    @staticmethod
    def parse_flows_from_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)

            bandwidth = data["bandwidth"]
            flows_data = data["flows"]

            flows = [
                Flow(
                    flow_data["deadline"],
                    flow_data["period"],
                    ((flow_data["size"] * 8) / bandwidth) * 1000
                )
                for flow_data in flows_data
            ]

        return flows