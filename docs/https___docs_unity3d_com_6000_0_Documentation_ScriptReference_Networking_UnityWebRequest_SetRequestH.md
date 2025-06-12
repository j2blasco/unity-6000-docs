* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SetRequestHeader.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).SetRequestHeader
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
## Declaration
public void SetRequestHeader(string name, string value); 
### Parameters
Parameter | Description  
---|---  
name | The key of the header to be set. Case-sensitive.  
value | The header's intended value.  
### Description
Set a HTTP request header to a custom value.
Header keys and values must be valid according to HTTP protocol specification. Neither string may contain certain illegal characters, such as control characters. Both strings must be non-null and contain a minimum of 1 character. For more information, see [HTTP specifications](https://www.w3.org/Protocols/).  
  
This method can't be called after [SendWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html) is called.  
  
It is not recommended to set these headers to these custom values: `Accept-Charset`, `Accept-Encoding`, `Access-Control-Request-Headers`, `Access-Control-Request-Method`, `Connection`, `Date`, `Dnt`, `Expect`, `Host`, `Keep-Alive`, `Origin`, `Referer`, `Te`, `Trailer`, `Transfer-Encoding`, `Upgrade`, `Via`. Due to different limitations across platforms, the custom value might be overridden, ignored, or unsupported, therefore the resulting behavior is unreliable. It is strongly recommended to leave these headers for automatic handling unless you want to risk viewing any unexpected results.  
  
The `Accept-Encoding` header is automatically set to supported encodings. Use of a different value is ignored or might cause request to fail. For more information, refer to the [Mozilla docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) on Accept-Encoding.  
  
The `Content-Length` header is automatically populated based on the contents of the attached [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) if any, and can't be set to a custom value.  
  
The `X-Unity-Version` header is automatically set by Unity and might not be set to a custom value.  
  
The `User-Agent` header is automatically set by Unity and it's not recommended to set it to a custom value.  
  
The `Cookie` and `Cookie2` headers are automatically managed by the underlying cookie engine. While the exact behavior is dependant on the platform used, typically, setting cookies via this header appends them to those set by engine. Additional resources: [ClearCookieCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.ClearCookieCache.html).  
  
In addition, the following headers are filled by the Web browser on the **Web** platform, and therefore might not have any custom values set: `Cookie`, `Cookie2`, `User-Agent`.
* * *
