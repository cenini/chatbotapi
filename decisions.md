# Decisions

## Stack

I decided to go with a Python-based stack, as it was requested, and in addition, I saw it as a good opportunity to get the chance to go outside of my comfort zone a bit, and learn something new. In addition, I wanted to try the new `FastAPI`, which seemed like a suitable framework for this project. It seemed really quick to get started, and to also have solid performance and a pretty rich feature set.

I knew right away that I wanted to run a database service as a side-car. I opted to go with a NoSQL database. At this stage, either a NoSQL or SQL database could have been fine. But I didn't want to set up all the boilerplate necessary to run a SQL database for this sized project. Depending on the flexibility of the chat item model, it could definitely still be a good idea to keep working with MongoDb as the database provider. 

## Improvements

At this stage, I decided to not spend time on implementing security best practices. E.g. using secrets for credentials would make the application a bit harder to set up in different environments. And additionally, also take some additional time. Of course, the API needs to be hosted with TLS configured, etc.

In addition, there are lots of improvements for the database: Adding actual indexing, designing better querys, etc.

Finally, one could definitely take a closer look at error codes, see if they need additional improvements or not. At a first glance, they seem to make a lot of sense.