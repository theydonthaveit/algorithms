# weighted quick unions - logirithmic
# Avoids tall trees
# keep track of the length of the tree
# balace is ensured by linking root of smaller tree to root of larger tree

# EXAMPLE CODE ADD TO QUICK-UNION
# data structure is the same but add an extra array sz[i] - count the objetcs in the tree
# find remains the same - return root(p) == root(q);
# below j = root(q);
# >>>>>
# if (i == j) return;
# if (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
# else               { id[j] = i; sz[i] += sz[j]; }


# flatten the tree gives extra performance (path compression) - close enough to linear
# i.e. each node along the path we touch can be set to the rooti
# ackerman function slower than lg*N
# EXAMPLE CODE:
# while (i != id[i] )
# {
# >>>>>
# id[i] = id[id[i]];
