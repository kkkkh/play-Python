from tqdm import tqdm
import requests
import os
from concurrent.futures import ProcessPoolExecutor

def download(args):
    url, save_dir, group_id, id = args
    file_name = url.split("/")[-1]
    new_file_name = f'{group_id}_{id}.mp3'
    local_filename = os.path.join(save_dir, new_file_name)
    r = requests.get(url, stream=True)
    total = int(r.headers.get('content-length', 0))
    with open(local_filename, "wb") as f, tqdm(
        total=total, unit='B', unit_scale=True, desc=f'{file_name}:{new_file_name}'
    ) as bar:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            bar.update(len(chunk))



def join_download_path(id):
  # 'https://dn710704.ca.archive.org/0/items/englishpod_all/englishpod_0001pb.mp3',
  return f'https://dn710704.ca.archive.org/0/items/englishpod_all/englishpod_0{str(id).zfill(3)}pb.mp3'


def batch_download(*params,save_dir = "./app/sources",group_id=1):
  os.makedirs(save_dir, exist_ok=True)
  links = list(map(lambda id: (join_download_path(id), save_dir, group_id, id), range(*params)))
  with ProcessPoolExecutor(max_workers=2) as executor:
      for result in executor.map(download, links):
          print(result)


