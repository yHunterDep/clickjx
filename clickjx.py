#!/usr/bin/python3

import argparse, requests

VR = "\033[31m"
VD = "\033[32m"
RS = "\033[0m"

def clicktest(domain):
        try:
                req = requests.get(domain, timeout=1)
                heds = req.headers
                vuln = True
                for hed in heds:
                        if "x-frame-options" in hed.lower():
                                vuln = False
                return vuln
        except Exception as x:
                pass

parser = argparse.ArgumentParser(description="ClickJackingTester Tool created by HunterDep")
parser.add_argument("-d", "--domain", help="Put the domain to test, ex: http://example.com/")
parser.add_argument("-f", "--file", help="Put the subdomains list file to test, ex: subdomains.txt")
args = parser.parse_args()

domain = args.domain
file = args.file
if domain and file:
        print(VR + "ERROR: -d OR -f" + RS);exit()

if domain:
        if not domain.startswith("http://") and not domain.startswith("https://"):
                domain = f"http://{domain}"

        atk = clicktest(domain)
        if atk:
                print(f"[{VR}clickjacking{RS}] {VD + domain + RS}")

if file:
        try:
                file_list = open(file, "r").readlines()
                file_list = [x.strip("\n") for x in file_list]

                for domain in file_list:
                        if not domain.startswith("http://") and not domain.startswith("https://"):
                                domain = f"http://{domain}"
                        atk = clicktest(domain)
                        if atk:
                                print(f"[{VR}clickjacking{RS}] {VD + domain + RS}")
        except:
                pass
