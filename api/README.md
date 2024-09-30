# Learning APIs

#### What are APIs? How are they used and why are they so popular?

APIs (Application Programming Interfaces) are tools that allow different software applications to communicate and 
exchange data.

APIs are used for tasks like fetching data, updating records, or triggering processes across different software applications. 
They are popular because they:

* Simplify integration between systems.
* Allow faster development.
* Promote modularity and scalability.
* Enable third-party developers to build on top of existing services.

#### Create a diagram to showcase the data transfer process in API communication.
```
                 Request
       -------------------------->
Client                            API Server
       <--------------------------
                 Response
```

#### What is a REST API? What makes an API RESTful? What are the REST guidelines?

A REST API (Representational State Transfer) is a web-based API that follows REST principles. 

An API is RESTful if it adheres to the following guidelines:

* **Statelessness:** Each request from the client to the server must contain all necessary information to understand and process it -
The server does not store any information about previous interactions with a client. 
* **Client-Server:** The server and client should be separate.
* **Uniform Interface:** Resources should be accessible via a consistent, well-defined URI.
* **Cacheable:** Responses can be cached to improve performance.
* **Layered System:** The architecture should allow multiple layers to be present between the client and server.

Guidelines:

* Resource Identification: Resources are identified via URIs.
* Representation of Resources: Resources can be represented in different formats (JSON, XML).
* Self-descriptive messages: Requests should contain all necessary information (using methods like GET, POST).
* Hypermedia as the engine of application state (HATEOAS): Clients navigate the application through links provided dynamically by the server.

#### What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

HTTP stands for Hypertext Transfer Protocol. It is used for transferring hypertext (web pages) and other data across the web. 
It encrypts HTTP communication to secure the data transfer between client and server using SSL/TLS encryption.

#### Explain HTTP request structure using the diagrams provided, or your own.

Structure:
* URL
* Method
* Headers
* Body

#### Explain HTTP response structure using the diagram provided, or your own.

Structure:
* Status line
* Headers
* Body

#### What are the 5 HTTP verbs and what do they do?

* GET: Retrieves data from the server (read-only).
* POST: Sends data to the server to create a new resource.
* PUT: Updates an existing resource with new data (replaces the resource).
* PATCH: Partially updates an existing resource.
* DELETE: Removes a resource from the server.

#### What is statelessness? Show examples of “stateless” and stateful http requests.

Statelessness means that each HTTP request is independent, and the server does not store any information about previous requests.

#### What is caching?

Caching is the process of storing copies of frequently accessed resources or responses to speed up subsequent requests. 
For example, when a resource is requested, the server might return a "Cache-Control" header to indicate how long the response 
should be cached to reduce the server load.