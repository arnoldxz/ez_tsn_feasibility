
# %%
from math import ceil, gcd
import numpy as np

# %%
class FlowProcessor:
    @staticmethod
    def resolution(flows):
        return np.gcd.reduce([int(flow.traveltime) for flow in flows])

    @staticmethod
    def hyperperiod(periods):
        lcm = ceil(periods[0])
        for i in range(1, len(periods)):
            lcm = lcm * ceil(periods[i]) // gcd(lcm, ceil(periods[i]))
        return lcm

    @staticmethod
    def process_flows(flows):
        resolution = FlowProcessor.resolution(flows)
        cycle = FlowProcessor.hyperperiod([int(flow.period) for flow in flows])
        m = []
        tt_values = [int(flow.traveltime / resolution) for flow in flows]
        period_values = [int(flow.period / resolution) for flow in flows]
        iter_limit = int(cycle / resolution)
        print(f'\nNFlows({len(flows)})\nResolution:{resolution}\nCycle:{cycle}\nTravelTimes:{tt_values}\nPeriods:{period_values}\nIterLimit:{iter_limit}\n')
        for tt, period in zip(tt_values, period_values):
            v = [np.array([0], dtype=object)] * iter_limit
            indices = np.arange(0, iter_limit, period)
            for idx in indices:
                v[idx:idx+tt] = [np.array([1], dtype=object)] * tt
            m.append(v)
        return m
