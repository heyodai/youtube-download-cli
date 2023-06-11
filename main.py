import youtube_dl
import argparse

parser = argparse.ArgumentParser(description='Download youtube videos')
parser.add_argument('url', metavar='URL', type=str, nargs='+',
                    help='URL of the video to download')
# TODO: Implement the arguments below
# parser.add_argument('-o', '--output', type=str, default='%(title)s.%(ext)s',
#                     help='Output filename template')
# parser.add_argument('-f', '--format', type=str, default='best',
#                     help='Video format to download')
# parser.add_argument('-p', '--playlist', action='store_true',
#                     help='Download playlist')
# parser.add_argument('-a', '--audio', action='store_true',   
#                     help='Download audio only')
# parser.add_argument('-v', '--verbose', action='store_true', 
#                     help='Print more info')
# parser.add_argument('-d', '--debug', action='store_true',
#                     help='Print debug info')
args = parser.parse_args()

ydl_opts = {}
# ydl_opts = {
#     'format': args.format,
#     'outtmpl': args.output,
#     'verbose': args.verbose,
#     'debug_printtraffic': args.debug,
#     'ignoreerrors': True,
#     'nooverwrites': True,
#     'noplaylist': not args.playlist,
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192'
#     }] if args.audio else []
# }

youtube_dl.YoutubeDL(ydl_opts).download(args.url)
# with youtube_dl.YoutubeDL() as ydl:
#     ydl.download(args.url)
