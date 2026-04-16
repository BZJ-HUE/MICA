#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MICA
====

A Cross-Modal Multi-View Contrastive Learning Framework for Spatial Multi-Omics Integration.

This package provides:
- model training interface
- encoder architecture
- preprocessing functions
- clustering and visualization utilities
"""

__title__ = "MICA"
__version__ = "1.0.0"
__description__ = "A Cross-Modal Multi-View Contrastive Learning Framework for Spatial Multi-Omics Integration"

from .MICA_pyG import Train_MICA
from .model import Encoder_overall
from .preprocess import (
    adjacent_matrix_preprocessing,
    clr_normalize_each_cell,
    construct_neighbor_graph,
    cross_modal_feature_fusion,
    fix_seed,
    lsi,
    pca,
)
from .utils import (
    clustering,
    evaluate_fusion_effect,
    mclust_R,
    plot_weight_value,
    search_res,
    visualize_fusion_comparison,
)

__all__ = [
    "Train_MICA",
    "Encoder_overall",
    "adjacent_matrix_preprocessing",
    "clr_normalize_each_cell",
    "construct_neighbor_graph",
    "cross_modal_feature_fusion",
    "fix_seed",
    "lsi",
    "pca",
    "clustering",
    "evaluate_fusion_effect",
    "mclust_R",
    "plot_weight_value",
    "search_res",
    "visualize_fusion_comparison",
]
