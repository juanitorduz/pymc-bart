#   Copyright 2022 The PyMC Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import pymc as pm

from pymc_bart.bart import BART
from pymc_bart.pgbart import PGBART
from pymc_bart.utils import plot_convergence, plot_dependence, plot_variable_importance

__all__ = ["BART", "PGBART"]
__version__ = "0.3.2"


pm.STEP_METHODS = list(pm.STEP_METHODS) + [PGBART]
