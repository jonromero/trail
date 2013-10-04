trail
=======

`trail` helps out jot down ideas *fast* while you are in development, so
when you come back after a while, you'll remember when you left off.
 
Why trail?
------

Did you ever have to work furiously on a project and then had to do something else for a couple of days (or more)?

Whenever I am working on a project (especially a hobby/opensource project) 
and I haven't played around for a while, my main problem is that I don't remember
what I was doing or why I have done certain things.

The first version of trail was inspired by [t](https://bitbucket.org/sjl/t/), the simpliest todo manager out there,
and it was written in Python (you can see older commits). After some thought, it was
trivial to implement this in bash, so I did it.



Installing trail
------------

Installing and setting up `trail` will take about a second.

First, download the newest version of `trail` file and place it inside "/usr/bin".

And you are done!

Using trail
-------

`trail` is quick and easy to use.

### Add a trail (thought)

To add a trail, use `trail [thought]`:

    $ trail Trying out a new sorting algorithm
    $ trail save function is so slow, trying not to save
    $ trail load doesn't work, I am going to sleep
    $

### List Your trails

Seeing your trail is even easier -- just use `trails -l number` while you are inside your project:

    $ trail -n 3
    9 of August 10:01 -> Trying out a new sorting algorithm
    9 of August 11:30 -> save function is so slow, trying not to save
    9 of August 11:45 -> load doesn't work, I am going to sleep
    $

### Edit/Delete a trail

All your trails are stored in a file called .trails inside your projects directory, so you can edit them using a text editor.

### Add to repository
Add the .trails file to your repository

### Different users
A user could have a personal trail by exporting TRAIL_USER:
`export TRAIL_USER=yourname`

Remember to run this everytime before you run trail (probably put it in your .bashrc)

Contributions 
----------------------------
Do you have an idea, patch, bug, fix or a visualization? Great!

