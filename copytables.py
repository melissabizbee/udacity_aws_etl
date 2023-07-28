import boto3

(""" 
s3 = boto3.resource('s3',
                       region_name="us-east-1",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                     )

LOG_DATA =  s3.Bucket("udacity-dend")
for log_data in LOG_DATA.objects.filter(Prefix="log_data/A/B/C"):
    print(log_data)


SONG_DATA =  s3.Bucket("udacity-dend")

for song_data in SONG_DATA.objects.filter(Prefix="song_data/A/B/C"):
    print(song_data)


LOG_JSONPATH =  s3.Bucket("udacity-dend")
for log_jpath in LOG_JSONPATH.objects.filter(Prefix="s3://udacity-dend/log_json_path.json"):
    print(log_jpath)

# STAGING TABLES

LOG_DATA       = 's3://udacity-dend/log_data/A/B/C'
SONG_DATA      = 's3://udacity-dend/song_data/A/B/C'
LOG_JSONPATH   = 's3://udacity-dend/log_json_path.json'
""")