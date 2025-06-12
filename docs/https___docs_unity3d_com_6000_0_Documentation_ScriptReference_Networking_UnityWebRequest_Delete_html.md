* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Delete.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).Delete
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
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) Delete(string uri); 
### Parameters
Parameter | Description  
---|---  
uri | The URI to which a `DELETE` request should be sent.  
### Returns
**UnityWebRequest** A UnityWebRequest configured to send an HTTP `DELETE` request. 
### Description
Creates a UnityWebRequest configured for HTTP `DELETE`.
This method creates a UnityWebRequest, sets the verb to `DELETE` and sets the target URL to the string argument `uri`. It sets no custom flags or headers.  
  
This method attaches no [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) or [UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) to the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).
* * *
