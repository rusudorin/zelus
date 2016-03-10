#!/usr/bin/env bash
while sleep 1 ; do echo `date '+%Y%m%d.%H%M%S'` `vmstat | head -3 | tail -1` ; done