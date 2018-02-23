# !/usr/bin/env python3

## Best to assign a @daily cronjob for this script.

from persistence import delete_expired_entries

def main():
	delete_expired_entries()

if __name__ == '__main__':
	main()