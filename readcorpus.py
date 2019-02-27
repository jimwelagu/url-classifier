#!/usr/bin/python

import json, sys, getopt, os
from urlclassifier import URLClassifier

def usage():
  print("Usage: %s --file=[filename]" % sys.argv[0])
  sys.exit()

def main(argv):

  file=''

  myopts, args = getopt.getopt(sys.argv[1:], "", ["file="])

  for o, a in myopts:
    if o in ('-f, --file'):
      file=a
    else:
      usage()

  if len(file) == 0:
    usage()

  corpus = open(file)
  urldata = json.load(corpus, encoding="latin1")

  m_urls = 0
  s_urls = 0

  for record in urldata:
    url_classifier = URLClassifier(record["url"])
    url_classifier.set_domain_age(record["domain_age_days"])
    url_classifier.set_alexa_rank(record["alexa_rank"])
    url_classifier.set_non_standard_port(record["default_port"], record["port"])
    url_classifier.set_file_extension(record["file_extension"])
    if not record["ips"]:
        url_classifier.set_no_ip_address()

    if url_classifier.isMalicious():
        m_urls += 1
    else:
        s_urls += 1

    print("{}, {}".format(url_classifier.url, url_classifier.isMalicious()))

  print("Malicious: {}, Safe: {}".format(m_urls, s_urls))

  corpus.close()

if __name__ == "__main__":
  main(sys.argv[1:])
