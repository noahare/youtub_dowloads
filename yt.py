import yt_dlp
import json
import logging
from extra_info import show_data
import os

logging.basicConfig(filename="youtub_dowload.log",
                                        filemode = "a",
                                        format = "[%(asctime)s] %(name)s ==> %(levelname)s ; %(message)s",
                                        level = logging.DEBUG,
                                        datefmt = "%D -> %H : %M : %S")



def get_data(url,mname):
    try:
        mname.info("get info about URL")

        ydl = yt_dlp.YoutubeDL()
        info = ydl.extract_info(url = url, download=False)

        with open("info.json","w") as f:
            json.dump(info,f, indent =4)
        
        mname.info("success")

    except yt_dlp.utils.DownloadError as e:

        mname.error("Error the url is not valed")
        mname.debug(f"Error {e}")

    except yt_dlp.utils.DownloadError as e:
        mname.error("Error can't access th video")
        mname.debug(f"error {e}")

    except ConnectionError as e:
        mname.error("Error conection has cut")
        mname.debug(f"error {e}")

    except KeyboardInterrupt as e:
        mname.error("program close")
        mname.debug(f"error {e}")


def dowloads(video_id,audio_id,save_path=os.getcwd()):
    try:
        cmd = f"yt-dlp -f '{video_id}+{audio_id}' -o '{save_path}%(title)s.%(ext)s' --merge-output-format mp4 '{video_url}'"
        os.system(cmd)
    except FileNotFoundError as e:

        mname.error("Error path not found")
        mname.debug(f"Error {e}")

    except PermissionError as e:

        mname.error("Error permission denig")
        mname.debug(f"Error {e}")

    except OSError as e:

        mname.error("Error the video title has a leter not support in your OS file name")
        mname.debug(f"Error {e}")

    except KeyboardInterrupt as e:

        mname.error("program stop")
        mname.debug(f"Error {e}")

    except Exception as e:

        mname.error("Error")
        mname.debug(f"Error {e}")

video_url = input ("enter video url\t").strip()
name = input ("enter a nmae for debug log (the default is 'user')\t").strip()
mname = logging.getLogger(name if name else "user")


get_data(video_url,mname)
show_data()

aux_id = input ("enter sound id;\t")
video_id = input ("enter video id;\t")
dowloads_path = input ("enter dowloads path[the default is curent directory];\t")

dowloads(video_id,aux_id,dowloads_path)

