/*
 *  Used for bad things, never do this unless
 *  you know what you are doing. This is used
 *  for making your code non portable. Allows
 *  access to functions that are only on GNU
 *  systems.
 */
#define _GNU_SOURCE

/*
 * Includes to make it work. stdio if for
 * standard printing (aka fprintf). 
 *
 * dlfcn is for dlsym and RTLD_NEXT.
 * dlsym is a part of the standard, but
 * RTLD_NEXT is a GNU only constant.
 */
#include <stdio.h>
#include <dlfcn.h>

/*
 * Only for strcpy.
 */
#include <string.h>

/*
 * Function pointer to the real malloc
 */
static void* (*real_malloc)(size_t)=NULL;

/*
 * Our message from our example program.
 */
static char *msg;

/*
 * init function that is ran the first time
 * this library is loaded.
 */
static void mtrace_init(void)
{
    /*
     * Set the function pointer from above to
     * the "real" malloc.
     *
     * dlsym:
     * http://pubs.opengroup.org/onlinepubs/009695399/functions/dlsym.html
     */
    real_malloc = dlsym(RTLD_NEXT, "malloc");
    if (NULL == real_malloc) {
        fprintf(stdout, "Error in `dlsym`: %s\n", dlerror());
    }
}

/*
 * Our fake malloc. It actually calls the "real" malloc, but
 * we add some extra stuff for fun!
 */
void *malloc(size_t size)
{
    if(real_malloc==NULL) {
        mtrace_init();
    }

    void *p = NULL;
    p = real_malloc(size);
    fprintf(stdout, "Address to be used: %p\n", p);

    /*
     * Comment this out for programs besides the example
     * one provided. This sets our message to the address
     * returned by the real malloc.
     */
    msg = p;

    return p;
}

/*
 * Our fake free. This one doesn't call the real free!
 * Memory leaks incoming!!
 */
void free(void *ptr) {
    /*
     * Comment this out for programs besides the example
     * one provided. This changes the data from our example
     * program.
     */
    strcpy(msg, "5678");
    fprintf(stdout, "In Free MSG: %s\n", msg);

    fprintf(stdout, "We didn't free()!\n");
}
