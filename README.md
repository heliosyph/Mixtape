# Mixtape

**Mixtape automatically creates a collaborative playlist using your own and any number of friends' music tastes and favorite songs smoothly blended together so that everyone can listen.  Just link any assortment of playlists you want and Mixtape will shuffle through them all.  Mixtape is perfect for providing group sessions with music that each member can enjoy listening to in the background.
Mixtape has other uses too, like providing users with a new way to experiment with their music.  Not everyone likes to jump right into a new genre, but Mixtape provides a new opportunity for usersto choose how they can.  The variety is dependent on the user as they can choose how many albums or playlists to pool together, so they can get a bit of everything or something more specific. Mixtape can pick and choose songs that are similar among playlists, which can allow users to discover songs close to their style.  It can also choose songs at random for users to experiment listening to.
**

**https://fa22-team-a.herokuapp.com/**

The project is deployed on Heroku:
[https://cmps-453-project-template.herokuapp.com/](https://cmps-453-project-template.herokuapp.com/)

To develop the Django application, clone this repository and follow the instructions:

## What's Already Included in the Django Template?

-   User Authentication System:
    -   [Login](https://cmps-453-project-template.herokuapp.com/accounts/login/)
    -   [User Registration](https://cmps-453-project-template.herokuapp.com/accounts/signup/)

## Create Python Virtual Environment

```bash
virtualenv --python=/usr/bin/python3 .venv  # for UNIX and MacOS bash/zsh
```

```bash
python -m virtualenv .venv                  # for Windows git bash and Windows CMD
```

## Activate Python Virtual Environment

```bash
source .venv/bin/activate                   # for UNIX and MacOS bash/zsh
```

```bash
source .venv/Scripts/activate               # for Windows git bash
```

```cmd
.venv\Scripts\activate.bat                  # for Windows CMD
```

For the following steps and for development, keep the virtual environment activated all the time.

## Install Python Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Collect Static Files

```bash
python manage.py collectstatic --no-input
```

## Run the Django Web Server

```bash
python manage.py runserver
```

## Developer's Guide

### Visual Studio Code

It's highly recommended to use [VSCode](https://code.visualstudio.com/) for the development.

The project repository includes VSCode-specific settings ([.vscode/settings.json](.vscode/settings.json))
that are helpful for developing Django applications.

With the python virtual environment active, from the root of the repository,
open the VSCode using the following command:

```bash
code .
```

Please install all the extensions (specified in [.vscode/extensions.json](.vscode/extensions.json))
recommended by VSCode upon opening the project in the code editor.

The [requirements.txt](requirements.txt) file includes the python packages required for some
of the VScode extensions. That's why VSCode needs to be opened from the bash or command
line with an active python virtual environment in which all the project-specific python packages
are installed.

Some fonts to reduce eye strain and provide better coding experience:

-   [FiraCode](https://github.com/tonsky/FiraCode)
-   [Jet Brains Mono](https://github.com/JetBrains/JetBrainsMono)
-   [Hack](https://github.com/source-foundry/Hack)

### GitLab CI/CD pipelines

Before performing a `git push`, run these commands to ensure that the new code changes passes
the pipeline stages:

#### Python linting

**Pipeline Stage**: _lint_

To ensure code changes meet the python coding and documentation standards, run the following
commands:

```bash
pylama .
```

If the above command raises errors, fix the lines specified in the error messages.

#### Django migrations

**Pipeline Stage**: _build_

To ensure Django migration files are created, applied, and added to git, run the following commands:

```bash
python manage.py makemigrations --check
python manage.py migrate --check
```

If the any of the above commands raises an error, create migration files and add to the commit.

#### Django Tests

**Pipeline Stage**: _test_

To ensure code changes passes all unit tests, run the following commands:

```bash
python manage.py test
```

## Team Members

**Update the last name, first name, Heroku app name, and URLs in the table below **

| Role     | Last Name  | First Name | Heroku App                           |
| -------- | ---------- | ---------- | ------------------------------------ |
| Member A | Washington | Cameron    | https://fa22-team-a-a.herokuapp.com/ |
| Member B | Canelas    | Amy        | https://fa22-team-a-b.herokuapp.com/ |
| Member C | Brinkley   | Luke       | https://fa22-team-a-c.herokuapp.com/ |
| Member D | Lasserre   | Kristian   | https://fa22-team-a-d.herokuapp.com/ |

## (Optional) Use Docker Containers for Development

See [DOCKER.md](DOCKER.md) file.
