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
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />&emsp;&ensp;            }<br />} |

> 要在未来实现方法时修改user type

| API  Name      | Add driver                                                   |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | https://localhost:8080/user/adddriver                        |
| Description    | Driver Registraon                                            |
| Excepted Send  | {<br />&emsp;"maxmiumNumber":<br />&emsp;"uid":<br />&emsp;"carType":<br />&emsp;"carLicense":<br />&emsp;"specialInfo":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />&emsp;&ensp;            }<br />} |

> 要在未来实现方法时修改user type

## Ride Management

| API  Name      | getRideByRID                                                 |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | https://localhost:80/ride/getRID/rid                         |
| Description    | get one ride info by ride id                                 |
| Excepted Send  | {<br />"uid":<br />}                                         |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                 "rid":<br />                 "rideType":<br />                 "rideOwner:"<br />                 "passNum":<br />                 "status":<br />                 "driver":<br />                 "time":<br />                  "Special Request":<br />                  "shared user":[]<br />&emsp;&ensp;            }<br />} |

| API  Name      | getRideByUID                                                 |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | https://localhost:80/ride/getUID/uid                         |
| Description    | get all of the rides under user have uid                     |
| Excepted Send  | {<br />}                                                     |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                   "list":[]                 <br />&emsp;&ensp;            }<br />} |

| API  Name      | addRide                                                      |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | https://localhost:80/ride/add                                |
| Description    | add a request info                                           |
| Excepted Send  | {<br />    “rideType”:<br />    "riderOwner":<br />    "passNum":<br />     "status":<br />     "driver":<br />     "destination":<br />      "time":<br />      "specialRequest":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                   "rid":                 <br />&emsp;&ensp;            }<br />} |

| API  Name      | modifyRide                                                   |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | https://localhost:80/ride/add                                |
| Description    | user modify ride when the status is open                     |
| Excepted Send  | {<br />"uid":<br />"rid":<br />"...":<br />}                 |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                 <br />&emsp;&ensp;            }<br />} |

| API  Name      | SearchRideDriver                                             |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | https://localhost:80/ride/driverSearch                       |
| Description    | driver search for all open ride requests                     |
| Excepted Send  | {<br />"uid":<br />}                                         |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                    "list":                 <br />&emsp;&ensp;            }<br />} |

| API  Name      | SearchRideUser                                               |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | https://localhost:80/ride/shareSearch                        |
| Description    | driver search for all open ride requests                     |
| Excepted Send  | {<br />"uid":<br />"destination":<br />"min_time":<br />"max_time":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                    "rid":                 <br />&emsp;&ensp;            }<br />} |
