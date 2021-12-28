## Deployment

#### Heroku

The website is hosted and deployed by [Heroku](https://www.heroku.com/home).
Everything is deployed from the master branch and updates automatically whenever the branch is updated in GitHub.

1.  Log in Heroku (or create a new one if you don't have one.);
2.  Go to your dashboard.
3.  Click on the "New"  -> "Create new app" button located right under the navbar.
4.  Choose a unique name for your app.
5.  Choose a region (preferably close to where you are located).
6.  If everything works fine you should see the overview page of your app.
7.  Click on Settings tab.
8.  Reveal Config vars.
9.  Here we configure the 
```
* SECRET_KEY
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY*
* DATABASE_URL
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* EMAIL_HOST_USER,
* EMAIL_HOST_PASS
* USE_AWS
```
 These are not public.
 
10. Click on deploy tab.
11. This app is connected to my repository in GitHub, so all pushes to github will update in Heroku aswell. 
12. Click on the Deploy Branch button.

#### Cloning

 1. If you want to clone the repository into a local file you can by:
 2. Clicking on the green button “Code” and copying the url showed.
 3. Open GitBash
 4. Change directory to the desired location where you want to clone the files to.
 5. Type git clone and paste the copied URL
 6. Press enter and you should have your local file cloned and ready.
 7. After opening the folder you should create a new file in the root directory, name it env.py
 8. In env.py you can set your environment variables.  
```
      import os

        os.environ["SECRET_KEY"] = "<your_value>"
        os.environ["STRIPE_PUBLIC_KEY"] = "<your_value>"
        os.environ["STRIPE_SECRET_KEY"] = "<your_value>"
        os.environ["DATABASE_URL"] = "<your_value>"
        os.environ["AWS_ACCESS_KEY_ID"] = "<your_value>"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "<your_value>"
        os.environ["EMAIL_HOST_USER"] = "<your_value>"
        os.environ["EMAIL_HOST_PASS"] = "<your_value>"
        # os.environ["DEVELOPMENT"] = "True" --> uncoment to use DEBUG MODE
        os.environ["USE_AWS"] = "True" --> set True or False to use AWS S3 Buckets
```

#### AWS, S3, IAM

1. Ensure you have an account or set one update
2. In the AWS Management Console search for S3, open it and click Create bucket
3. Name your bucket to match your Heroku app name and select the region closest to you. Uncheck Block all public access and acknowledge that the bucket will be public.
click Create bucket.

4. Click the newly made bucket and click the Properties tab and turn on Static website hosting, just fill in a default value for the index and error document and click save.
5. Now click on the Permissions tab, with the Cross-origin resource sharing (CORS) fill in:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
save the changes.

6. Go to the bucket policy and click on the policy generator, fill it out with your own arn.
7. Copy the policy that you get and paste it in the Bucket policy. Make sure you add the /* with the resource key to allow acces to all resources in this Bucket
8. Go to the Access control list (ACL) tab and set the list projects permission for everyone under the Public Access section.
9. In the AWS Management Console search for IAM, open it.
10. On the IAM dashboard click User group and then Create group, name your group so it makes sense to you what it is. click Create group.
11. On the menu left click Policies and then Create Policy.
12. Click on the Json tab and click Import managed policy, search for S3 select the AmazonS3FullAccess one. Click import.
13. You just want to give permission to your bucket, so make sure you fill it out like this, but with your own arn!
Click next untill you reach Review Policy

14. Give it an name and a description and click Create policy.
15. You'll arrive back on the policy page, go to User group` in the menu on the left and click on manage-your-group-name.
16. Click Attach policies search for and select the policy you just created.
17. Click on Users in the menu on the left. Then click Add users name it after your app, in my case postfly-jouw-online-drukkerij-staticfiles-user, give programmatic access and select next. Add the user to the group you just created. Click through on next and then on create user.
18. Download the csv file you see there and save it!
You need the secrect keys in there and once you've done this there is now way to retrieve it!!

#### Connecting AWS to Django

This section assumes you have succeeded at running this application in your local environment first, deployed it to Heroku and set up AWS as described above.

1. Remove the DISABLE_COLLECTSTATIC variable from your Config Vars on Heroku and add these values to it:

| Key | Value |
 --- | ---
AWS_ACCESS_KEY_ID | `your_AWS_ACCESS_KEY_ID`
AWS_SECRET_ACCESS_KEY | `your_AWS_SECRET_ACCESS_KEY`
USE_AWS | True

The values you'll find in the downloaded csv file.
Next time you deploy to Heroku, AWS will retrieve your static files and store them.

2. Go to S3, where you'll find a static folder with all your static files in it.
3. Click on Create folder and name it media click save and inside the media folder click Upload.
4. Click Add files and select the images that go with your products or in this case with the size.
5. Click next and under Manage public permissions, and choose Grant public-read access.
6. Then click Upload, you will see your files being uploaded.

