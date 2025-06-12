* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * Interacting with web servers


[](https://docs.unity3d.com/6000.0/Documentation/Manual/coroutines.html)
Splitting tasks across frames
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
Common operations: using the HLAPI
# Interacting with web servers
UnityWebRequest provides a modular system for composing HTTP requests and handling HTTP responses. The primary goal of the UnityWebRequest system is to allow Unity games to interact with web browser back-ends. It also supports high-demand features such as chunked HTTP requests, streaming POST/PUT operations, and full control over HTTP headers and verbs.
The system consists of two layers: 
  * A [High-Level API](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html) (HLAPI) wraps the Low-Level API and provides a convenient interface for performing common operations
  * A [Low-Level API](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html) (LLAPI) provides maximum flexibility for more advanced users


## Supported platforms
The UnityWebRequest system supports most Unity platforms:
  * All versions of the Editor and Standalone players
  * Web
  * Mobile platforms: iOS, Android
  * Universal Windows Platform


## Architecture
The UnityWebRequest ecosystem breaks down an HTTP transaction into three distinct operations:
  * Supplying data to the server
  * Receiving data from the server
  * HTTP flow control (for example, redirects and error handling)


To provide a better interface for advanced users, these operations are each governed by their own objects:
  * An `UploadHandler` object handles transmission of data to the server
  * A `DownloadHandler` object handles receipt, buffering and postprocessing of data received from the server
  * A `UnityWebRequest` object manages the other two objects, and also handles HTTP flow control. This object is where custom headers and URLs are defined, and where error and redirect information is stored.

![Data sent from user code passes through an UploadHandler and then a UnityWebRequest before reaching the HTTP web server. Data received from the server passes through a UnityWebRequest and then a DownloadHandler before reaching user code.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UnityWebRequestArchitecture.png) Data sent from user code passes through an UploadHandler and then a UnityWebRequest before reaching the HTTP web server. Data received from the server passes through a UnityWebRequest and then a DownloadHandler before reaching user code.
For any HTTP transaction, the normal code flow is:
  * Create a Web Request object
  * Configure the Web Request object 
    * Set custom headers
    * Set HTTP verb (such as GET, POST, HEAD - custom verbs are permitted on all platforms except for Android)
    * Set URL
  * (Optional) Create an Upload Handler and attach it to the Web Request 
    * Provide data to be uploaded
    * Provide HTTP form to be uploaded
  * (Optional) Create a Download Handler and attach it to the Web Request
  * Send the Web Request 
    * If inside a coroutine, you may Yield the result of the `Send()` call to wait for the request to complete
  * (Optional) Read received data from the Download Handler
  * (Optional) Read error information, HTTP status code and response headers from the UnityWebRequest object


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/coroutines.html)
Splitting tasks across frames
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-hlapi.html)
Common operations: using the HLAPI
