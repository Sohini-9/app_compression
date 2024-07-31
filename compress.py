import zlib,base64   #zlibis the library which contains the function compress for compressing the data
                     #base64 helps in the compression of the data   
data = open('demo.txt','r').read()
data_bytes = bytes(data,'utf-8')   #conversion of the string to the bytes
compressed_data = base64.b64encode(zlib.compress(data_bytes,9))    #compress accepts bytes data and not str, we also needs to mention the level of compression
decoded_data = compressed_data.decode('utf-8')
compressed_file = open('compressed.txt','w')
compressed_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)