# ECE568 Prework Set Up Guide

## 1.  Reserve a Virtual Machine

1. Visit https://vcm.duke.edu/home/ and login

2. Reserve a VM

   ![image-20230112202435855](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122024926.png)
   
   


3. Select OS

   ![image-20230112202719449](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122027512.png)

   

4. Write down the `hostname`, `user`,`URL(for restart)`. The remote host address is `user`@ `hostname`

   ![image-20230112230755510](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122307607.png)

## 2. Connect the Server

0. If you have registered your public ssh key, go ahead. Otherwise, follow the following guide to register your public SSH key (https://www.cs.duke.edu/csl/security/ssh)

1. For windows user, the guide use mobaXterm as example. For Linux and Mac OS user, check the above link. For alternative SSH software like Putty, Xshell, please use google to find the guide.
2. Open Sessions - new session - SSH, follow the instruction in the image.

![image-20230112231317642](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122313676.png)



3. If success, you will get a interface like this

   ![image-20230112211007903](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122110930.png)

   

## 3. Server Set up

0. Get the root permission. (password is password of your netId)

   ```bash
   sudo -i
   ```

1. Add your teammate

   ```bash
   sudo adduser your_teammate_netid
   sudo adduser netid sudo
   ```

2. Software Installation

   ```bash
   sudo apt-get install gcc g++ make valgrind git postgresql libpq-dev python python3-pip 
   sudo pip3 install django psycopg2
   sudo apt-get install libssl-dev libxerces-c-dev libpqxx-dev manpages-posix-dev
   ```

3. Check whether installation is successful (should be 4.1.5)

   ```bash
   django-admin --version
   ```

4. Other Check 

   ```bash
   gcc -v
   g++ -v
   make -v
   valgrind --version
   git --version
   pg_config --version
   python3 --version
   pip --version
   ...
   ```

   should be like this

   ![image-20230112215657113](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122156171.png)

   

5. Install whatever editor you like (vim, emacs, screen, vscode... )

   too long, don't write

## 4. Remote Git Setup

0. Change account to user account and make directory

   ```bash
   su your_net_id
   cd /
   mkdir ECE568
   cd ECE568
   mkdir HW1
   cd HW1
   ```

1. config user info

   ```bash
   git init
   git config --global user.name "Your Name"
   git config --global user.email "Your_email@example.com"
   ```

2. Connect to Github

   2.1 Generate Key

   ```bash
   ssh-keygen -t rsa -C "Your_email@example.com"
   cat ~/.ssh/id_rsa.pub
   ```

   2.2 Copy the key, open github, click the avatar - setting - SSH and GPG keys - new SSH key, paste the key in `Key` and make a title for it.

   ![image-20230112225224102](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/image-20230112225224102.png)

   2.3 Go back to shell, if answer is `...You've successfully authenticated, but GitHub does not provide shell access`, it is connected.

   ```bash
   ssh -T git@github.com
   ```

   

3. Make a new repository in github

   ![image-20230112225900739](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122259776.png)

4. Go back to shell and test

```bash
git remote add origin git@github.com:YOUR_NAME/Repositories_Name.git
echo "# ECE568-HW1" >> README.md
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
```



5. The repository should be like this:

   ![image-20230112230329475](https://raw.githubusercontent.com/Hangming-Ye/All-Pic/main/pic/202301122303522.png)

6. Cheers!!!!  :beers: :beers: :beers: :beers: :beers: :beers: 
