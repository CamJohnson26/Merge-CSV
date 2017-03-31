import os

current_metric = "impressions"
header = None					 # Replace header with "column_name1,column_name2\n". MAKE SURE NUMBER OF COLUMNS MATCHES NUMBER OF HEADER COLUMNS

folders = []

current_folder = os.getcwd() # This is the folder the python script is running in
all_items = os.listdir(current_folder)
for item in all_items:
	if(not os.path.isfile(item)):
		folders.append(item)

folders.remove(".git")

for folder in folders:
	new_file = open(os.path.join(current_folder, current_metric + folder + ".csv"), 'w')

	all_files_in_folder = os.listdir(os.path.join(current_folder, folder))
	for index, file in enumerate(all_files_in_folder):

		file_contents = open(os.path.join(current_folder, folder, file), 'r').readlines()

		if header is None:
			header = file_contents[0]
		if index == 0:
			new_file.writelines(header)
		for line in file_contents[1:]:
			new_file.writelines(line)
		new_file.write("\n")


