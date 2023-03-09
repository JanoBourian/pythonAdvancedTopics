# Tasks

Tasks is an object useful to create sequence of coroutines, for example in a for loop. 

## Task Cancellation 

Is important that the coroutines uses *try/except* stament, because that help us to robust our code. 

## Task Groups 

Remember when you created a coroutine you can create a lot of task inside a coroutine for execute those tasks.

## Sleeping 

If you have an event loop with full duration, you can use the sleep for avoid blocking it. 