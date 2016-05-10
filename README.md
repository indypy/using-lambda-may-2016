# IndyPy May 2016 -- Using Python with AWS Lambda

The `slides.rst` can be generated using [Hovercraft](http://hovercraft.readthedocs.io). But the exciting stuff is in the `hello_world` and `create_thumbs` directories.

## Demo Code

### Hello World (in Lambda)

In the `hello_world` directory is a snippet of code you can just copy-and-paste into the TTW Lambda editor and then setup an API endpoint to see it work via a simple `GET` request.

Here is how to try it out:

    $ virtualenv env
    $ env/bin/pip install -r requirements.txt
    $ env/bin/http https://your-url-to-your-api-endpoint
    Profit!

You will see your endpoint URL in the AWS Console.

### Create Thumbnails

In the `create_thumbs` directory is sample code that showcases how to included 3rd party dependencies (even those with compiled resources) into a Lambda project. Simply zip up the contents of the folder and upload it into a S3 bucket. Then create a new Lambda function and select to upload from S3 to select the zip file.

    $ cd create_thumbs
    $ zip -r create_thumbs.zip
    $ aws s3 cp create_thumbs.zip s3://your-bucket/

Now setup your event source to be the S3 object created event and watch the magic happen.

The demo will put files into a subdirectory called `thumbs/` and I'd recommend creating and listening only for files in a subdirectory of the bucket so you don't end up in a continuous loop of creating thumbs and putting them and creating more thumbs.

