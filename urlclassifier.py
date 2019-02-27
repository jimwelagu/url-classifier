
class URLClassifier:
    def __init__(self, url):
        self.url = url
        self.malScore = 0

    def set_domain_age(self, age):
        if (age < 547):
            self.malScore -= 1
        elif (547 < age < 1095):
            self.malScore += 1
        elif (age > 1095):
            self.malScore += 2

    def set_no_ip_address(self):
        self.malScore -= 1

    def set_ip_address(self):
            self.malScore += 1

    def set_alexa_rank(self, alexaRank):
        if(alexaRank < 1000000):
            self.malScore += 1
        else:
            self.malScore -= 1

    def set_file_extension(self, extension):
        if(extension == "exe"):
            self.malScore -= 1

    def set_non_standard_port(self, default_port, port):
        if(default_port != port):
            self.malScore -= 1

    def isMalicious(self):
        if(self.malScore <= 0):
            return 1
        else:
            return 0
