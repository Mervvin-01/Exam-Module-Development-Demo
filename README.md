# Odoo 17 Custom Module Installation Guide

## Getting Started

To help you get started with installing a custom module in Odoo 17, follow the steps below.

Already familiar with Odoo? Just dive into the process or [use the guide below](#steps-to-install-the-module).

## Configure Your Odoo Installation

- [ ] **Locate and Edit the `odoo.conf` File**:
   - The configuration file is typically located at `/etc/odoo.conf`.
   - Open the file using a text editor, e.g., `sudo nano /etc/odoo.conf`.
   - Add the path to your custom module in the `addons_path` line.
   - Set the admin password by adding or editing the `admin_passwd` parameter.
   ```ini
   addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom_addons
   admin_passwd = your_admin_password

## Restart the Odoo Service:
  Apply the changes by restarting the Odoo service.
    sudo systemctl restart odoo

## Create or Select a Database
  Access the Odoo Login Page:
    Go to http://your_server_ip:8069 in your web browser.
 
## Manage Databases
  Click on "Manage Databases" on the login page.
  To create a new database, click "Create Database".
  Fill in the required details, and use the admin password set in odoo.conf.

  Log In to Your Database:
    Use the credentials you set to log in.

## Steps to Install the Module

  Navigate to the Apps Menu:
    After logging in, go to the Apps menu. You may need to enable Developer Mode to see this option.
  
  Update the Apps List:
    Click on "Update Apps List" to refresh the available modules.
  
  Search for the Custom Module:
    Use the search bar to find your module by name.
  
  Install the Module:
    Click on the Install button next to your module.

## Start Using the Module

  Access the Module:
    Go to the main menu and select the module you installed.
  
  Begin Using the Module:
    Explore the module's features and start using it as needed.
