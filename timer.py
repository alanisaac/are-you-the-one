import contextlib
import cProfile
from dataclasses import dataclass
import time

@dataclass
class Timespan:
    elapsed: float = 0

@contextlib.contextmanager
def start(profile: bool = False) -> Timespan:
    t = Timespan()
    start = time.perf_counter()
    context = cProfile.Profile() if profile else contextlib.nullcontext()
    with context as pr:
        yield t
    if pr:
        pr.print_stats(sort='time')
    end = time.perf_counter()
    t.elapsed = end
