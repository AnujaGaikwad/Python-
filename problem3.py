comment1 ="Make lot of money"
comment2 ="buy now"
comment3 ="subscribe this"
comment4 ="click this"

message = input("Enter your comment: ")

if((comment1 in message)or(comment2 in message)or(comment3 in message)or(comment4 in message)):
    print("This comment is a spammer")

else:
    print("This comment is not a spammer")
