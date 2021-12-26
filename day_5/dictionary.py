#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 

user_profile = {
  'age' : 15,
  'username' : 'bossgammer',
  'weapons' : [],
  'is_active' : True,
  'clan' : 'Top clan',
}
print(user_profile.keys())

user_profile.update({'weapons': ['GUN AK41']})
user_profile.update({'is_banned': False})
print(user_profile)
user_profile['is_banned'] = True
print(user_profile.get('is_banned'))

for profile_key in user_profile.items():
  print(profile_key)

user_profile2 = user_profile.copy()
user_profile2.update({'age': 18, 'username': 'Nobe'})

print(user_profile2)