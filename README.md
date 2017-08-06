# Sorting Algorithm
1.`Insertion sort` is a sorting algorithm that builds a final sorted array (sometimes called a list) one element at a time. While sorting is a simple concept, it is a basic principle used in complex computer programs such as file search, data compression, and path finding. Running time is an important thing to consider when selecting a sorting algorithm since efficiency is often thought of in terms of speed. Insertion sort has an average and worst-case running time of `O(n**2)`, so in most cases, a faster algorithm is more desirable.

![](https://ds055uzetaobb.cloudfront.net/image_optimizer/5fc8daa9296837453ccbc8c7f9c2494bbd1fcdda.gif)

```python
for i = 1 to length(A)
    x = A[i]
    j = i - 1
    while j >= 0 and A[j] > x
        A[j+1] = A[j]
        j = j - 1
    end while
    A[j+1] = x
 end for
```

2. `Bubble sort` Bubble Sort is a simple, inefficient sorting algorithm used to sort lists. It is generally one of the first algorithms taught in computer science courses because it is a good algorithm to learn to build intuition about sorting. While sorting is a simple concept, it is a basic principle used in complex computer programs such as file search, data compression, and path finding. Running time is an important thing to consider when selecting a sorting algorithm since efficiency is often thought of in terms of speed. Bubble Sort has an average and worst-case running time of `O(n**2)` , so in most cases, a faster algorithm is more desirable.


![Bubble sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/4f60337caedcc96ffeb08692e4f8d00f5cb3fd58.gif)

```python
Bubble-sort(a)
  for i = a.length() to 1
       for j = 1 to i-1
                 if a[j]>a[j+1]
                          swap(a[j],a[j+1])
                 end if
```
