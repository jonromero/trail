t
=======

`trail` helps out jot down ideas *fast* while you are in development, so
when you come back after a while, you'll remember when you left off.
 
Why trail?
------

Did you ever have to work furiously on a project and then had to do something else for a couple of days (or more)?

Whenever I am working on a project (especially a hobby/opensource project) 
and I haven't played around for a while, my main problem is that I don't remember
what I was doing or why I have done certain things.

trail is based on [t][], the simpliest todo manager out there.

[t][https://bitbucket.org/sjl/t/]


### Hehe

[j]: http://github.com/rupa/j2/

### It Plays Nice with Version Control

Other systems keep your tasks in a plain text file.  This is a good thing, and
`t` follows their lead.

However, some of them append new tasks to the end of the file when you create
them.  This is not good if you're using a version control system to let more
than one person edit a todo list.  If two people add a task and then try to
merge, they'll get a conflict and have to resolve it manually.

`t` uses random IDs (actually SHA1 hashes) to order the todo list files.  Once
the list has a couple of tasks in it, adding more is far less likely to cause
a merge conflict because the list is sorted.


Installing trail
------------

`trail` requires [Python][] 2.5 or newer, and some form of UNIX-like shell (bash
works well).  It works on Linux, OS X, and Windows (with [Cygwin][]).

[Python]: http://python.org/
[Cygwin]: http://www.cygwin.com/

Installing and setting up `trail` will take about one minute.

First, [download][] the newest version or clone the Mercurial repository
(`git clone https://github.com/jonromero/trail`).  Put it anywhere you like.

[download]: https://github.com/jonromero/trail/archive/master.zip

Next, decide where you want to keep your "trails".  I put mine in `~/tasks`.
Create that directory:

    mkdir ~/tasks

Finally, set up an alias to run `trail`.  Put something like this in your
`~/.bashrc` file:

    alias t='python ~/path/to/trail.py --task-dir ~/tasks --list tasks'

Make sure you run `source ~/.bashrc` or restart your terminal window to make
the alias take effect.

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

Seeing your trail is even easier -- just use `trails` while you are inside your project:

    $ trail
    9 of August: 10:01 - Trying out a new sorting algorithm
    9 of August: 11:30 - save function is so slow, trying not to save
    9 of August: 11:45 - load doesn't work, I am going to sleep
    $

### Edit/Delete a trail

All your trails are stored in a file called .trails inside your projects directory,
so you can edit them using a text editor.


TODO
---------------
Using `trail` to calculate how much time you spent on a project/feature/bug.
Example:

    $ trail start awesome-feature
    $ trail doing something awesome
    $ trail something else awesome
    $ trail stop awesome-feature

    $ trail --list awesome feature


Contributions 
----------------------------
Do you have an idea, patch, bug, fix or a visualization? Great!

