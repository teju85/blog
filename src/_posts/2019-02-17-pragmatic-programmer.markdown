---
layout: post
title: "Pragmatic Programmer"
tags: book-notes programming
---

### Pragmatic Programmer
"Pragmatic Programmer - from journeyman to master" is a book on programming
written by Andrew Hunt and David Thomas. This book can be found
[here](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X).
IMO, every programmer who codes for living should read this in order to understand
how to convert requirements to specifications to a flexible and maintainable code.
One message that stands out from this book is "You shouldn't be wedded to any
particular technology, but have a broad enough background and experience base to
allow you to choose good solutions in particular situations."

### Summary
#### Naming
* Use intention revealing names
* Avoid ambiguous variable names
* Use pronounceable names
* Class names must be nouns
* Method names must be verbs
* Choose a consistent style and stick to it!

#### Comments
* Comments Lie!
* Avoid them as much as possible
* Don’t keep commented code. Delete it!

#### Data Structures
* Don’t blindly add getters and setters
* Objects and data structures are anti-symmetric!
* Avoid creating hybrid of these two!

#### Error Handling
* Use exceptions rather than error codes
* Provide meaningful messages with the exceptions thrown
* Create exception classes based on the needs of the caller

#### TDD
* Write tests first, code later!
* Test code is as important as production code
* When in doubt follow the above rule!

#### Classes
* Should follow SRP
* Should follow OCP
* Should follow DIP
* When classes lose cohesion, split them

#### Systems
* Construction of a system must be separated from its use
* One such mechanism is Dependency Injection
* Use the simplest thing that can possibly work.

#### Functions
* Must be small
* Must do only one thing
* Use descriptive names
* Have less number of input arguments
* Have no side effects
* Try to avoid output arguments
* Always follow command-query-separation
* Prefer exceptions to returning error codes
* Don’t Repeat Yourself (DRY)!

#### Formatting
* Small source files preferable over large ones
* Use vertical blank lines for visual cues
* Concepts closely related must be vertically closer
* This is just like paragraphs 
* Keep all instance variables at one place
* Keep the lines short

#### Boundaries
* User learning-tests to understand third party APIs
* Isolate boundaries through wrapping them inside our own class

#### Emergence
* Four rules of simple design:
* Runs all tests
* Contains no duplication
* Expresses programmer’s intent
* Minimum number of classes and methods

#### Concurrency
* Try to avoid sharing data
* Keep the concurrent code separate
* Avoid using more than one method on shared object
* Keep your synchronized sections as small as possible
* Treat spurious failures as candidate threading issues
* Get your non-threaded code working first
* It is better when broken code fails as early as possible
