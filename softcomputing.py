def union(A, B):
    R = []
    for i in range(len(A)):
        
        if(A[i]>B[i]):
          R.append(A[i])
        else:
            R.append(B[i])  # Use max for cleaner comparison
        return R  # Don't forget to return the result list

def print_fuzzy_set(U, W):
    # Printing fuzzy set in a specific format A[i]/W[i]
    for i in range(len(U) - 1):
        print(f'{round(U[i], 2)}/{round(W[i], 1)}', end=' + ')
    print(f'{round(U[-1], 2)}/{round(W[-1], 1)}')  # Last element without '+'

# User input for the fuzzy sets
A = list(map(float, input("Enter the values of first fuzzy set: ").strip().split()))
B = list(map(float, input("Enter the values of second fuzzy set: ").strip().split()))
W = list(map(int, input("Enter the weights of each element: ").strip().split()))

U = union(A, B)
    
    # Print the resulting fuzzy set with weights
print_fuzzy_set(U, W)




# def intersection(A, B):
#     R = []
#     for i in range(len(A)):
#         if(A[i]<B[i]):
#           R.append(A[i])
#         else:
#             R.append(B[i]) # Use min for intersection
#     return R

# def print_fuzzy_set(A, W):
#     # Printing fuzzy set in a specific format A[i]/W[i]
#     for i in range(len(A) - 1):
#         print(f'{round(A[i], 2)}/{round(W[i], 1)}', end=' + ')
#     print(f'{round(A[-1], 2)}/{round(W[-1], 1)}')  # Last element without '+'

# # User input for the fuzzy sets
# A = list(map(float, input("Enter the values of first fuzzy set: ").strip().split()))
# B = list(map(float, input("Enter the values of second fuzzy set: ").strip().split()))
# W = list(map(int, input("Enter the weights of each element: ").strip().split()))

# # Ensure all lists have the same length
# if len(A) != len(B) or len(A) != len(W):
#     print("Error: Fuzzy sets and weights must have the same number of elements.")
# else:
#     # Compute the intersection of fuzzy sets A and B
#     R = intersection(A, B)
    
#     # Print the resulting fuzzy set with weights
#     print_fuzzy_set(R, W)



# def complement(A):
#     R = []
#     for i in range(len(A)):
#           s=1-A[i]
#           R.append(s)
#     return R

# def print_fuzzy_set(R, W):
#     # Printing fuzzy set in a specific format A[i]/W[i]
#     for i in range(len(R) - 1):
#         print(f'{round(R[i], 2)}/{round(W[i], 1)}', end=' + ')
#     print(f'{round(R[-1], 2)}/{round(W[-1], 1)}')  # Last element without '+'

# # User input for the fuzzy sets
# A = list(map(float, input("Enter the values of first fuzzy set: ").strip().split()))
# W = list(map(int, input("Enter the weights of each element: ").strip().split()))

# # Compute the Complement of fuzzy sets A and B
# R = complement(A)
# # Print the resulting fuzzy set with weights
# print_fuzzy_set(R, W)





# def complement(C):
#     R = []
#     for i in range(len(C)):
#           s=1-A[i]
#           R.append(s)
#     return R
# def diff(A,B):
#     com_B=complement(B)
#     R = []
#     for i in range(len(A)):
#         if A[i]<com_B:
#             R.append(A[i])
#         else:
#             R.append(com_B)
#     return R

# def print_fuzzy_set(R, W):
#     # Printing fuzzy set in a specific format A[i]/W[i]
#     for i in range(len(R) - 1):
#         print(f'{round(R[i], 2)}/{round(W[i], 1)}', end=' + ')
#     print(f'{round(R[-1], 2)}/{round(W[-1], 1)}')  # Last element without '+'

# # User input for the fuzzy sets
# A = list(map(float, input("Enter the values of first fuzzy set: ").strip().split()))
# B = list(map(float, input("Enter the values of second fuzzy set: ").strip().split()))
# W = list(map(int, input("Enter the weights of each element: ").strip().split()))

# # Compute the differentiation of fuzzy sets A and B
# R = diff(A, B)
# # Print the resulting fuzzy set with weights
# print_fuzzy_set(R, W)






