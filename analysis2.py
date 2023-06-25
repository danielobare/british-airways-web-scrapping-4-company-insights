import xlrd
givenWord =input("Enter some random word = ")

# storing the frequency of the given word in a variable
frequency_count =0

# input excel file path
inputExcelFile ="BA_reviews_1.csv"

# Creating a workbook
new_workbook=xlrd.open_workbook(inputExcelFile)

# Opening the first worksheet in the workbook
firstWorksheet=new_workbook.sheet_by_index(0)

# Traversing in all the rows of the worksheet

# (nrows is used to get the number of rows)
for each_row in range (firstWorksheet.nrows):

   # Traversing in all the columns of the worksheet

   # (ncols is used to get the number of columns)
   for each_col in range (firstWorksheet.ncols):

      # Checking whether each cell value is equal to the given word
      if(firstWorksheet.cell_value(each_row, each_col)==givenWord):

         # Incrementing the frequency count by 1
         frequency_count= frequency_count+1

# Printing count of the given word frequency
print("The frequency count of the given word {",givenWord,"} = ", frequency_count)