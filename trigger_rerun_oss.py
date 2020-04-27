import sys
import argparse
import requests


OSS_SERVER = r'https://bios-ci.intel.com'


def trigger_rerun_oss_task(task_id, rerun_all):
    url = r'{}/app/rest/rerun_auto_task/?auto_task_id={}&rerun_all={}'.format(OSS_SERVER, task_id, rerun_all)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print(res.content)
            sys.exit(0)
        else:
            sys.exit(res.content)
    except Exception as e:
        sys.exit('exception {} happens when request url {}'.format(e, url))


def main():
    parser = argparse.ArgumentParser(
        prog='trigger_rerun_oss.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='',
        epilog='')
    parser.add_argument('--task_id', required=True)
    parser.add_argument('--rerun_all', required=True)
    args = parser.parse_args()
    trigger_rerun_oss_task(args.task_id, args.rerun_all)


if __name__ == '__main__':
    main()
