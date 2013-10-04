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

The first version of trail was inspired by [t][], the simpliest todo manager out there,
and it was written in Python (you can see older commits). After some thought, it was
trivial to implement this in bash, so I did it.

[t][https://bitbucket.org/sjl/t/]


Installing trail
------------

Installing and setting up `trail` will take about a second.

First, download the newest version of `trail` file and place it at "/usr/bin".

And you are done!

Now, when you run `trail some_text`, a "." file with your name and "_trail" will be created
with that text and the current date, in the same path. This is a simple text file that you can open with a text editor. I usually have this file in the same root folder of my project.

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

All your trails are stored in a file called ."your_username"_trails inside your projects directory, so you can edit them using a text editor.


Contributions 
----------------------------
Do you have an idea, patch, bug, fix or a visualization? Great!

