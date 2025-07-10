import subprocess


def grep_match_result(match_pattern:str, file_path:str):
    index_pair_list = []

    try:
        result = subprocess.run(
            ["grep", match_pattern, file_path],
            timeout=120,
            check=True,
            capture_output=True,
            text=True
        )

        for line in result.stdout.split('\n'):
            item_list = line.strip().split()
            if len(item_list) == 2:
                item1 = item_list[0].strip()
                item2 = item_list[1].strip()
                index_pair_list.append((item1, item2))
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，返回码: {e.returncode}")
        print(f"错误输出: {e.stderr}")
        print(f'输出：{e.stdout}')

    return index_pair_list

if __name__ == "__main__":
    pattern1 = '^251524\s'
    file_path = '/mnt/geogpt/liunian/domain_analysis/data/pld-arc'
    result = grep_match_result(pattern1, file_path)
    print(result)