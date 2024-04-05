import requests
import re


class RequestGuard:
    def __init__(self, domain):
        """
        Initializes the thingy and then parses the list for the sucky paths
        """
        self.domain = domain
        self.forbidden = self.parse_robots()

    def parse_robots(self):
        """
        gets robots.txt, parses it, then gives a list of sucky paths
        """
        forbidden = []
        try:
            robots_url = f"{self.domain}/robots.txt"
            response = requests.get(robots_url)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    # Use regex to match lines that start with 'Disallow:' followed by any amount of
                    # whitespace, then capture the path
                    match = re.match(r'Disallow:\s*(.*)', line)
                    if match:
                        # If a match is found, append the whole path to the list of forbidden paths
                        forbidden.append(match.group(1))
        except Exception as e:
            print(f"Error fetching or parsing robots.txt: {e}")
        return forbidden


    def can_follow_link(self, url):
        """
        checks to see if it is allowed to be followed... duh
        """
        if not url.startswith(self.domain):
            return False
        for path in self.forbidden:
            # Ensure the path is checked immediately following the domain
            pattern = f"^{self.domain}{path}"
            if re.match(pattern, url):
                return False
        return True

    def make_get_request(self, *args, **kwargs):
        """
        Before asking for a webpage, we check if we're allowed to visit it.
        If we are, we go ahead and ask for it. If not, we don't do anything.
        """
        url = args[0]
        if self.can_follow_link(url):

            return requests.get(*args, **kwargs)
        else:
            return None


