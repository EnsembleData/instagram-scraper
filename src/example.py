from instagram_interface import Instagram_I_ED


# Get a free token at www.influencerhunters.com
TOKEN = "YOUR TOKEN HERE"

#Initialize sender class 
tt = Instagram_I_ED(token_ED_API=TOKEN)

#Send the request to the ED server
print("sending the request..")
res, success = tt.get_user_posts_from_username(username="cristiano", depth=1, oldest_timestamp=1611308425 )


if success:
    print("Success!")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")