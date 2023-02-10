# Ride Sharing Service

## Description
Ride Sharing Service is a Django app, This web-app will let users request, drive for, and join rides.

## Deployment

1. Install
   ```bash
   sudo apt-get install gcc g++ make valgrind git postgresql libpq-dev python python3-pip 
   sudo pip3 install django psycopg2
   sudo apt-get install libssl-dev libxerces-c-dev libpqxx-dev manpages-posix-dev
   ```
2. Set up Email and CSRF Token in /HW1/docker-deploy/web-app/hw1/setting.py
   ```python
   ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','localhost']
   CSRF_TRUSTED_ORIGINS= ['http://0.0.0.0:8000','http://127.0.0.1:8000','http://localhost:8000']
   EMAIL_USE_TLS =         # True/False
   EMAIL_USE_SSL =         # True/False
   EMAIL_HOST =            # SMTP Host Address
   EMAIL_PORT =            # Port of SMTP
   EMAIL_HOST_USER =       # Mail Address
   EMAIL_HOST_PASSWORD =   # Password/Token
   ```
3. Run in the /HW1 using
   ```bash
   sudo docker-compose up
   ```
## Function

User: 
1. Create Account
2. Login & Logout
   - Handle login failure with an an invalid user account
3. Register as a driver and enter their personal and vehicle info —> user become driver
   - The vehicle information includes the type, license plate number, maximum number of passengers, and optionally any other special vehicle info
   - Only have 1 vehicle
4. access and edit their info.
   - personal & vehicle info 
   - driver status
5. request a ride —> user become owner 
   - specifying a destination address, a required arrival (date & time), the number of total passengers from the owner’s party, and optionally, a vehicle type and any other special requests.
   - specify the destination address, a required arrival date / time, the number of total passengers from their party, a vehicle type (optionally), whether the ride may be shared by other users or not, and any other special requests.
6. search for open ride requests (Ride Searching (Sharer))
   - specifying a destination, arrival window (the user’s earliest and latest acceptable arrival date & time) and number of passengers in their party.
7. joining ride after the searching (in 6.) —> user become sharer
   - multiple sharers who sign up to join one ride

owner: 
1. edit/modify ride request up until it is confirmed (as long as the ride is open)
   - Ride Request Editing (Owner): A ride owner should be able to edit the specific requested atributes of the ride as long as the ride is not confirmed.
2. view ride status until the ride is complete (non-complete rides)
   - Ride Status Viewing (Owner / Sharer): For open ride requests, this should show the current ride details (from the original request + any updates due to sharers joining the ride). For confirmed ride requests, the driver and vehicle details should also be shown.

driver: 
1. accepts the ride after searching (in 3.) (request is confirmed) (A driver can claim and start a ride service, thus confirming it.)
   - An email should be sent to the owner and any sharers of a ride once it is confirmed by a driver
2. close a ride (finishes the ride and marks it as complete)
   - edit a ride to mark it as complete.
   - Once closed, the ride owner and each sharer should be notified by email that the ride has been confirmed (hence no further changes are allowed).
3. search for open ride requests based on the ride request atributes
   - Only requests which fit within the driver’s vehicle capacity and match the vehicle type and special request info (if either of those were specified in the ride request) should be shown.
   - filtered by the driver's vehicle capacity and type / special info, if applicable
4. Ride Status Viewing (Driver) 
   - select a confirmed ride and view all of the ride details
   - view the status of their confirmed rides
   - show the information for the owner and each sharer of the ride, including the number of passengers in each party.
5. A driver should be able to see a list of their confirmed rides

sharer: 
1. view the ride status, similarly to a ride owner
   - Ride Status Viewing (Owner / Sharer): For open ride requests, this should show the current ride details (from the original request + any updates due to sharers joining the ride). For confirmed ride requests, the driver and vehicle details should also be shown.
2. edit their ride status as long as the ride is open.
   - The "edit status" would included the ability to change info like the number of sharer until the ride is confirmed.
