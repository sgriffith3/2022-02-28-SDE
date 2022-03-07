# Adding a Second Deploy Key to BCHD

1. On bchd, move to the `~/.ssh` dir:
    
    `student@bchd:~$` `cd ~/.ssh`

0. Generate a new key.

    `student@bchd:~/.ssh$` `ssh-keygen -f newkey`

    > Hit Enter through the prompts

0. Cat out the newkey.pub file.

    `student@bchd:~/.ssh$` `cat newkey.pub`

0. Copy the contents from the step above in as a new Deploy Key for your second repo. 

    > Make sure you select **Allow Write Access**!

0. Add the following to the end of your ssh config file:

    `student@bchd:~/.ssh$` `vim config`

    ```
    Host myproject.com
      HostName github.com
      IdentitiesOnly yes
      IdentityFile ~/.ssh/newkey
      user git
    ```

    > Note: Keep the host as "myproject.com" - no matter what your project is called.

0. Replace your new project repo's git config (assuming it is cloned already and called **myproject**).

    `student@bchd:~$` `sed -i 's/github.com/myproject.com/g' ~/myproject/.git/config`

    > Keep the "myproject.com" as written here to reference the SSH config file correctly. But you may need to change `~/myproject` to represent your actual directory.

