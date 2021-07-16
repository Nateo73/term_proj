import csv
from pprint import pprint
OBJECT_ID_INDEX = 0
MAINT_ID_INDEX = 1
GROUND_NAME_INDEX = 2
AREA_SIZE_INDEX = 3
RESPONSIBLITY_INDEX = 4
AO_INDEX = 5
BRIGADE_INDEX = 8

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.

def main():
  mow_areas = read_compound_list("mow_area.csv")
  print_list(mow_areas)
  responsiability = lambda respo: respo[RESPONSIBLITY_INDEX]
  print (responsiability)
  acre = lambda acarea: acarea[AREA_SIZE_INDEX]
  id_sorted = sorted(mow_areas, key=acre)

  for i in id_sorted:
        print (i[4])
  acres_list = create_acre_list(mow_areas)
  total_acres = sum(acres_list)

  print (total_acres)
  

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list
def print_list(compound_list):
  for i in compound_list:
    print (i)
def create_acre_list(compound_list):
      
      acres= []
      float_acres=[]
      acre = lambda acarea: acarea[AREA_SIZE_INDEX]
      a_sorted = sorted(compound_list,key=acre)
      
      for a in a_sorted:     
        acres.append(a[4])
      for item in acres:
            float_acres.append(float(item))
      return float_acres
main()