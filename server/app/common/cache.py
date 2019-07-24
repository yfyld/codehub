from flask_cache import Cache
from flask import request
import urllib

cache = Cache()

def cache_key():
  args = request.args
  key = request.path + '?' + urllib.urlencode([
      (k, v) for k in sorted(args) for v in sorted(args.getlist(k))
  ])
  return key
