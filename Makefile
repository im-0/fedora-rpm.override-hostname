.POSIX:
.SUFFIXES: .c .o

CC = gcc

BASE_CFLAGS = -fPIC -std=gnu99 -Wall -Wextra
CFLAGS ?= -O2 -g
BASE_LDFLAGS = -shared
LDFLAGS ?=


all: liboverride-hostname.so

.c.o:
	$(CC) $(BASE_CFLAGS) $(CFLAGS) -c -o $(@) $(<)

liboverride-hostname.so: lib.o
	$(CC) $(BASE_CFLAGS) $(CFLAGS) $(BASE_LDFLAGS) $(LDFLAGS) -o $(@) $(<)

clean:
	rm -f *.o
	rm -f liboverride-hostname.so
