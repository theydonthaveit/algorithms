# eager approach to union find
# data structure: id[] of size N
# interpretation: p and q are conneceted iff they have the same id
# id[]: 0,0 1,1 2,1 3,8 4,8 5,0 6,0 7,1 8,8 9,8
# therefore: {0,5,6} {1,2,7} {3,4,8,9}

# JAVA EXAMPLE (expensive):
#public class QuickFindUF
#{
#    private int[] id;
#    public QuickFindUF(int N)
#    {
#        id = new int[N]
#        for (int i = 0; i < N; i++)
#            id[i] = i;
#    }
#
#    public boolean connected(int p, int q)
#    { return id[p] == id[q]; }
#
#    public void union(int p, int q)
#    {
#        int pid = id[p];
#        int qid = id[q];
#        for (int i = 0; i < id.lenght; i++)
#            if (id[i] == pid) id[i] = qid;
#    }
#}
