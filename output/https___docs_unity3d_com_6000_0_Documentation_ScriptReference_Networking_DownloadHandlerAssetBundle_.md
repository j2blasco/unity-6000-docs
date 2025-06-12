* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html

# DownloadHandlerAssetBundle
class in UnityEngine.Networking
/
Inherits from:[Networking.DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html)
/
Implemented in:[UnityEngine.UnityWebRequestAssetBundleModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UnityWebRequestAssetBundleModule.html)
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
A [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) subclass specialized for downloading [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)s.
This subclass streams downloaded data into Unity's asset bundle decompression and decoding system on worker threads, providing efficient downloading and processing for [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) objects. Additional resources: [UnityWebRequestAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html)
### Properties
Property | Description  
---|---  
[assetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle-assetBundle.html) | Returns the downloaded AssetBundle, or null. (Read Only)  
[autoLoadAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle-autoLoadAssetBundle.html) | If true, the AssetBundle will be loaded as part of the UnityWebRequest process. If false, the AssetBundle will be loaded on demand when accessing the DownloadHandlerAssetBundle.assetBundle property.  
[isDownloadComplete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle-isDownloadComplete.html) | Returns true if the data downloading portion of the operation is complete.  
### Constructors
Constructor | Description  
---|---  
[DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle-ctor.html) | Standard constructor for non-cached asset bundles.  
### Protected Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetData.html) | Not implemented. Throws NotSupportedException.  
[GetText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetText.html) | Not implemented. Throws NotSupportedException.  
### Static Methods
Method | Description  
---|---  
[GetContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html) | Returns the downloaded AssetBundle, or null.  
### Inherited Members
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
[GetNativeData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetNativeData.html) | Provides allocation-free access to the downloaded data as a NativeArray.  
[GetProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.GetProgress.html) | Callback, invoked when UnityWebRequest.downloadProgress is accessed.  
[ReceiveContentLengthHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.ReceiveContentLengthHeader.html) | Callback, invoked with a Content-Length header is received.  
[ReceiveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.ReceiveData.html) | Callback, invoked as data is received from the remote server.  
* * *
