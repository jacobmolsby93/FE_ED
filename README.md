# FE_ED

A Discussion page, where users can sign up. Create a user profile, upload a profile image and write a short biography. Inspired by the website Reddit,
developed with a simpler approach with the possibility of scaling. As well as uploading and reading other posts, users can engage with other users in the form of comments and likes throughout the different posts. Features that will be implemented shortly is the ability to see others users' pages.
As well as a more categorized sorting system of the posts created.

[![landing-page.png](https://i.postimg.cc/ZKNjV5zQ/landing-page.png)](https://postimg.cc/svVp2yXP)

## Features 

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

## Testing 

- I have chosen to go with the already imported django testcase that runs along with unitest, A testing package that lets me simulate the different functions and request that is required to make the site run smoothly.
    
    1. URL testing
        - I have written a test for each url of the page to see that the urls are resolved and working as should.
    
    2. View testing
        <br>
        For each of the views of the application, I have written tests to conclude that they are working as they should. By simulating the requests that make the application run, such as POST, GET, DELETE.
        - By simulating the creation of a user to act as the authenticated user on the page, where then the user is tried in each of the different views.
        After the user is created I created a post for the user to see in the test GET request of the home page and post detail.
        In the test Add post view I create a post and simulate the POST method with a successfull status code of 200.
        The test DELETE request, gets the post that I have created in the beginning and performing the delete method on it. I know this by counting the number of posts before the action is called, then making the assertEquals to 1, to verify that 1 / 2 posts have been deleted. 
        The same has been done for deleting comments on a post, liking a post and editing a post. With the same structure as above. All to simulate a response code of 200.
    3. Model testing
        <br>
        The testing of models has been done just to see that the post_save works on both slugify post title, as well as user is bloguser on signup.
        - For the slugify title, the test is simply done be checking if the title of the post is equal to the slug of the post in small letters with each word seperated with a dash.
        - For the user, I have created a post save method that saves the user as a bloguser on signup. How I check that this works is by double checking the value User: "username" is equals to Bloguser: "username" when running the test. By knowing that they are the same I know the post save method has been complete.

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffeed-news.herokuapp.com%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 
