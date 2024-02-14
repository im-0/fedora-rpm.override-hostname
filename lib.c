#include <errno.h>
#include <stdlib.h>
#include <string.h>

extern char **environ;

int gethostname(char *name, size_t len)
{
	if (!len) {
		errno = ENAMETOOLONG;
		return -1;
	};

	const char *override = getenv("HOSTNAME");
	if (!override) {
		override = "";
	};

	strncpy(name, override, len - 1);
	name[len - 1] = '\0';
	return 0;
}
