* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html)
  * [Advanced operations: Using the LLAPI](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html)
  * Creating UnityWebRequests


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html)
Advanced operations: Using the LLAPI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-upload-handlers.html)
Creating UploadHandlers
# Creating UnityWebRequests
WebRequests can be instantiated like any other object. Two constructors are available:
  * The standard, parameter-less constructor creates a new UnityWebRequest with all settings blank or default. The target URL isn’t set, no custom headers are set, and the redirect limit is set to 32.
  * The second constructor takes a string argument. It assigns the UnityWebRequest’s target URL to the value of the string argument, and is otherwise same as the parameter-less constructor.


Multiple other properties are available for setting up, tracking status and checking result or UnityWebRequest.
## Example
```
UnityWebRequest wr = new UnityWebRequest(); // Completely blank
UnityWebRequest wr2 = new UnityWebRequest("https://www.mysite.com"); // Target URL is set

// the following two are required to web requests to work
wr.url = "https://www.mysite.com";
wr.method = UnityWebRequest.kHttpVerbGET;   // can be set to any custom method, common constants provided

wr.useHttpContinue = false;
wr.chunkedTransfer = false;
wr.redirectLimit = 0;  // disable redirects
wr.timeout = 60;       // don't make this small, web requests do take some time

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html)
Advanced operations: Using the LLAPI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-upload-handlers.html)
Creating UploadHandlers
