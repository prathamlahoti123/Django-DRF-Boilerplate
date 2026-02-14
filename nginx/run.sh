#!/bin/sh

set -e

envsubst '${BACKEND_HOSTNAME}' < default.conf.tpl > conf.d/default.conf
nginx -g 'daemon off;'
