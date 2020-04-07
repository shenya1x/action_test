import argparse
import requests


OSS_SERVER = r'https://bios-ci.intel.com'


def trigger_rerun_oss_task(task_id, rerun_all):
    print('task_id:{}'.format(task_id))
    print('rerun_all:{}'.format(rerun_all))
    url = r'{}/app/rest/rerun_auto_task/?auto_task_id={}&rerun_all={}'.format(OSS_SERVER, task_id, rerun_all)
    # res = requests.get(url)
    # print(res.content)
    # request = urllib2.Request(url)
    # response = urllib2.urlopen(request)
    # response_data = response.read()
    # response.close()
    # print response_data


def main():
    parser = argparse.ArgumentParser(
        prog='trigger_rerun_oss.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='',
        epilog='')

    parser.add_argument('-t', '--task_id')
    parser.add_argument('-r', '--rerun_all')
    args = parser.parse_args()
    trigger_rerun_oss_task(args.task_id, args.rerun_all)


if __name__ == '__main__':
    main()
