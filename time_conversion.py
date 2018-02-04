# Works only when the site parsed is in Estonian

month_to_number_dict = {"jaanuar":      "01",
                        "veebruar":     "02",
                        "märts":        "03",
                        "aprill":       "04",
                        "mai":          "05",
                        "juuni":        "06",
                        "juuli":        "07",
                        "august":       "08",
                        "september":    "09",
                        "oktoober":     "10",
                        "november":     "11",
                        "detsember":    "12" }

def convert_post_date_to_sortable_format(time):
  #\d+\. [a-zA-Z]+ \d\d\d\d \d\d:\d\d'
  time = time.split(" ")
  time[0] = time[0].strip(".")
  time[1] = month_to_number_dict[time[1]]

  # YYYY-MM-DD-hh-mm
  return time[2] +"-"+ time[1] +"-"+ time[0] +"-"+ time[3]