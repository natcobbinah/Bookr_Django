# Bookr 
A web app designed to let users browse and add book reviews (and books as well). 

## Features
```
> Models and Migrations
> URL Mapping, Views and Templates
> Customizing Django Admin
> Serving Static Files
> Forms
> Advanced Form Validation and Model Forms
> Media Serving and File Uploads
> Sessions and Authentication
> Advanced Templating and Class-Based Views
> Building a Rest API
> Generating CSV, PDF, XLSX, Graphs, and other Binary files
> Testing
> Integrating Third-Party Libraries
> Using a Frontend JavaScript Library with Django
```

## Sample Screenshots from working app
Homepage (Book lists page)
![homepage new](https://github.com/natcobbinah/Bookr_Django/assets/10479361/ba9bbe01-0289-491d-b43c-3d1c9cd2a709)

Reviews Page
![details page new](https://github.com/natcobbinah/Bookr_Django/assets/10479361/43bddc92-60e5-4d98-b447-e288b098ecd6)

Search 
![search bookr](https://github.com/natcobbinah/Bookr_Django/assets/10479361/c3bd7bf0-193a-4681-be9c-869be3245cbc)

Adding a Publisher
![creatingnewpublisher](https://github.com/natcobbinah/Bookr_Django/assets/10479361/4b0f8059-1dcb-433e-8680-58eb673a9c73)

![createdpublisher](https://github.com/natcobbinah/Bookr_Django/assets/10479361/9c6921e6-74a8-491d-b700-c77da3dfba93)

Editing a Publisher
![editingpublisher](https://github.com/natcobbinah/Bookr_Django/assets/10479361/703b94ba-257f-4a6b-b344-7862570ca95f)

![updatingpublisher](https://github.com/natcobbinah/Bookr_Django/assets/10479361/56e2e094-a79c-4cf9-8523-0a7b053e872f)

Adding a Review
![adding new review](https://github.com/natcobbinah/Bookr_Django/assets/10479361/44fac1c6-14f6-4a8b-ad88-5d5b39388c73)

![review added successfully](https://github.com/natcobbinah/Bookr_Django/assets/10479361/4b89d3c4-92b4-4946-9bea-84b4ac0eac37)

![review created on review page](https://github.com/natcobbinah/Bookr_Django/assets/10479361/cb9247c8-930f-4d2a-b137-6c6da4318d52)

Editing a Review
![editing review](https://github.com/natcobbinah/Bookr_Django/assets/10479361/528f65e4-489a-4b33-8a83-03304b0eda99)

![edited review with sucess](https://github.com/natcobbinah/Bookr_Django/assets/10479361/831868f6-e9c4-4455-ae10-cb4cb7d71825)

![review edited shown](https://github.com/natcobbinah/Bookr_Django/assets/10479361/a0da8202-aaae-4815-afb8-3f394f382ce3)

Serving and Saving Media Files
Edit book page, extended with upload files and image features
![uploading media](https://github.com/natcobbinah/Bookr_Django/assets/10479361/2e74dcc6-a310-449c-bdb9-52f6c8c26156)

![uploading media files selected](https://github.com/natcobbinah/Bookr_Django/assets/10479361/204fc307-6892-4bff-9ab3-8ba89d957dda)

![uploading media files successful](https://github.com/natcobbinah/Bookr_Django/assets/10479361/f690b4c5-d554-418b-b0f8-288b36c3b332)

Viewing/Retrieving media files to View, for Book Details Page
Book Cover if set on Book details page
![uploaded book cover retrieved and displayed with book sample as link](https://github.com/natcobbinah/Bookr_Django/assets/10479361/1d9f4eb5-80dd-4e6a-b011-fb13c493032d)

Sample pdf file, for book if set
![view uploaded media files with link](https://github.com/natcobbinah/Bookr_Django/assets/10479361/0a2c9b31-2a0a-4854-b994-250f00c263fd)

Authentication and Permissions
Login Page
![login page](https://github.com/natcobbinah/Bookr_Django/assets/10479361/6fa2dbb1-ac7c-4836-a8bc-61b6e32c38b9)

Login Page on Success
![login success page](https://github.com/natcobbinah/Bookr_Django/assets/10479361/232482f1-a51b-48b3-8172-a48bee605c6a)

Logged out Page
![logged out page](https://github.com/natcobbinah/Bookr_Django/assets/10479361/fe0cc8fe-c036-414b-9e00-9d0c3d90ddc2)

Authentication based content if user is staff or logged-in
![authentication based content if user is logged in](https://github.com/natcobbinah/Bookr_Django/assets/10479361/221efadc-f29b-4865-a369-1b3a494dcde4)

Authentication based content if user not logged-in or an anonymous user
![no addreview or media if user is anonymous](https://github.com/natcobbinah/Bookr_Django/assets/10479361/0b700a05-9248-4909-a8c5-3aae461fdc4f)

Auth and Permission based customization for logged-in users using sessions
![session books viewed by auth user and search history](https://github.com/natcobbinah/Bookr_Django/assets/10479361/1e1b8dbd-32cd-4b63-8f87-19827486cc27)

Custom template tags to render html on profile page 
Books read by user
![templatetags on profile page](https://github.com/natcobbinah/Bookr_Django/assets/10479361/05813c4d-c9a5-4906-9852-14bc05ad39d8)

API endpoints
![using token authentication](https://github.com/natcobbinah/Bookr_Django/assets/10479361/f772db53-c645-4917-88e7-b4348c5db93f)

![login success token](https://github.com/natcobbinah/Bookr_Django/assets/10479361/437d062c-c3c4-49ef-a214-58cdf54fc557)

![api end points](https://github.com/natcobbinah/Bookr_Django/assets/10479361/69dbf2ba-5d82-420d-97c6-589aaa52efc3)

![reviews api endpoint](https://github.com/natcobbinah/Bookr_Django/assets/10479361/8ebfe407-6cde-4755-8ffb-a2e4b22bd650)

![curl output](https://github.com/natcobbinah/Bookr_Django/assets/10479361/cfa1d51d-a1e8-460c-b386-d07ede6ad9b0)

Generating graphs, pdfs, and xlsx file
Graph of user reading list
![graph of user reading history](https://github.com/natcobbinah/Bookr_Django/assets/10479361/29b819dc-fad1-4e90-82c9-bbe3a31f6513)

Download user reading list in xlsx
![download reading history](https://github.com/natcobbinah/Bookr_Django/assets/10479361/9617de17-d0e8-44c1-9be8-f604c81adc28)

Verifying download reading list in xlsx format
![reading history in excel](https://github.com/natcobbinah/Bookr_Django/assets/10479361/8a77e2ca-51d7-43db-9926-f86025feee9a)

Incorporating JavaScript framework into Django
Recent Reviews generated with react
![recent reviews generated with react library](https://github.com/user-attachments/assets/96207998-03a7-49bb-b0a6-110cd1fcac98)




