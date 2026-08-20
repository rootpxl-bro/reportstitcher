"""Orchestrates read, transform, write for ReportStitcher."""

from .reader import Reader
from .processor import normalize, enrich
from .writer import Writer


def run_pipeline(source, target):
 rows = Reader(source).read()
 rows = enrich(normalize(rows))
 Writer(target).write(rows)
 return len(rows)