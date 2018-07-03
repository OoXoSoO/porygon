# Random point problem
The goal of this problem is to generate a random point inside a given polygon. You should modify the ```generate_random_point``` inside randompoint file to make it return a point in tuple format ```(x,y)```.
This functions recieves a polygon as an input. 

The polygon is a sorted list of points, each point represents a vertex of the polygon. For example, a simple square will be represented as ```[(0,0), (0,1), (1,1), (1,0)]```

Remarks
- Points in the edge of the polygon are not considered to be inside it.
- Polygons will not have holes
