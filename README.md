# Intro-to-Relational-Database-Project
This is the final course project for Intro to Relational Database

Requirements to run the project:
- Download the files from repo: tournament.py, tournament_test.py, tournament.sql.
- Download and install Vagrant from this link https://www.vagrantup.com/, if you haven't done it yet.
- Download and install VirtualBox from this link https://www.virtualbox.org/wiki/Downloads, if you haven't done it yet.
- Unzip the FSND-Virtual-Machine.zip to find 'vagrant' folder inside it.
- Create a folder in this 'vagrant' folder for this tournament project files and paste the files downloaded from repo in that folder.

These are the steps to setup and run virtual machine:
- Open terminal and change to directory this 'vagrant' directory and further into the folder created for tournament project.
- Run the command, 'vagrant up'. Running this command may take few minutes.
- Run the command, 'vagrant ssh'. This will start Linux VM.
- After running the VM, change the directory to 'vagrant'. This folder will have the same files as before starting the VM.

These are the steps to setup the database:
- Run command 'psql' while logged in the VM to open PostgreSQL terminal.
- Run command in psql terminal, '\i tournament.sql' to import the tables.

These are the steps to run unit tests of tournament project:
- Run command 'python tournament_test.py' to run the unit tests.
- It will the output according the success o unit tests.
