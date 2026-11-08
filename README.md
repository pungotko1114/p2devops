# Shortly
❓ What is this project, in one sentence? What does a user do with it?

This is a link shortener project, a three tier docker setup, a web, api and a database 

## Architecture: three tiers
❓ What does web do? serve as the frontend page and as the frontline for the api 
❓ What does api do? it is a python script that servers as the connection between web and database
❓ What does db do? stores url links
❓ Why split it into three containers instead of one big one? having to isolate each application on a container gives us more flexibility when one app is acting up and needs restart then we do not end up restarting the whole system

💡 A simple diagram helps:

web > api < database


Browser → web → api → db
## Two networks
❓ Who's on frontend? Who's on backend?
❓ Why is api on both? (🌉)
❓ What does internal: true do for backend? What did your wget test show?
❓ If an attacker broke into web, could they reach db? Why not?

💬 You could use the group-chat idea if it helped you understand it. That's your words!

## One published port
❓ Which port is published, and on which service?
❓ What happens when you curl localhost:8000? Why is that good?
❓ What's the general principle? (Hint: least privilege, one front door 🚪)

## Security
❓ List the layers you built. For each one, one line: what attack does it stop?

USER 10001
read_only + tmpfs
cap_drop: ALL
no-new-privileges
secrets instead of environment variables
internal network
## How to run
❓ The exact steps you did in the fresh-clone test:

clone
create .env: which 3 lines?
create the secret: which command?
start: which command?
open: which URL?
💡 Put commands inside code blocks so people can copy them.

## Reliability (optional but nice)
❓ What do restart, healthchecks with depends_on, resource limits and log rotation each protect against?
## Learning materials
This stack is the base for a self-study DevOps track. See [`learn/`](learn/README.md):
- [Docker capstone](learn/docker-capstone.md): build these three Dockerfiles and `compose.yaml` step by step
- [Git CLI lab guide](learn/git-cli-lab-guide.md): six hands-on Git labs on a practice copy of Shortly
- [Git Quest](learn/git-quest/index.html): seven scenario-based Git shifts in a simulated terminal (open the file in a browser)
