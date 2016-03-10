# RPG Game
A web database driver game concept inspired by Diablo/Hearthstone.

The Idea of the game is when you create an account you can create characters, you then can you play matches with them vs bosses in a turn-based game, using different types of spells with different amount of damage and cooldowns. Playing matches gives you XP to gain access to more spells.

Eventually the idea is to be able to have multiplayer matches with people online. Selling/Buying items that players have picked up from playing games and being able to share "chests" of items.


### Requirements

* Python 2.7.11
* PostgreSQL
* Git

##### If using Windows:
Download and Install: https://www.microsoft.com/en-us/download/details.aspx?id=44266

### Installation


 
```sh
$ git clone https://github.com/JamesJGarner/rpg-game
$ cd rpg-game
```

Create local.py in /game/settings/

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '' # Add in your own
DEBUG = True
```
Once you've filled out the file with your settings run these commands:
```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
```