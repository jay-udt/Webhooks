import sys
import requests


def github_create_webhooks(owner, repo, secret_token, webhook_url):
    hook = {u'name': u'web', u'active': True, u'config': {u'url': webhook_url}}
    p = requests.post(
        'https://api.github.com/repos/' + owner + '/' + repo + '/hooks',
        json=hook,
        headers={'content-type': 'application/json', 'Authorization': 'token ' + secret_token})
    if p.ok:
        print("Webhook created successfully")
    else:
        p.raise_for_status()


def gitlab_create_webhooks(project_id, secret_token, webhook_url):
    p = requests.post(
        'https://gitlab.com/api/v4/projects/' + project_id + '/hooks?url=' + webhook_url,
        headers={'content-type': 'application/json', 'PRIVATE-TOKEN': secret_token})
    if p.ok:
        print("Webhook created successfully")
    else:
        p.raise_for_status()


def process_arguments(value):
    if not value:
        raise Exception("Command line arguments needs be provided")
    if "github" in value:
        github_create_webhooks(value[1], value[2], value[3], value[4])
    elif "gitlab" in value:
        gitlab_create_webhooks(value[1], value[2], value[3])


if __name__ == '__main__':
    process_arguments(sys.argv[1:])
