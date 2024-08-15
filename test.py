def factorial(n):
    product=1 # Start with $1$
    for k in range(2,n+1): # For each $k=2,3,\ldots,n$,
    product*=k # Multiply by $k$
    return product