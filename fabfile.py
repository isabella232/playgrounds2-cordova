#!/usr/bin/env python

from fabric.api import *

def build(platform=None):
    local('cordova build %s' % (platform or ''))

def ios():
    local('cordova emulate ios')

def android():
    local('cordova emulate android')
