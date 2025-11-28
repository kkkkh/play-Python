from lrc.index import generate_lrc,batch_generate_lrc
from download.index import batch_download

# generate_lrc("./app/sources/englishpod_0001pb.mp3", "./app/sources/englishpod_0001pb.lrc")
if __name__ == "__main__":
  # batch_download(10,11,save_dir = "./app/resource", group_id=1)
  batch_generate_lrc(10,11,save_dir = "./app/resource",group_id=1)

