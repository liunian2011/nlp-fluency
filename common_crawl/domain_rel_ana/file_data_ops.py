import os
import json

def merge_all_json_files(input_meta_file_path:str, out_folder:str, in_foler:str, target_file_path:str):
    with open(input_meta_file_path, 'r') as f:
        for line in f:
            meta_info = json.loads(line)
            domain = meta_info['domain']
            out_full_path = os.path.join(out_folder, '{0}.json'.format(domain))
            in_full_path = os.path.join(in_foler, '{0}.json'.format(domain))

            with open(out_full_path, 'r') as f:
                out_file_content = json.load(f)
            with open(in_full_path, 'r') as f:
                in_file_content = json.load(f)

            meta_info.update(out_file_content)
            meta_info.update(in_file_content)

            with open(target_file_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(meta_info) + '\n')


def find_hyperlink_not_in_cc(domain_hyperlink_file_path:str, all_cc_domain_file_path:str):
    all_cc_domain_set = set()
    with open(all_cc_domain_file_path, 'r') as f:
        for line in f:
            domain = line.split(',')[0].strip()
            all_cc_domain_set.add(domain)
    print(f'all cc domain size:{len(all_cc_domain_set)}')

    next_and_pre_domain_set = set()
    with open(domain_hyperlink_file_path, 'r') as f:
        for line in f:
            domain_line = json.loads(line)
            next_domains = domain_line['next_domains']
            pre_domains = domain_line['pre_domains']
            next_and_pre_domain_set.update(next_domains)
            next_and_pre_domain_set.update(pre_domains)
    print(f'all hyperline domain size:{len(next_and_pre_domain_set)}')

    hyperlink_domain_not_include_cc_domain_set = next_and_pre_domain_set - all_cc_domain_set
    print(f'next and pre link domain not in download cc domain size:{len(hyperlink_domain_not_include_cc_domain_set)}')
    print(f'{hyperlink_domain_not_include_cc_domain_set}')

    cc_domain_not_include_hyperlink_domain_set = all_cc_domain_set - next_and_pre_domain_set
    print(f'cc domain not include in hyperlink domain size:{len(cc_domain_not_include_hyperlink_domain_set)}')
    print(f'{cc_domain_not_include_hyperlink_domain_set}')



if __name__ == "__main__":
    input_meta_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/metadata_top_10000.jsonl'
    out_folder = '/mnt/geogpt/liunian/domain_analysis/websearch/out_degree_output/'
    in_folder = '/mnt/geogpt/liunian/domain_analysis/websearch/in_degree_output'
    target_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/domain_link_top_10000.jsonl'
    #merge_all_json_files(input_meta_file_path, out_folder, in_folder, target_file_path)

    all_cc_domain_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/top_domain.csv'
    find_hyperlink_not_in_cc(target_file_path, all_cc_domain_file_path)
