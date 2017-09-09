#!/usr/bin/env python
# encoding: utf-8

import sys
import select
import json


def reverse(d):
    try:
        m = json.loads(d)
        print(json.dumps(m))
    except:
        try:
            with open(d) as f:
                m = json.load(f)
                print(json.dumps(m))
        except:
            sys.exit(1)


def beautify(d):
    try:
        m = json.loads(d)
        print(json.dumps(m, indent=4, sort_keys=True))
    except:
        try:
            with open(d) as f:
                m = json.load(f)
                print(json.dumps(m, indent=4, sort_keys=True))
        except:
            sys.exit(1)


if __name__ == '__main__':
    reversed = False

    if len(sys.argv) == 2:
        if sys.argv[1] == "-r":
            reversed = True
        else:
            beautify(sys.argv[1])
            sys.exit(1)
    elif len(sys.argv) > 2:
        if "-r" in sys.argv:
            reversed = True
        if not reversed:
            beautify(sys.argv[1])
        elif sys.argv[1] == "-r":
            reverse(sys.argv[2])
        elif sys.argv[2] == '-r':
            reverse(sys.argv[1])
        sys.exit(0)

    try:
        if "-r" in sys.argv:
            reversed = True
        r, _, _ = select.select([sys.stdin], [], [], 0.1)
        if sys.stdin in r:
            d = sys.stdin.buffer.read()
            if reversed:
                reverse(d)
            else:
                beautify(d)
            sys.exit(0)
    except:
        pass

