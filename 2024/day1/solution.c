#include<stdlib.h>
#include<stdio.h>


int int_cmp(const void *a, const void *b){
    int x = *(const int*)a, y = *(const int*)b;
    return (x>y)-(x<y);
}


int main(void){
    size_t n = 0;
    int *p = NULL, *q = NULL;

    FILE *file = fopen("input", "r");
    if (file == NULL) return EXIT_FAILURE;

    for(int x, y; fscanf(file, "%d %d", &x, &y) == 2;){
        ++n;
        p=realloc(p, n*sizeof*p);
        q=realloc(q, n*sizeof*q);
        if (p == NULL || q == NULL) return EXIT_FAILURE;
        p[n-1] = x, q[n-1] = y;
    }

    fclose(file);

    qsort(p, n, sizeof(int), int_cmp);
    qsort(q, n, sizeof(int), int_cmp);

    int r1 = 0;
    for(size_t i=0; i<n; ++i){
        r1 += abs(p[i] - q[i]);
    }

    printf("%d", r1);
    
    putchar('\n');
    
    int r2 = 0;
    
    for(size_t i=0, j=0; i<n && j<n;){
        int count = 0;
        const int p_i = p[i];
        while(j<n && p_i > q[j]) ++j;
        while(j<n && p_i == q[j]) ++j, count+=p_i;
        while(i<n && p_i == p[i]) ++i, r2+=count;
    }

    printf("%d", r2);
    
    free(p), free(q);

    return EXIT_SUCCESS;
}