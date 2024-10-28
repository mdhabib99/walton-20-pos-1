## Walton POS ERP

WaltonPOS ERP is a suite of web based business apps.


## Installation Guide
To install Walton ERP16 on an Ubuntu 22.04 LTS Server Open terminal and in the terminal, use the ssh command followed by the remote server's IP address or hostname and your username. Replace <server_ip> with the actual IP address or hostname, and <username> with your username on the server.

```bash
ssh <username>@<server_ip> -p <port_number>
```

After logging in to the server by providing the password, verify that the server version is Ubuntu 22.04 itself. To verify the version, use the command.
```bash
lsb_release -a 
```
Next, run the following command to ensure that all installed packages on the server are updated to their most current available versions:
```bash
sudo apt update && sudo apt upgrade
```
### Secure your server:
Make sure the system is protected against ssh assaults; using Fail2ban will aid in ssh attack prevention.
```bash
sudo apt-get install openssh-server fail2ban
```
### Create a System User:
We're installing Walton POS 16 on a specific system user account. For this, we need to make a new system account. Use the given command to create a user called "waltonpos"
```bash
sudo useradd -m -d /opt/waltonpos -U -r -s /bin/bash waltonpos
```
### Install the dependencies for Walton POS 16:
We have to add some extra Python packages like Python version, wheel, venv, etc., to our Ubuntu 22.04 system before we can install Walton POS 16. To do this, Run the following command:
```bash
sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
```
### Install  and Configure the PostgreSQL database server:
Walton POS exclusively uses PostgreSQL for its data storage. Now run this command to install the PostgreSQL server on our Ubuntu 22.04 system.
```bash
sudo apt-get install postgresql
```

After installation, Do the following to create the user `waltonpos`. Additionally, you must change the password for the user `waltonpos` at that time. You must enter the new password in the POS configuration file at the very end of the installation process.
```bash
sudo -u postgres createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt waltonpos
```
The user must then be designated as a superuser in order to receive further privileges.
```bash
sudo su postgres
psql
ALTER USER waltonpos WITH SUPERUSER;
```
Exit from psql and Postgres user:
```bash
\q
exit
```
### Install Wkhtmltopdf:
Walton-POS requires the Wkhtmltopdf package for printing-related purposes, which is a free, open-source command-line utility that utilizes the Qt webkit engine to transform HTML content into PDF. Install Wkhtmltopdf by executing this command.
```bash
sudo apt install wkhtmltopdf
```
Since Walton-POS requires a wkhtmltopdf 0.12.1 or higher version verify it by using
```bash
wkhtmltopdf --version
```
### Install Walton-POS:
With the help of Win-SCP of any SFTP client transfer the source code of Walton-POS to the designated server in `/opt/waltonpos/` directory.

Next, change the files ownership for new created user `waltonpos`

```bash
chown -R waltonpos:waltonpos .
```

Next, it's important to switch to the system user we established for Walton-POS. This step is crucial to avoid encountering issues related to access rights. So we can switch to the user that we have created before.
```bash
sudo su - waltonpos -s /bin/bash
```

In this guide, we will set up Walton-POS 16 within a Python virtual environment. First go to the `/opt/waltonpos/waltonpos16` dir, run the subsequent command to generate a new Python virtual environment.

```
python3 -m venv .venv
```
After the virtual environment is installed, we need to activate it by running

```bash
source .venv/bin/activate
```

Now, let's proceed to install Walton-POS 16.
```bash
(venv) waltonpos16@ubuntu:~$ pip3 install wheel
(venv) waltonpos16@ubuntu:~$ pip3 install -r ./requirements.txt
```
### Create an Odoo Service:
We have to create a systemd unit for WaltonPOS16 So that it can behave like a service.

```bash
sudo nano /etc/systemd/system/waltonpos16.service
```
Copy and paste the following content into the systemd unit file odoo16.service:

```bash
[Unit]
   Description=Walton-POS 16
   [Service]
   Type=simple
   User=odoo16
   ExecStart=/opt/waltonpos/waltonpos16/.venv/bin/python3 /opt/waltonpos/waltonpos16/odoo-bin -c /opt/waltonpos/waltonpos16/odoo.conf
   [Install]
   WantedBy=default.target
```
That concludes the setup. You can now reload systemd and start running WaltonPOS16. Since we edited the service file, we need to run daemon-reload

```bash
sudo systemctl daemon-reload
sudo systemctl start odoo16.service
```

Check if WaltonPOS16 is active by running this command:
```bash
sudo systemctl status odoo16.service
```
Now open your web browser and go to “http://<your_server_ip_address>:8069”.