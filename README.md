# WeChat/WeCom Token Central Administration

The Ultimate [旺柴] and Powerful [旺柴] solution to WeChat/WeCom token management 

## Installation

Pure standard library. Just get and run.

## Setup

1. Generate apikey, `python token_server.py`
2. Create a copy of the default config,  `cp config.sample.ini config.ini`
3. Provide your apikey and url/id/secret in `config.ini`

## Usage

```shell
$ python token_server.py

$ curl http://<host>:<port>/<apikey>/
{"access_token": "current access_token"}
```

## Todo

- [ ] Error Handling
- [ ] Watch Dog [旺柴]
