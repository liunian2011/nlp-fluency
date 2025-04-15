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
        MinhashDedupSignature(output_folder="signatures/", config=minhash_config, language=Languages.english ),
    ]

    pipeline_4 = [
        MinhashDedupBuckets( input_folder="signatures/", output_folder="buckets/", config=minhash_config, ),
    ]

    pipeline_5 = [
        MinhashDedupCluster( input_folder="buckets/", output_folder="remove_ids/", config=minhash_config, ),
    ]

    pipeline_6 = [
        JsonlReader(local_datafolder, glob_pattern="*.jsonl"),
        TokensCounter(),
        MinhashDedupFilter( input_folder="remove_ids/", exclusion_writer=JsonlWriter("removed/"), ),
        JsonlWriter("final_output"),  # save the final filtered output to disk
    ]

    executor_3: PipelineExecutor = LocalPipelineExecutor(pipeline=pipeline_3, workers=TOTAL_WORKERS, tasks=TOTAL_TASKS)

    executor_4: PipelineExecutor = LocalPipelineExecutor(pipeline=pipeline_4, workers=TOTAL_WORKERS, tasks=TOTAL_TASKS)

    executor_5: PipelineExecutor = LocalPipelineExecutor(pipeline=pipeline_5, workers=1, tasks=1)

    executor_6: PipelineExecutor = LocalPipelineExecutor(pipeline=pipeline_6, workers=TOTAL_WORKERS, tasks=TOTAL_TASKS)

    print(executor_3.run())
    print(executor_4.run())
    print(executor_5.run())
    print(executor_6.run())


if __name__ == "__main__":
    run_example()

