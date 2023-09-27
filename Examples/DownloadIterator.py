

from mpzinke import DownloadIterator
import requests


def print_callback(self):
	if(self._downloaded % 1048576 == 0):
		print(f"Downloaded {self._downloaded / 1048576} MB")


def main():
	# Open an HTTP request
	response: requests.Response = requests.get("https://speed.hetzner.de/100MB.bin", stream=True, timeout=21)
	# Wrap the request with DownloadIterator iterator.
	#  After 300 seconds of downloading, a TimeoutError will be thrown.
	#  With every chunk downloaded, the print_callback will be called.
	iterator = DownloadIterator(response, timeout=300, callback=print_callback)

	chunks = []
	# Download chunks by iterating through DownloadIterator object
	for chunk in iterator:
		if(chunk):
			chunks.append(chunk)

	file_bytes = b''.join(chunks)
	print(f"Downloaded: {len(file_bytes)}")


if __name__ == '__main__':
	main()
