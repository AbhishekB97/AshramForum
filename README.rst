Introduction:
=============

The objective of the project is to build a discussion forum for Ashram Campus with the help of python based web framework django, which provides a platform for its users to browse topics by time and allows users to respond to a certain post or follow a thread for further content and get email notifications. 

User Functionalities
====================
•	Search Bar:  Filter topics by keywords contained in the title
•	Sign In: User must login to post topics but can browse anonymously
•	Google Sign In:  User can log in with their Google Account using OAuth2 authentication system.
•	Sign Up: Students are required to sign up to use all features of the forum 
•	View Topics:  User may view the topics that are currently posted on the forum sorted in reverse chronological order. 
•	Email Notifications:  User can follow a topic to get email notifications when a new comment is posted using an integrated mailing system.
•	Add Topic: User can post a topic for approval by  a moderator. If approved it gets published to the forum.
•	View Category:  User can view topics only for a particular category
•	Filter by Tags:  User can filter topics by tags used against them.
•	Comments: User can reply to a topic
•	Subcomments:  User can reply to a comment
•	Upvote: User can vote up a post they like.
•	Downvote: User can vote down a post they dislike.
•	Forgot Password:  User can reset password using the registered email account 
•	Change Password:  User can change password from profile settings 
•	Profile View:  User can view and edit their profile.
•	View Post History:  User can view the list of the topics that they have posted


Admin Functionalities
=====================
•	Delete Topic: Admin can remove a topic for violating rules and terms of use.
•	Add Badge: Admin can create badges to assign to users. Badges have no additional functionality than to indicate some role eg: Teacher, Student, etc.
•	Delete Badge: Admin can delete badges which automatically removes them from users who have been assigned that badge.
•	Add Categories & Subcategories:  Admin may add categories or subcategories that the users may post topics in. 
•	Delete Categories:  Admin may delete categories which automatically removes any topics in that category.  
•	Assign Badge to User:  Admin can assign a user a badge based on their role in the college or to show appreciation for some outstanding work. 
•	Approve Topic:  Admin must approve each topic posted by the user before it is published to the forum.
•	Delete User: Admin may delete a user which automatically removes any topics or comments posted by them.
•	Ban User: Admin may ban a user from the foum which prevents them from login. All the content posted by them (topics and replies) remain intact.
•	Delete Topic: Admin may remove a topic which automatically removes all comments.
•	Delete Comment: Admin may remove a comment which automatically removes its sub-comments. 
