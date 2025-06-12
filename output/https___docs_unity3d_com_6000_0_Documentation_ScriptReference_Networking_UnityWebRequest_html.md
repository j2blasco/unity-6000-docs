* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html

# UnityWebRequest
class in UnityEngine.Networking
/
Implemented in:[UnityEngine.UnityWebRequestModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UnityWebRequestModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Provides methods to communicate with web servers.
`UnityWebRequest` handles the flow of HTTP communication with web servers. To download and upload data, use [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) and [UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) respectively.   
  
`UnityWebRequest` includes static utility functions that return `UnityWebRequest` instances configured for common use cases. For example: 
  * [UnityWebRequest.Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)
  * [UnityWebRequest.Post](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html)
  * [UnityWebRequest.Put](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Put.html)


To send a web request from a `UnityWebRequest` instance, call [UnityWebRequest.SendWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html). After the `UnityWebRequest` begins to communicate with a remote server, you can't change any of the properties in that `UnityWebRequest` instance. HTTPS is supported, server certificate is validated against the root certificate store available on the system the app runs on. Validation can be disabled (for example for development server using self-signed certificate) or changed to a custom handling by assigning [UnityWebRequest.certificateHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-certificateHandler.html) property.   
  
Depending on the platform your application runs on, `UnityWebRequest` either sets the [User-Agent header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) itself or leaves it for the operating system to set. `UnityWebRequest` sets the `User-Agent` header for all platforms except iOS and WebGL.   
  
**Note** : From Unity 2019.2, `UnityWebRequest` sets the `User-Agent` header for Android devices. In earlier releases, the operating system set the `User-Agent` header.   
  
**Note** : If the device that the application runs on uses proxy settings, `UnityWebRequest` applies the proxy settings after the application sends the request.
### Static Properties
Property | Description  
---|---  
[kHttpVerbCREATE](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbCREATE.html) | The string "CREATE", commonly used as the verb for an HTTP CREATE request.  
[kHttpVerbDELETE](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbDELETE.html) | The string "DELETE", commonly used as the verb for an HTTP DELETE request.  
[kHttpVerbGET](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbGET.html) | The string "GET", commonly used as the verb for an HTTP GET request.  
[kHttpVerbHEAD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbHEAD.html) | The string "HEAD", commonly used as the verb for an HTTP HEAD request.  
[kHttpVerbPOST](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbPOST.html) | The string "POST", commonly used as the verb for an HTTP POST request.  
[kHttpVerbPUT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-kHttpVerbPUT.html) | The string "PUT", commonly used as the verb for an HTTP PUT request.  
### Properties
Property | Description  
---|---  
[certificateHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-certificateHandler.html) | Holds a reference to a CertificateHandler object, which manages certificate validation for this UnityWebRequest.  
[disposeCertificateHandlerOnDispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-disposeCertificateHandlerOnDispose.html) | If true, any CertificateHandler attached to this UnityWebRequest will have CertificateHandler.Dispose called automatically when UnityWebRequest.Dispose is called.  
[disposeDownloadHandlerOnDispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-disposeDownloadHandlerOnDispose.html) | If true, any DownloadHandler attached to this UnityWebRequest will have DownloadHandler.Dispose called automatically when UnityWebRequest.Dispose is called.  
[disposeUploadHandlerOnDispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-disposeUploadHandlerOnDispose.html) | If true, any UploadHandler attached to this UnityWebRequest will have UploadHandler.Dispose called automatically when UnityWebRequest.Dispose is called.  
[downloadedBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-downloadedBytes.html) | Returns the number of bytes of body data the system has downloaded from the remote server. (Read Only)  
[downloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-downloadHandler.html) | Holds a reference to a DownloadHandler object, which manages body data received from the remote server by this UnityWebRequest.  
[downloadProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-downloadProgress.html) | Returns a floating-point value between 0.0 and 1.0, indicating the progress of downloading body data from the server. (Read Only)  
[error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-error.html) | A human-readable string describing any system errors encountered by this UnityWebRequest object while handling HTTP requests or responses. The default value is null. (Read Only)  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-isDone.html) | Returns true after the UnityWebRequest has finished communicating with the remote server. (Read Only)  
[isModifiable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-isModifiable.html) | Returns true while a UnityWebRequest’s configuration properties can be altered. (Read Only)  
[method](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-method.html) | Defines the HTTP verb used by this UnityWebRequest, such as GET or POST.  
[redirectLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-redirectLimit.html) | Indicates the number of redirects that this UnityWebRequest follows before halting with a Redirect Limit Exceeded system error.  
[responseCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-responseCode.html) | The numeric HTTP response code returned by the server, such as 200, 404 or 500. (Read Only)  
[result](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-result.html) | The result of this UnityWebRequest.  
[timeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-timeout.html) | The number of seconds after which UnityWebRequest attempts to abort the request if no response is received.  
[uploadedBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uploadedBytes.html) | Returns the number of bytes of body data the system has uploaded to the remote server. (Read Only)  
[uploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uploadHandler.html) | Holds a reference to the UploadHandler object which manages body data to be uploaded to the remote server.  
[uploadProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uploadProgress.html) | Returns a floating-point value between 0.0 and 1.0, indicating the progress of uploading body data to the server.  
[uri](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uri.html) | Defines the target URI for the UnityWebRequest to communicate with.  
[url](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-url.html) | Defines the target URL for the UnityWebRequest to communicate with.  
[useHttpContinue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-useHttpContinue.html) | Determines whether this UnityWebRequest will include Expect: 100-Continue in its outgoing request headers. (Default: true).  
### Constructors
Constructor | Description  
---|---  
[UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-ctor.html) | Creates a UnityWebRequest with the default options and no attached DownloadHandler or UploadHandler. Default method is GET.  
### Public Methods
Method | Description  
---|---  
[Abort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Abort.html) | If in progress, halts the UnityWebRequest as soon as possible.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Dispose.html) | Signals that this UnityWebRequest is no longer being used, and should clean up any resources it is using.  
[GetRequestHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetRequestHeader.html) | Retrieves the value of a custom request header.  
[GetResponseHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetResponseHeader.html) | Retrieves the value of a response header from the latest HTTP response received.  
[GetResponseHeaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetResponseHeaders.html) | Retrieves a dictionary containing all the response headers received by this UnityWebRequest in the latest HTTP response.  
[SendWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html) | Begin communicating with the remote server.  
[SetRequestHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SetRequestHeader.html) | Set a HTTP request header to a custom value.  
### Static Methods
Method | Description  
---|---  
[ClearCookieCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.ClearCookieCache.html) | Clears stored cookies from the cache.  
[Delete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Delete.html) | Creates a UnityWebRequest configured for HTTP DELETE.  
[EscapeURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.EscapeURL.html) | Escapes characters in a string to ensure they are URL-friendly.  
[GenerateBoundary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GenerateBoundary.html) | Generate a random 40-byte array for use as a multipart form boundary.  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html) | Create a UnityWebRequest for HTTP GET.  
[Head](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Head.html) | Creates a UnityWebRequest configured to send a HTTP HEAD request.  
[Post](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html) | Creates a UnityWebRequest configured to send form data to a server via HTTP POST.  
[PostWwwForm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.PostWwwForm.html) | Creates a UnityWebRequest configured to send form data to a server via HTTP POST.  
[Put](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Put.html) | Creates a UnityWebRequest configured to upload raw data to a remote server via HTTP PUT.  
[SerializeFormSections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SerializeFormSections.html) | Converts a List of IMultipartFormSection objects into a byte array containing raw multipart form data.  
[SerializeSimpleForm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SerializeSimpleForm.html) | Serialize a dictionary of strings into a byte array containing URL-encoded UTF8 characters.  
[UnEscapeURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.UnEscapeURL.html) | Converts URL-friendly escape sequences back to normal text.  
* * *
