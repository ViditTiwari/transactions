from .settings import DATA_PATH, data_file
import os

def get_path(file_name):
    return os.path.join(DATA_PATH, file_name)


def get_analytics():
	basic_info = {'orders_no' : 0 , 'total_amount' : 0, 'names_one_order': []}
	distribution = {'1':0, '2':0, '3':0, '4':0, '5+':0}

	unique_records = []

	with open(get_path(data_file)) as customer_records:
		for row_num, record in enumerate(customer_records):
			if row_num != 0 and record.strip():
				record_data = [data.strip() for data in record.strip().split(',')]
				basic_info['orders_no'] +=1
				basic_info['total_amount'] += int(record_data[3])
				if unique_records:
					for unique_record in unique_records:
						if record_data[1] == unique_record[0] and record_data[2] == unique_record[1]:
							unique_record[2] +=1
							break
							
					else:
						unique_records.append([record_data[1], record_data[2], 1])

				else:
					unique_records.append([record_data[1], record_data[2], 1])

	for unique_record in unique_records:
		if unique_record[2] == 1:
			basic_info['names_one_order'].append(unique_record[1])
			distribution['1'] +=1
		elif unique_record[2] == 2:
			distribution['2'] +=1
		elif unique_record[2] == 3:
			distribution['3'] +=1
		elif unique_record[2] == 4:
			distribution['4'] +=1
		else:
			distribution['5+'] +=1

	context = {'basic_info' : {**basic_info}, 'distribution': {**distribution}}
	return context
				