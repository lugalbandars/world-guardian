import requests


class SessionCreator:

    @staticmethod
    def create(proxy=None) -> requests.Session:
        """Create a requests.Session instance with customizable configuration"""
        session = requests.Session()
        if proxy:
            session.proxies = {
                'http': proxy,
                'https': proxy,
            }

        session.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/" \
                                    "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        session.headers['Accept-Encoding'] = "gzip, deflate, br"
        session.headers['Accept-Language'] = "en-US,en;q=0.5"
        session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                                        "(KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        return session
