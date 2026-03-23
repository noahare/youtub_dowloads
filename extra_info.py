import json
import logging

logging.basicConfig(filename="youtub_dowload.log",
                  filemode = "a",
                  format = "[%(asctime)s] %(name)s ==> %(levelname)s ; %(message)s",
                  level = logging.DEBUG,
                  datefmt = "%D -> %H : %M : %S")

mname = logging.getLogger("JSON") 


def show_data():
    try:
        mname.info("get import data in URL data")

        with open('info.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"--- {data.get('title')} ---")
        print("-" * 50)


        video_only = []      
        audio_only = []       

        for fmt in data.get('formats', []):
                f_id = fmt.get('format_id')
                f_note = str(fmt.get('format_note', ''))
                f_ext = fmt.get('ext', '')
                acodec = fmt.get('acodec', 'none') 
                vcodec = fmt.get('vcodec', 'none') 


                elif vcodec != 'none' and acodec == 'none':
                        if 'p' in f_note: 
                                video_only.append(f"{f_id:<5} | {f_note:<10} | {f_ext}")


                elif vcodec == 'none' and acodec != 'none':
                        audio_only.append(f"{f_id:<5} | {acodec:<10} | {f_ext}")


        print("\n[ 🔵 only video ]")
        print(f"{'ID':<5} | {'quality':<10} | {'deteal'}")
        for item in video_only: print(item)

        print("\n[ 🔴 only sound ]")
        print(f"{'ID':<5} | {'encody':<10} | {'deteal'}")
        for item in audio_only: print(item)

        mname.info("success")


    except FileNotFoundError as e:

        mname.error("Error file not exist!!")
        mname.debug(f"error {e}")

    except json.JSONDecodeError as e:

        mname.error("Error file not complet!!")
        mname.debug(f"error {e}")

    except KeyError as e:

        mname.error("Error data not complet!!")
        mname.debug(f"error {e}")

    except PermissionError as e:

        mname.error("Error permission denie")
        mname.debug(f"error {e}")

    except ConnectionError as e:

        mname.error("Error conection Error")
        mname.debug(f"error {e}")

    except KeyboardInterrupt as e:

        mname.error("Quit program")
        mname.debug(f"error {e}")





