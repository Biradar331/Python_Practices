# Figure out a way to store 9 and 9.0 as separate values in the set.(you can take help of the built in data types)
values={9,"9"}
print(type(values))
print(values)

# Or we can write it as 

values={
    ('float',9.0),
    ('int',9)
}
print(values)