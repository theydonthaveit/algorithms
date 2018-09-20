# lazy approach
# integar array id[] of size N
# interpratation: id[i] is parent of i
# Root of i is id[id[id[...id[i]...]]]
# EXAMPLE:
# id[]: 0,0 1,1 2,9 3,4 4,9 5,6 6,6 7,7 8,8 9,9
# {0} {1} {9-2 9-4 9-4-3} {6-5} {7} {8}

#public class QuickUnionUF
#{
#    private int[] id;
#    public QuickUnionUF(int N)
#    {
#        id = new int(N)
#        for (int i = 0; i < N; i++) id[i] = i;
#    }
#
#    private int root(int i)
#    {
#        while (i !- id[i]) i = id[i];
#        return i;
#    }
#
#    public boolean connected(int p, int q)
#    {
#        return root(p) == root(q);
#    }
#
#    public void union(int p, int q)
#    {
#        int i = root(p);
#        int j = root(q);
#        id[i] = j;
#    }
#}
