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
| URL            | https://localhost:8080/user/add                              |
| Description    | Create a user account/Register                               |
| Excepted Send  | {<br />&emsp;"username":<br />&emsp;"password":<br />&emsp;"email":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />&emsp;&ensp;            }<br />} |

## Ride Management

