import os
import json
import base64
from glob import glob

class FileInterface:
    def __init__(self):
        os.makedirs('files', exist_ok=True)  # Pastikan direktori files ada
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if filename == '':
                return dict(status='ERROR', data='Filename kosong')
            with open(filename, 'rb') as fp:
                isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))
            
    def upload(self, params=[]):
        try:
            filename = params[0]
            filedata_b64 = params[1]
            filedata = base64.b64decode(filedata_b64)
            with open(filename, 'wb') as f:
                f.write(filedata)
            return dict(status='OK', data=f"{filename} uploaded successfully")
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def delete(self, params=[]):
        try:
            filename = params[0]
            if os.path.exists(filename):
                os.remove(filename)
                return dict(status='OK', data=f"{filename} deleted successfully")
            else:
                return dict(status='ERROR', data='file tidak ditemukan')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

if __name__ == '__main__':
    f = FileInterface()

    # Cetak hasil dengan json.dumps untuk readable format
    print(json.dumps(f.list(), indent=4))
    print(json.dumps(f.get(['pokijan.jpg']), indent=4))
