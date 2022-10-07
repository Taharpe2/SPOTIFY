


### If you have desire to add data to a RedShift datatable use the below code snippet


from red_panda import RedPanda

##


redshift_conf = {
    "user": "username",
    "password": "password",
    "host": "hostname",
    "port": port number in integer,
    "dbname": "dbname",
}

aws_conf = {
    "aws_access_key_id": "<access_key>",
    "aws_secret_access_key": "<secret_key>",
    # "aws_session_token": "temporary-token-if-you-have-one",
}

rp = RedPanda(redshift_conf, aws_conf)
s3_bucket = "bucketname"
s3_path = "subfolder if any" # optional, if you don't have any sub folders
s3_file_name = "filename" # optional, randomly generated if not provided
rp.df_to_redshift(song_df, "table_name", bucket=s3_bucket, path=s3_path, append=False)






