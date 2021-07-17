# WeChat/WeCom Token Central Administration

The Ultimate [旺柴] and Powerful [旺柴] solution to WeChat/WeCom token management 

## Setup

1. Generate apikey, `python token_server.py`
2. Create a copy of the default config,  `cp sample.env .env`
3. Restrict env file permission, `chmod o-rwx .env`
4. Provide your apikey and url/id/secret in `.env`
5. Modify sample `wxtoken.service` and enable it

## Usage

```shell
$ python token_server.py

$ curl http://<host>:<port>/<apikey>/
{"access_token": "current access_token"}
```

## Run without `systemd`

```bash
source load_env.sh
python token_server.py
```

## Todo

- [ ] Error Handling
- [ ] Watch Dog [旺柴]
