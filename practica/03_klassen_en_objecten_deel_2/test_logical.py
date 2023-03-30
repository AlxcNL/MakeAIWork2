#!/usr/bin/env python

from logical import *
import logging

logging.basicConfig(level=logging.INFO)

logging.info(logOr(False, False))