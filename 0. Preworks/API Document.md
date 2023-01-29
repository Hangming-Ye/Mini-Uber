# API Document

Template

| API  Name      |                                                              |
| -------------- | ------------------------------------------------------------ |
| Method         |                                                              |
| URL            |                                                              |
| Description    |                                                              |
| Excepted Send  | {<br />}                                                     |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                 <br />&emsp;&ensp;            }<br />} |

## User Management

| API  Name      | Add user                                                     |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | https://localhost:8080/user/adduser                          |
| Description    | Create a user account/Register                               |
| Excepted Send  | {<br />&emsp;"username":<br />&emsp;"password":<br />&emsp;"email":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />                  "userType":<br />                  "salt":<br />&emsp;&ensp;            }<br />} |

| API  Name      | Add driver                                                   |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | https://localhost:8080/user/adddriver                        |
| Description    | Driver Registraon                                            |
| Excepted Send  | {<br />&emsp;"maxmiumNumber":<br />&emsp;"carType":<br />&emsp;"carLicense":<br />&emsp;"specialInfo":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />                  "userType":<br />&emsp;&ensp;            }<br />} |

## Ride Management

