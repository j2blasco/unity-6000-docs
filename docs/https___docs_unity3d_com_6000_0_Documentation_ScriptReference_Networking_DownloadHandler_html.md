* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html

# DownloadHandler
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
Manage and process HTTP response body data received from a remote server.
DownloadHandler objects are helper objects. When attached to a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html), they define how to handle HTTP response body data received from a remote server. Generally, they are used to buffer, stream and/or process response bodies.  
  
DownloadHandler is a base class. Depending on usage scenario, different specialized classes are available. [DownloadHandlerBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerBuffer.html) provides basic buffering, while [DownloadHandlerTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerTexture.html) and [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html) provide more efficient solutions for [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) and [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) downloads.  
  
For custom use cases, see [DownloadHandlerScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerScript.html).  
  
Additional resources: [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html), [DownloadHandlerBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerBuffer.html), [DownloadHandlerTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerTexture.html), [DownloadHandlerAudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.html), [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html), [DownloadHandlerScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerScript.html).
### Properties
Property | Description  
---|---  
[data](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler-data.html) | Returns the raw bytes downloaded from the remote server, or null. (Read Only)  
[error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler-error.html) | Error message describing a failure that occurred inside the download handler.  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler-isDone.html) | Returns true if this DownloadHandler has been informed by its parent UnityWebRequest that all data has been received, and this DownloadHandler has completed any necessary post-download processing. (Read Only)  
[nativeData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler-nativeData.html) | Provides direct access to downloaded data.  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler-text.html) | Convenience property. Returns the bytes from data interpreted as a UTF8 string. (Read Only)  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.Dispose.html) | Signals that this DownloadHandler is no longer being used, and should clean up any resources it is using.  
### Protected Methods
Method | Description  
---|---  
[CompleteContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.CompleteContent.html) | Callback, invoked when all data has been received from the remote server.  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetData.html) | Callback, invoked when the data property is accessed.  
[GetNativeData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetNativeData.html) | Provides allocation-free access to the downloaded data as a NativeArray.  
[GetProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetProgress.html) | Callback, invoked when UnityWebRequest.downloadProgress is accessed.  
[GetText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetText.html) | Callback, invoked when the text property is accessed.  
[ReceiveContentLengthHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.ReceiveContentLengthHeader.html) | Callback, invoked with a Content-Length header is received.  
[ReceiveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.ReceiveData.html) | Callback, invoked as data is received from the remote server.  
* * *
