##  Convert database data with old end_date format 
## to new end_date format
# Old end_date format: dd.mm.YYYY
# New end_date format: YYYY.mm.dd
#
#  this makes the end_date alphabetically sortable with
# sql query

from persistence import save, load, Columns
from time_conversion import convert_end_date_to_sortable_format


def convert_end_date():
	job_postings = load()

	altered_job_postings = []
	for post in job_postings:
		post = list(post)
		post[Columns.end_date] = convert_end_date_to_sortable_format(post[Columns.end_date])
		altered_job_postings += [tuple(post)]
	save(altered_job_postings)


def main():
	convert_end_date()

if __name__ == '__main__':
	main()