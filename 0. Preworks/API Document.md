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
| URL            | http://vcm-30609.vm.duke.edu:8000/user/addUser               |
| Description    | Create a user account/Register                               |
| Excepted Send  | {<br />&emsp;"username":<br />&emsp;"password":<br />&emsp;"email":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />&emsp;&ensp;            }<br />} |

> 要在未来实现方法时修改user type

只返回uid嘛????
怎么handle fail login-->error case?

| API  Name      | Log in                                                       |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | http://vcm-30609.vm.duke.edu:8000/user/login                 |
| Description    | User log in                                                  |
| Excepted Send  | {<br />&emsp;"username":<br />&emsp;"password":      <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "uid":<br />&emsp;&ensp;            }<br />} |

| API  Name      | Log out                                                      |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | http://vcm-30609.vm.duke.edu:8000/user/logout                |
| Description    | User log in                                                  |
| Excepted Send  | {                                                    <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />&emsp;&ensp;            }<br />} |


???怎么标注optional信息

| API  Name      | Add driver                                                   |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/user/addDriver             |
| Description    | Driver Registraon                                            |
| Excepted Send  | {<br />&emsp;"maxmiumPassengers":<br />&emsp;"uid":<br />&emsp;"carType":<br />&emsp;"carLicense":<br />&emsp;"specialInfo":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />&emsp;&ensp;            }<br />} |

> 要在未来实现方法时修改user type


??????怎么知道driver的信息？？？？怎么区分user和driver的获得信息的区别？？
????怎么实现改password
| API  Name      | getUserInfo                                                  |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/user/getUserInfo           |
| Description    | access personal & vehicle info                               |
| Excepted Send  | {<br />&emsp;"uid":                                  <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                  "username":<br />                  "email": <br />&emsp;&ensp;            }<br />} |


??????怎么修改driver的信息？？？？怎么区分user和driver的修改信息的区别？？
| API  Name      | editUserInfo                                                 |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/user/editUserInfo          |
| Description    | edit personal & vehicle info                                 |
| Excepted Send  | {<br />&emsp;"uid":<br />&emsp;"username":<br />&emsp;"email":                                  <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />&emsp;&ensp;            }<br />} |


## Ride Management
?????？？？？？
Ride Status Viewing (Driver/Owner / Sharer) ?????????
| API  Name      | getRideByRID                                                 |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/getRID/rid            |
| Description    | get one ride info by ride id                                 |
| Excepted Send  | {<br />"uid":<br />}                                         |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                 "rid":<br />                 "rideType":<br />                 "rideOwner:"<br />                 "passNum":<br />                 "status":<br />                 "driver":<br />                 "time":<br />                  "Special Request":<br />                  "shared user":[]<br />&emsp;&ensp;            }<br />} |

？？？？？？？？
为什么不send uid?????????
Ride Status Viewing (Driver/Owner / Sharer) ?????????
| API  Name      | getRideByUID                                                 |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/getUID/uid            |
| Description    | get all of the rides under user have uid                     |
| Excepted Send  | {<br />}                                                     |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                   "list":[]                 <br />&emsp;&ensp;            }<br />} |


为什么有driver？
为什么没有vehicle type (optionally)？？？？？

| API  Name      | addRide                                                      |
| -------------- | ------------------------------------------------------------ |
| Method         | POST                                                         |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/add                   |
| Description    | add a request info (ride)                                    |
| Excepted Send  | {<br />    “rideType”:<br />    "riderOwner":<br />    "passNum":<br />     "status":<br />     "driver":<br />     "destination":<br />      "time":<br />      "specialRequest":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                   "rid":                 <br />&emsp;&ensp;            }<br />} |


？？？？？optional？？
| API  Name      | modifyRide                                                   |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/add                   |????????????
| Description    | user modify ride when the status is open                     |
| Excepted Send  | {<br />"uid":<br />"rid":<br />"...":<br />}                 |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                 <br />&emsp;&ensp;            }<br />} |


为什么要send uid？？？
filtered by the driver’s vehicle capacity and type / special info,???????


| API  Name      | SearchRideDriver                                             |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/driverSearch          |
| Description    | driver search for all open ride requests                     |
| Excepted Send  | {<br />"uid":<br />}                                         |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                    "list":                 <br />&emsp;&ensp;            }<br />} |

Ride Searching (Sharer)？？？？？
为什么要send uid？？？
为什么没有send number of passengers in their party？？
| API  Name      | SearchRideUser                                               |
| -------------- | ------------------------------------------------------------ |
| Method         | GET                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/shareSearch           |
| Description    | driver search for all open ride requests                     |
| Excepted Send  | {<br />"uid":<br />"destination":<br />"min_time":<br />"max_time":<br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{<br />                    "rid":                 <br />&emsp;&ensp;            }<br />} |


An email should be sent to the owner and any sharers of a ride once it is confirmed by a driver??????

| API  Name      | confirmRide                                                  |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/confirmRide           |
| Description    | driver confirm request                                       |
| Excepted Send  | {<br />"uid":<br />"rid":                            <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{                 <br />&emsp;&ensp;            }<br />} |


| API  Name      | closeRide                                                    |
| -------------- | ------------------------------------------------------------ |
| Method         | PUT                                                          |
| URL            | http://vcm-30609.vm.duke.edu:8000/ride/closeRide             |
| Description    | driver clode ride (complete)                                 |
| Excepted Send  | {<br />"uid":<br />"rid":                            <br />} |
| Expected Reply | {<br />&emsp; "code": 200<br />&emsp;"message": success<br />&emsp;"data":{                 <br />&emsp;&ensp;            }<br />} |

