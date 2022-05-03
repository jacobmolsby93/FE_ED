# FE_ED

A Discussion page, where users can sign up. Create a user profile, upload a profile image and write a short biography. Inspired by the website Reddit,
developed with a simpler approach with the possibility of scaling. As well as uploading and reading other posts, users can engage with other users in the form of comments and likes throughout the different posts. Features that will be implemented shortly is the ability to see others users' pages.
As well as a more categorized sorting system of the posts created.

[![landing-page.png](https://i.postimg.cc/ZKNjV5zQ/landing-page.png)](https://postimg.cc/svVp2yXP)

# Features 

A breif overview of all the sections I have implemented in the page.

### Existing Features

- __Navigation Bar__

  - The navbar is featured on all pages, with a sleek design that blends in with the overall layout of the page. An easy search function in the middle, as well as a navigation off-canvas nav menu that slides of from the right.
  - The user will have the ability to log in to the page or signup if they have not already done so, If the user is logged in they can access their profile or add posts.
[![navbar.png](https://i.postimg.cc/26jhdHjT/navbar.png)](https://postimg.cc/Lq7J231Z)

- __The landing page__

  - The landing page offers a simple welcome message along with a very short description of what the page offers. Its dynamic to the user. 
  - Lets the user know if they are logged in or not. Link to the latest posts.

- __Home page - Latest posts__

  - Just below the landing page, the user will see all the latest posts posted in a grid layout. 
  - The user can navigate through the different posts and select the one that they find most interesting.
[![home-page-latest.png](https://i.postimg.cc/RZzd8xMZ/home-page-latest.png)](https://postimg.cc/8jtLJ3J2)


- __Post Detail__

  - After selecting a post, the user will be navigated to the post overview page, where the full post is displayed along the the featured image and author details.
  - The user will be able to read about the post, as well as like or comment.
[![post-detail.png](https://i.postimg.cc/zDbkGGvf/post-detail.png)](https://postimg.cc/jCTf8KzV)
[![comment-area-post-detail.png](https://i.postimg.cc/cLmRbK9F/comment-area-post-detail.png)](https://postimg.cc/qNN6t7dK)

- __The Footer__ 

  - The footer I have design is just a simple one with the logo of the page and who the developer is.
  - The footers thought is to be a simple design element.

    [![footer.png](https://i.postimg.cc/9fLBr4yD/footer.png)](https://postimg.cc/R3ntYZsm)

- __User Profile__

  - The user profile section is where the logged in user can get an overview of their profile, and what posts they have posted.
  - This is valuable to the user becuase they can see how many posts they have created, and update their profile image along with some personal information.

    [![profile-page.png](https://i.postimg.cc/Y26zWyNc/profile-page.png)](https://postimg.cc/vDmnRhSX)

- __The Sign Up Page__

  - This section of the page will allow the user to signup and get full access to the everything on it.

    [![signup.png](https://i.postimg.cc/VLyGnC0T/signup.png)](https://postimg.cc/NL4kwL47)


### Features Left to Implement

1. To let users see other users profile pages plus send messages to eachother privately.
2. Implement most liked posts on the home page, to let the users see the latest posts as well as the most liked.

# Testing 


### Automated Testing
- I have chosen to go with the already imported django testcase that runs along with unitest, A testing package that lets me simulate the different functions and request that is required to make the site run smoothly.
    
    1. URL testing
        - I have written a test for each url of the page to see that the urls are resolved and working as should.


        Results: 
          - [![test-urls.png](https://i.postimg.cc/4y55j8k2/test-urls.png)](https://postimg.cc/n9XBDGLq)
    

    2. View testing
        <br>
        For each of the views of the application, I have written tests to conclude that they are working as they should. By simulating the requests that make the application run, such as POST, GET, DELETE.
        - By simulating the creation of a user to act as the authenticated user on the page, where then the user is tried in each of the different views.
        After the user is created I created a post for the user to see in the test GET request of the home page and post detail.
        In the test Add post view I create a post and simulate the POST method with a successfull status code of 200.
        The test DELETE request, gets the post that I have created in the beginning and performing the delete method on it. I know this by counting the number of posts before the action is called, then making the assertEquals to 1, to verify that 1 / 2 posts have been deleted. 
        The same has been done for deleting comments on a post, liking a post and editing a post. With the same structure as above. All to simulate a response code of 200.


        Results:
          - [![test-views.png](https://i.postimg.cc/15mMDZwk/test-views.png)](https://postimg.cc/V5hjcp7g)


    3. Model testing
        <br>
        The testing of models has been done just to see that the post_save works on both slugify post title, as well as user is bloguser on signup.
        - For the slugify title, the test is simply done be checking if the title of the post is equal to the slug of the post in small letters with each word seperated with a dash.
        - For the user, I have created a post save method that saves the user as a bloguser on signup. How I check that this works is by double checking the value User: "username" is equals to Bloguser: "username" when running the test. By knowing that they are the same I know the post save method has been complete.


        Results:
          - [![test-models.png](https://i.postimg.cc/W4F5t6gt/test-models.png)](https://postimg.cc/QBDQy76r)


### Manual Testing
- A link to an external document where I have documented the manual testing procedures.
- I go through each of the functions of the website in a detailed manner. To ensure that the current features functions as they should.
  [Manual-Testing Document](https://docs.google.com/document/d/e/2PACX-1vRACOclSMO6wS1u_GWsOU_ejg2jlzsDqgMnbogqi1DGDNJVcQT8r7hr37aPhL6MQTC6BBKKl2-hOkbf/pub)


### Validator Testing 

#### HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffeed-news.herokuapp.com%2F)
#### CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/validator?lang=sv&profile=css3svg&uri=https%3A%2F%2Ffeed-news.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)
#### PEP8
  - All the python code has been copied and pasted into a pep8 checker online.
  - There are no pep8 issues in the problems tab of the bash-terminal that needs to be addressed.
  - 4 lines of code in settings.py that are to long, but will brake the code if split up.

  #### PEP8 validator Results 
  - [settings.py](https://postimg.cc/pytpSVGY)
  - [home_views](https://postimg.cc/R3VTKQfh)
  - [post_models](https://postimg.cc/zbHKFdfz)
  - [utils](https://postimg.cc/BXBDpPJK)
  - [post_views](https://postimg.cc/9Df4Bxx6)
  - [post_form](https://postimg.cc/xqS3P2LB)
  - [user_models](https://postimg.cc/JH1JCRqn)
  - [user_views](https://postimg.cc/yWVSdYm6)


# Deployment

The web-application has been deployed using Heroku & AWS buckets, in this section I will explain the steps I took to deploy the website.

- Heroku: 
  - Go the [Heroku](https://heroku.com/) page and create an account if you dont already have one. 
  - When logged in proceed to create new app, and select the region closest to you.
  - Name the application with a unique name.
  - After the app as been created, Go to resources tab and search for Heroku postgres, add the free version.
  - Make sure you have pushed the completed version of your code to github, then select deploy with github on the deploy tab of heroku.
  - Search for the repository, select the correct one.
  - Make sure all the requirements are installed from this requirements.txt file.
  - In your root directory of your codebase, create a new Procfile and add. web: gunicorn projectname.wsgi
  - In the environment variables add a new variable called DISABLE_COLLECTSTATIC : 1
  - In heroku, go to the deploy tab and press deploy branch.
  - The application should now be deployed without staticfiles.
- AWS buckets:
  - Go to [AWS](https://aws.amazon.com/) page and create an account. A credit card is needed.
  - In the search bar, search for S3.
  - In S3, create a new bucket. Prefferably named after the project.
  - Click on the bucket properties tab and enable static website hosting.
    - Enter the default values of index.html and error.html.
  - On the permissions tab, scroll down to Block public access (bucket settings) and press edit. Turn off this setting and approve.
  - Further down on the page at CORS, paste these settings.
    - [
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
  - Now head up the page to bucket policy, and press policy generator.
    - Policy type will be S3bucketpolicy
    - Principal: *
    - Actions: getObject
    - Copy bucket ARN into the ARN field.
    - Press Add statement and copy the policy from the policy generator into the bucket policy, and add /* to the ARN.
    - Lastly on the access control list, grant everyone the list objects property.

  - In the top search bar search for IAM.
  - When in the page. Go to User Groups, and create a new one for the bucket to live in.
  - The tab section to the left, select policies. Then create policy.
  - In the JSON tab, select import managed policy. Select AmazonS3FullAccess.
  - Copy the ARN From the bucket created earlier and paste it into resources as ["ARN", "ARN/*"]
  - Click review policy, Name it and give a brief description.
  - Then press create policy.
  - Go back to groups. Select the group created for this purpose, and attach policy. attach the policy just created.
  - In the tab menu to the left select user, and create a user for the group created.
  - Select a suitable username, Add the user to the group created.
  - Download the csv file and save the file !IMPORTANT!.

- Django
  - Install boto3 and django-storages
  - Add storages to installed apps in settings.py.

  - Paste in the following in the bottom of settings.py
    <br>
    if 'USE_AWS' in os.environ:
    
    AWS_STORAGE_BUCKET_NAME = 'milestone4-feed-bucket'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
- Heroku
  - In app page, go to settings and add the AWS keys to the environment variables.
  - Along with USE_AWS for the above to work.

The live link can be found here - https://feed-news.herokuapp.com/ 


# UX/UI Design and WireFrames
- The wireframes have been created using the tool Figma.
  The design I've created is a simple but eye-catching design, with design principles that follow the 60-30-10 rule, where shades of grey, orange, and white have been utilized to capture the audience.
  The primary color, is used for the call-to-action buttons and links. A call for the user that here where the bright orange color is, a link / button to take you to another sections of the website. 
  The secondary color is white, acting as a breaker between the orange and the grey. making the transition between the two colors smooth. The reason behind white is its naturall flow and nice contrast to both the primary and dominant colors.
  The Dominant color I've used is a shade of grey #333333. A nice slightly darker shade that brings out a nice feel to the overall website.

  [Figma Link](https://www.figma.com/file/S8ZmFnf8i1n34VppadPwIE/FE_ED?node-id=0%3A1)

  - Landing page Wireframe
  - [![Landing-Page.png](https://i.postimg.cc/1z01fQp8/Landing-Page.png)](https://postimg.cc/GBp556gR)

  - Offcanvas Nav Wireframe
  - [![Offcanvas-nav-menu.png](https://i.postimg.cc/52vZRVKs/Offcanvas-nav-menu.png)](https://postimg.cc/HrYZrfgM)

  - Post Detail Wireframe
  - [![Post-Detail.png](https://i.postimg.cc/h4Ls6GKz/Post-Detail.png)](https://postimg.cc/ThPnWfLf)

  - Form Wireframe
  - [![Form.png](https://i.postimg.cc/bNLTYFDq/Form.png)](https://postimg.cc/BXLDMpBz)
  
  - User Profile Wireframe
  - [![User-Profile-1.png](https://i.postimg.cc/k5VGRDTT/User-Profile-1.png)](https://postimg.cc/KK2xdcST)

# Database Schema & Agile software Tools

- A link to the workflow management software used in the process of creating this application. [Trello](https://trello.com/invite/b/gMC933ys/1ce3d7e3142f437329bddfd7480b6fc2/milestone4)
User stories have been created for each of the tasks that has

- A flowchart created in lucid charts. Which displays how the models relates to eachother.
  - [![Flowchart.png](https://i.postimg.cc/ZKP87sFr/Flowchart.png)](https://postimg.cc/9rMwzpkM)


## Credits 
- AWS deployment code taken from:
    - https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/40cc2543c48643fda09351da6fa90579/
- Testing code partially taken / learned from:
    - https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3

### Content 

- Tel aviv media and content taken from:
    - https://www.pexels.com/sv-se/sok/tel%20aviv%20city/
https://askalocalapp.com/Tel_Aviv/EN/10-interesting-facts-city-tel-aviv/

- Sydney media and content taken from:
    - https://www.pexels.com/sv-se/foto/hav-stad-horisont-byggnader-9129012/
https://www.guestreservations.com/about/news/10-interesting-facts-that-you-probably-didnt-know-about-sydney-australia

- Portugal media and content taken from:
    - https://www.trafalgar.com/real-word/fun-facts-about-portugal/
https://www.pexels.com/sv-se/foto/stad-vag-manniskor-gata-3763903/

- Bangkok media and content taken from:
    - https://facts.net/city-facts/
https://www.pexels.com/sv-se/foto/fordon-motorcykel-auto-rickshaw-thailand-1682748/


