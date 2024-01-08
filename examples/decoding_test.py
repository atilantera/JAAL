# Tests JAAL 2.0 data decoding

import base64
import html
import json
import zlib

# Load test file
infilepath = "Prim+Binheap1.json"
outfilepath = "Prim+Binheap1-decoded.json"
f = open(infilepath)
fl = f.readlines()
f.close()
grading_data = json.loads(fl[0])

for key in ['description', 'generator', 'encoding']:
    print("grading_data['{}']: {}".format(key, grading_data[key]))
print("grading_data['data'] (first and last 8 characters): {} ... {}".format(
    grading_data['data'][0:8], grading_data['data'][-8:]))
print("len(grading_data['data']: {}".format(len(grading_data['data'])))

# Extract JAAL data field
jaal_data = grading_data['data']
jaal_data = bytes(jaal_data, encoding='ascii')
print("type(jaal_data): {}\nlen(jaal_data): {} (Note: base64 encoded)".format(
    type(jaal_data), len(jaal_data)))

# Base64 decode
decoded = base64.decodebytes(jaal_data)
print("type(decoded): {}\nlen(decoded): {}".format(type(decoded),
                                                      len(decoded)))

# zlib decompress
unzipped = zlib.decompress(decoded)
print("type(unzipped): {}\nlen(unzipped): {}".format(type(unzipped),
                                                      len(unzipped)))
print("unzipped (first and last 8 bytes): {} ... {}".format(
    unzipped[0:8], unzipped[-8:]))

unzipped_str = str(unzipped)
print("unzipped str (first and last 8 bytes): {} ... {}".format(
    unzipped_str[0:8], unzipped_str[-8:]))

print("Strip \"b'\" from beginning and \"'\" from end.")
unzipped_str = unzipped_str[2:-1]
print("unzipped str (first and last 8 bytes): {} ... {}".format(
    unzipped_str[0:8], unzipped_str[-8:]))

# HTML de-escape
unescaped = html.unescape(unzipped_str)
print("type(unescaped): {}\nlen(unescaped): {}".format(type(unescaped),
                                                      len(unescaped)))
print("unzipped str (first and last 8 bytes): {} ... {}".format(
    unescaped[0:8], unescaped[-8:]))

print("unescaped str, characters 1500-1564:\n{}".format(unescaped[1500:1565]))
print("unescaped str, characters 1565-1599:\n{}".format(unescaped[1565:1600]))
print("unescaped str, characters 1562-1566: {} {} {} {} {} {}".format(
    unescaped[1562], unescaped[1563], unescaped[1564], unescaped[1565],
    unescaped[1566], unescaped[1567]))

# SVG inside JAAL is double escaped. Replace literal three-character substrings
# \\" with two-character substring \" .
print(r'Replacing literal \\" with \".')
unescaped = unescaped.replace(r'\\"', r'\"')

print("unescaped str, characters 1500-1564:\n{}".format(unescaped[1500:1565]))
print("unescaped str, characters 1565-1599:\n{}".format(unescaped[1565:1600]))
print("unescaped str, characters 1562-1566: {} {} {} {} {} {}".format(
    unescaped[1562], unescaped[1563], unescaped[1564], unescaped[1565],
    unescaped[1566], unescaped[1567]))

f = open(outfilepath, 'w')
f.write(unescaped)
f.close()

# Parse as JSON
jaal_recording = json.loads(unescaped)

print("-----------------------------------------")
print("JAAL parsed as JSON:")
print("metadata: {}".format(jaal_recording['metadata']))
