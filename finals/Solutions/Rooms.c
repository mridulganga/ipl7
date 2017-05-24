#include <stdio.h>
#include <stdlib.h>
#define INF 999

void dij(int a[100][100],int v[100],int d[100],int n, int x)
{
    int i,sindex=-1,svalue=INF;
    v[x]=1;
    for(i=0;i<n;i++)
    {
        if(v[i]==0 && a[x][i])
        {
            if((d[x]+a[x][i])<d[i])
               d[i]=d[x]+a[x][i];
        }
    }

    for(i=0;i<n;i++)
    {
        if(v[i]==0 && d[i]<svalue)
        {
            svalue=d[i];
            sindex=i;
        }
    }

    if(sindex!=-1)
        dij(a,v,d,n,sindex);
}
int main()
{
    int a[100][100],i,j,k,n, v[100],d[100],count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
  for(k=0;k<n;k++){
    for(i=0;i<n;i++)
    {
        d[i]=INF;
        v[i]=0;
    }

    d[k]=0;
    dij(a,v,d,n,k);
    for(i=k+1;i<n;i++){
        if(d[i]%2==0)
            count++;
    }
     }

    printf("%3.2f\n",(float)count/((n*(n-1))/2));

    return 0;
}