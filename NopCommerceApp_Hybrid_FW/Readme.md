# Hybrid FrameWork with selenium 4

In this directory it was implemented the FrameWork using POM, Pytest and HTML reports. With this list of videos i can implement what is exposed here: [Hybrid FrameWork From Scratch with python](https://www.youtube.com/playlist?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf)

## **Page to test**

[NopCommerceApp Administrator](https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin%2FCustomer%2FList)

## **A resume of each class**

This a compress resume. Each step realize explain in details in the list of videos and the readme.txt i created to explain each step and some errors i obtained to configure the framework and use without problems at this day.

1. I installed of packages required, createed a structure folder and Automatized some simple TC that test the login page and the tittle. Whit this i can run two TC and configure the screenshots in case of failure.
2. I implemented a TDD TC with an excel file copy and paste de login TC preview created. I configure the new conftest. file to throw the diferent TC created for each browser (edge, chrome and firefox). Finally i run the TC from CMD to create the report. Also, i can run parallel TC.
3. I add three TC that are more complex. Its takes much time to implement but finally i can running it.
4. I configure the pytest.ini file to can group and run different TC (regression and sanity for example). And i am starting to undestand how to work with Git, GitHub and jenkings to run the automatized TC. Up to here i only upload the framework to GitHub.
5. Finally, i saw how to run throw jenkins the automatized TC and make it possible with my proyect and configurations.

## **Final Thoughts**

Its a very informative course when i understand how implement and maintaince a proyect and design the TC and DDT TC with POM.

Undoubtedly, the importance of automating test cases to not only avoid repetitiveness but also to rapidly deploy an application is even clearer to me.
