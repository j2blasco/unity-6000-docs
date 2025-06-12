* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-upload-handlers.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Interacting with web servers](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request.html)
  * [Advanced operations: Using the LLAPI](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-llapi.html)
  * Creating UploadHandlers


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html)
Creating UnityWebRequests
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-download-handlers.html)
Creating DownloadHandlers
# Creating UploadHandlers
Currently, there are two types of upload handlers available: `UploadHandlerRaw` and `UploadHandlerFile`.
`UploadHandlerRaw` class accepts a data buffer at construction time. When this buffer is an array of bytes, it’s copied internally into native code memory. `UnityWebRequest` system uses this buffer when the remote server is ready to receive the request body data. When the buffer is provided as a `NativeArray`, no copying is performed.
`UploadHandlerFile` allows you to send the contents of a file as the request body. Using this handler, you can send a large file to a server without using a lot of memory. As the handler reads data from the file and then sends it, only a small fraction of the file is kept in memory at any given time.
Upload Handlers also accept a Content Type string. This string is used for the value of the UnityWebRequest’s `Content-Type` header if you set no `Content-Type` header on the UnityWebRequest itself. If you manually set a `Content-Type` header on the UnityWebRequest object, the `Content-Type` on the Upload Handler object is ignored.
If you do not set a `Content-Type` on either the UnityWebRequest or the `UploadHandler`, the system defaults to setting a `Content-Type` of `application/octet-stream`.
`UnityWebRequest` has a property `disposeUploadHandlerOnDispose`, which defaults to true. If this property is true, when UnityWebRequest object is disposed, Dispose() will also be called on attached upload handler rendering it useless. If you keep a reference to upload handler longer than the reference to UnityWebRequest, you should set disposeUploadHandlerOnDispose to false.
## Example
```
byte[] payload = new byte[1024];
// ... fill payload with data ...

UnityWebRequest wr = new UnityWebRequest("https://www.mysite.com/data-upload");
UploadHandler uploader = new UploadHandlerRaw(payload);

// Sends header: "Content-Type: custom/content-type";
uploader.contentType = "custom/content-type";

wr.uploadHandler = uploader;

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-unity-web-requests.html)
Creating UnityWebRequests
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-request-creating-download-handlers.html)
Creating DownloadHandlers
