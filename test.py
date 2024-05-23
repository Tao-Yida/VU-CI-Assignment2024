import h5py

# Function to read name information
def read_name(file, index):
    name_ref = file['digitStruct']['name'][index][0]
    name = ''.join(chr(file[name_ref][i][0]) for i in range(len(file[name_ref])))
    return name

# Function to read bbox information with proper data type handling
def read_bbox(file, index):
    bbox = {}
    item = file[file['digitStruct']['bbox'][index][0]]
    for key in ['label', 'left', 'top', 'width', 'height']:
        attr = item[key]
        bbox[key] = [file[attr[i][0]][0][0] for i in range(len(attr))]
    # Convert label to integer
    bbox['label'] = [int(l) for l in bbox['label']]
    return bbox

# Load the .mat file
file_path = '../SVHN_data/train/digitStruct.mat'
mat = h5py.File(file_path, 'r')

# Read the name and bbox information for the first image
first_name = read_name(mat, 0)
first_bbox = read_bbox(mat, 0)

print(first_name)
print(first_bbox)
