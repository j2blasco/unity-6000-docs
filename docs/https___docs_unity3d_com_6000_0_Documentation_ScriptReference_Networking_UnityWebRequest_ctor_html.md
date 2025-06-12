* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-ctor.html

# UnityWebRequest Constructor
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
public UnityWebRequest(); 
## Declaration
public UnityWebRequest(string url); 
## Declaration
public UnityWebRequest(Uri uri); 
## Declaration
public UnityWebRequest(string url, string method); 
## Declaration
public UnityWebRequest(Uri uri, string method); 
## Declaration
public UnityWebRequest(string url, string method, [Networking.DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) downloadHandler, [Networking.UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) uploadHandler); 
## Declaration
public UnityWebRequest(Uri uri, string method, [Networking.DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) downloadHandler, [Networking.UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) uploadHandler); 
### Parameters
Parameter | Description  
---|---  
url | The target URL with which this UnityWebRequest will communicate. Also accessible via the [url](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-url.html) property.  
uri | The target URI to which form data will be transmitted.  
method | HTTP GET, POST, etc. methods.  
downloadHandler | Replies from the server.  
uploadHandler | Upload data to the server.  
### Description
Creates a UnityWebRequest with the default options and no attached [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) or [UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html). Default method is `GET`.
The raw constructor is useful for use cases which require detailed custom configuration of a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html). Most use cases will require the attachment of a [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html), an [UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) or both in order to function propertly.  
  
Additional resources: [Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html), [GetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetTexture.html), [GetAudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetAudioClip.html), [GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetAssetBundle.html), [Head](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Head.html), [Post](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html), [Put](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Put.html), [Delete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Delete.html).
* * *
