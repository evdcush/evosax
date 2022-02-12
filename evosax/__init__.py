from .strategy import Strategy
from .utils import FitnessShaper, ParameterReshaper

from .strategies import (
    Simple_GA,
    Simple_ES,
    CMA_ES,
    Differential_ES,
    PSO_ES,
    Open_ES,
    PEPG_ES,
    PBT_ES,
    Persistent_ES,
    xNES,
    Augmented_RS,
)


Strategies = {
    "Simple_GA": Simple_GA,
    "Simple_ES": Simple_ES,
    "CMA_ES": CMA_ES,
    "Differential_ES": Differential_ES,
    "PSO_ES": PSO_ES,
    "Open_ES": Open_ES,
    "PEPG_ES": PEPG_ES,
    "PBT_ES": PBT_ES,
    "Persistent_ES": Persistent_ES,
    "xNES": xNES,
    "Augmented_RS": Augmented_RS,
}

__all__ = [
    "Strategy",
    "Simple_GA",
    "Simple_ES",
    "CMA_ES",
    "Differential_ES",
    "PSO_ES",
    "Open_ES",
    "PEPG_ES",
    "PBT_ES",
    "Persistent_ES",
    "xNES",
    "Augmented_RS",
    "Strategies",
    "FitnessShaper",
    "ParameterReshaper",
]
