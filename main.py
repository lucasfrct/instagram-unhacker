# Get instance
import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

L = instaloader.Instaloader()

# Login or load session
username = "lucas.ferreira.costa.oficial"
password = ""
try:
    L.login(username, password)
except TwoFactorAuthRequiredException:
    L.two_factor_login(205343)

## rafaell.moreiraa
## Kamila_19
## cristiane.tavares.costa
target_profile = "kamila_martins18"
# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, target_profile)

# Print list of followees
follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
# (likewise with profile.get_followers())

