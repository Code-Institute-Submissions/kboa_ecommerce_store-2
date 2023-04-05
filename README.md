# Mother's Tongue Blog
KBOA Foods is an ecommerce foodstore in gbagada. The application was built for ease of shopping from anywhere on the website and the items delivered to the client's location.
The store is a full fledge ecommerce application that has been integrated with AWS and Stripe for payment details to conclude its transaction.

<p> Users with the weblink can shop from the website </p>
<p> Only registered users have access to crud functionalities on the application </p>
<p> Users are able to checkout their order. </p>
<p> Users are able to complete their order using stripe </p>
https://kboa-foods.herokuapp.com/

![Image Here](./docs/features/)

## Our Main goal:
<ul>
<li> to provide the ease of shopping from anywhere
<li> support with ready to cook foods
<li> to be accessible to our target audience in their various locations.
</ul>

### Content Strategy
<ul>
<li> user-friendly
<li> stand-out design with beautiful colors
<li> easy to use navigations
</ul>

### Target Audience:
Our application is targeted at online shoppers who would rather shop from the comfort of their home/environment. 

## User Story
<ul>
<li> Account Registeration

    As a Site User I can register an account so that I can interact with the blog

![Image Here](./docs/features/signup.png)

<li> Login

    As a Site User I can sign into an existing account so that I can interact with the blog

![Image Here](./docs/features/Login.png)

<li> Logout

    As a Site User I can signout of an account so that I can stop interacting with the blog

![Image Here](./docs/features/Logout.png)    

<li> Create a post

    As a Site User I can create post, so that I can upload blog posts. 
    

![Image Here](./docs/features/createapost.png)

<li> Retrieve a post

    As a Site User I can retrieve post, so that I can view a list of posts.

![Image Here](./docs/features/retrievepost.png)

<li> Update a post

    As a Site User I can update post, so that I can view the post list.

![Image Here](./docs/features/updatebutton.png)

<li> Delete a post
    
    As a Site User I can delete post, so that I can delete unwanted blog post.  

![Image Here](./docs/features/updatebutton.png)

<li> Like a post

    As a Site User I can like a post so that I can interact with the content 

![Image Here](./docs/features/likeapost.png)

<li> Unlike a post
    
    As a Site User I can unlike a post so that I can interact with the content 

![Image Here](./docs/features/unlikeapost.png)

<li> Leave a comment
    As a Site User I can leave comments on a post so that I can be involved in the conversation

![Image Here](./docs/features/leaveacomment.png)

<li> View category post

    As a Site User I can view category post, so that I can see similar posts to read. 

![Image Here](./docs/features/categorylink.png)

<li> Social media links
    <ul> 
    <li> This section has the social media icons, so users can find more information about the blog on facebook, instagram, twitter and youtube.
    <li> The icons when click on takes the user to the respective url.
    <li> It gives the users ability to users to folluw us on all our socia media links.
    </ul>

![Image Here](./docs/features/sociallinks.png)
</ul>

## Testing
<ul>
<li> The page works in different browser; Chrome, Safari, and my mobile device (iPhone11). </li>
<li> I confirm that this project is responsive, looks good and functions on all standard screen sizes using devtools device toolbar. </li>
<li> I have used the http://ami.responsivedesign.is/ website to check the render on different sceens. </li>
<li> I have tested that the navigation, home, login, logout, signup, create post button are all readable and easy to understand. </li>
<li> All the forms work perfectly well. </li>
</ul>

## Challenges
The major challenge that I experienced was timing.
<ul>
<li> Timing </li>
<li> I'm unable to create the update post function </li>
<li> Users are unable to upload images when they create post </li>
</ul>

## Validation
<ul>
<li>HTML </li>
<ul>
<li> No errors were returned when passing through the official W3C validator. </li>
</ul>
<li>CSS </li>
<ul>
<li> No errors were returned when passing through the official W3C validator. </li>
</ul>
<li>Accessibilty</li>
<ul>
<li> I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools. </li>
</ul>
</ul>

## Technology Used
<ul>

<li> HTML: we used this to build all the webpage for this website. </li>
<li> CSS: this was used to style our various pages. </li>
<li> Gitpod: is an online IDE for GitHub and GitLab that launches ready-to-code dev environments for any project with a single click. www.gitpod.io www.gitpod.io </li>
<li> Github: provides hosting for software development version control using Git. www.github.com </li>
<li> Chrome Dev Tool: this was used extensively to test debug my code. </li>
<li> Bootsrap 5.0</li>
<li> Django 3.8</li>
<li> Psycopg database</li>
<li> manage.py</li>
<li> Fontawesome </li>
<li> Cloudinary Storage </li>
<li> ElephantSQL </li>
<li> Stripe </li>
<li> Webhook </li>
<li> json </li>
<li> Django Countries </li>
<li> Amazon Web Services </li>
<li> ElephantSQL </li>
</ul>

## Deployment
The site was deployed to GitHub Page. The following steps were taken for deployment:
<ul>
<li> Steps for Deployment
</li>
    <ul>
    <li>Create a new app on Heroku
    </li>
    <li>Set my config vars to store my sensitive data
    </li>
    <li>Create the database on Elephant SQL
    </li>
    <li>Set debug to False in settings.py
    </li>
    <li>Click on deploy
    </li>
    </ul>
</ul>
