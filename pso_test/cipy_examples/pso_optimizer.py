# Copyright 2016 Andrich van Wyk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cipy.algorithms.core import max_iterations
from cipy.benchmarks.functions import sphere
from cipy.optimizers.pso_optimizer import PSOOptimizer


def main(dimension, iterations):
    """ Main function for PSO optimizer example.

    Instantiate PSOOptimizer to optimize 30-dimensional spherical function.
    """
    optimizer = PSOOptimizer()
    solution = optimizer.minimize(sphere, -5.12, 5.12, dimension,
                                  max_iterations(iterations))
    return solution, optimizer


if __name__ == "__main__":
    # solution, optimizer = main(30, 1000)
    solution, optimizer = main(2, 1000)
    print(solution)
    print(optimizer.accuracy())
