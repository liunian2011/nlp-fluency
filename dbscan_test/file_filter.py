from datatrove.executor.base import PipelineExecutor
from datatrove.io import get_datafolder
from datatrove.executor.local import LocalPipelineExecutor
from datatrove.pipeline.tokens import TokensCounter
from datatrove.pipeline.readers import JsonlReader
from datatrove.pipeline.writers.jsonl import JsonlWriter
from datatrove.utils.typeshelper import Languages
from datatrove.utils.hashing import HashConfig
from datatrove.pipeline.dedup.minhash import (
    MinhashDedupSignature,
    MinhashConfig,
    MinhashDedupBuckets,
    MinhashDedupCluster,
    MinhashDedupFilter,
)
from datatrove.pipeline.filters import (
    C4QualityFilter,
    FineWebQualityFilter,
    GopherQualityFilter,
    GopherRepetitionFilter,
    LanguageFilter,
    URLFilter,
)


minhash_config = MinhashConfig(
    hash_config=HashConfig(precision=64),
    num_buckets=10,
    hashes_per_bucket=8,
)  # better precision -> fewer false positives (collisions)

FINDER_WORKERS = 10  # this will speed up/parallelize step 2
TOTAL_TASKS = 20
TOTAL_WORKERS = 20

def run_example():
    # 创建本地文件夹的数据源
    local_datafolder = get_datafolder("intermediate")

    pipeline_3 = [
        JsonlReader(local_datafolder, glob_pattern="*.jsonl"),
        LanguageFilter(
            exclusion_writer=JsonlWriter(
                f"2_non_english/",

            )
        ),
        GopherRepetitionFilter(
            exclusion_writer=JsonlWriter(f"3_gopher_rep/")
        ),
        JsonlWriter("filter_output"),  # save the final filtered output to disk
    ]

    executor_6: PipelineExecutor = LocalPipelineExecutor(pipeline=pipeline_3, workers=TOTAL_WORKERS, tasks=TOTAL_TASKS)

    print(executor_6.run())


if __name__ == "__main__":
    run_example()

