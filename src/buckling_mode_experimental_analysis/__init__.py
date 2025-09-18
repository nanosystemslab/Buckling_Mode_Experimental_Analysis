"""
Buckling Mode Experimental Analysis

A package for analyzing buckling test data and extracting maximum force values.
"""

from .cli import (
    load_file_TT,
    extract_max_force_from_df,
    process_csv_files,
    generate_summary_report,
    main,
)

__version__ = "0.1.0"
__all__ = [
    "load_file_TT",
    "extract_max_force_from_df", 
    "process_csv_files",
    "generate_summary_report",
    "main",
]
