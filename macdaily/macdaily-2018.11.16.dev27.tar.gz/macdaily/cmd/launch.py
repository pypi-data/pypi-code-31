# -*- coding: utf-8 -*-

import collections
import getpass
import os
import plistlib
import pwd

from macdaily.util.const import ROOT, bold, red, reset
from macdaily.util.misc import (make_stderr, print_info, print_misc,
                                print_scpt, print_term)

try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess


def run_script(argv, quiet, verbose):
    args = ' '.join(argv)
    print_scpt(args, os.devnull, verbose)
    try:
        subprocess.check_call(argv, stdout=subprocess.DEVNULL, stderr=make_stderr(quiet))
    except subprocess.CalledProcessError:
        text = "macdaily: {}launch{}: command `{}{!r}{} failed".format(red, reset, bold, args, reset)
        print_term(text, os.devnull, quiet)
        raise


def launch_askpass(quiet=False, verbose=False):
    text = 'Launching MacDaily SSH-AskPass program'
    print_info(text, os.devnull, quiet)

    path = 'Macintosh HD{}:img:askpass.icns'.format(ROOT.replace(os.path.sep, ":"))
    ASKPASS = ['#!/usr/bin/env osascript',
               '',
               '-- script based on https://github.com/theseal/ssh-askpass',
               '',
               'on run argv',
               '    set args to argv as text',
               '    if args starts with "--help" or args starts with "-h" then',
               '        return "macdaily-askpass [-h|--help] [prompt]"',
               '    end if',
               '    display dialog args with icon file ("{}") default button "OK" default answer "" with hidden answer'.format(path),  # noqa
               "    return result's text returned",
               'end run',
               '']
    askpass = os.path.join(ROOT, 'res', 'askpass.applescript')
    text = 'Making executable {!r}'.format(askpass)
    print_misc(text, os.devnull, verbose)

    user = getpass.getuser()
    owner = pwd.getpwuid(os.stat(askpass).st_uid).pw_name
    if user != owner:
        os.environ['SUDO_ASKPASS'] = askpass
        run_script(['sudo', '--askpass', 'chown', user, askpass], quiet, verbose)

    with open(askpass, 'w') as file:
        file.write(os.linesep.join(ASKPASS))
    run_script(['chmod', 'u+x', askpass], quiet, verbose)
    if user != owner:
        run_script(['chown', owner, askpass], quiet, verbose)

    PLIST = collections.OrderedDict(
        Label='com.macdaily.askpass',
        ProgramArguments=['/usr/bin/ssh-agent', '-l'],
        EnvironmentVariables=collections.OrderedDict(
            SSH_ASKPASS=askpass,
            DISPLAY=0,
        ),
        Sockets=collections.OrderedDict(
            Listeners=collections.OrderedDict(
                SecureSocketWithKey='SSH_AUTH_SOCK'
            )
        ),
        EnableTransactions=True,
    )
    plist = os.path.expanduser('~/Library/LaunchAgents/com.macdaily.askpass.plist')
    text = 'Adding Launch Agent {!r}'.format(plist)
    print_misc(text, os.devnull, verbose)
    if os.path.exists(plist):
        run_script(['launchctl', 'unload', '-w', plist], quiet, verbose)
    with open(plist, 'wb') as file:
        plistlib.dump(PLIST, file, sort_keys=False)
    run_script(['launchctl', 'load', '-w', plist], quiet, verbose)
    run_script(['ssh-add', '-c'], quiet, verbose)

    return askpass


def launch_confirm(quiet=False, verbose=False):
    text = 'Launching MacDaily Confirmation program'
    print_info(text, os.devnull, quiet)

    path = 'Macintosh HD{}:img:confirm.icns'.format(ROOT.replace(os.path.sep, ":"))
    ASKPASS = ['#!/usr/bin/env osascript',
               '',
               'on run argv',
               '    set args to argv as text',
               '    if args starts with "--help" or args starts with "-h" then',
               '        return "macdaily-confirm [-h|--help] [prompt]"',
               '    end if',
               '    display dialog args with icon file ("{}") default button "Cancel"'.format(path),
               "    return result's button returned",
               'end run',
               '']
    confirm = os.path.join(ROOT, 'res', 'confirm.applescript')
    text = 'Making executable {!r}'.format(confirm)
    print_misc(text, os.devnull, verbose)

    user = getpass.getuser()
    owner = pwd.getpwuid(os.stat(confirm).st_uid).pw_name
    if user != owner:
        os.environ['SUDO_ASKPASS'] = os.path.join(ROOT, 'res', 'askpass.applescript')
        run_script(['sudo', '--askpass', 'chown', user, confirm], quiet, verbose)

    with open(confirm, 'w') as file:
        file.write(os.linesep.join(ASKPASS))
    run_script(['chmod', 'u+x', confirm], quiet, verbose)
    if user != owner:
        run_script(['chown', owner, confirm], quiet, verbose)

    return confirm
