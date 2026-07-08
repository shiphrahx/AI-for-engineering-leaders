**Image upload PR**

We did a big refactor to move image processing into an async worker queue using Kafka. Basically, in order to make this work we had to add middleware and fix a race condition in the serialization path.

As you know, this was a lot of work. It's worth noting the code is much cleaner now.
