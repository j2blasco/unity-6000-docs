* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-downloadHandler.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).downloadHandler
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
[Networking.DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) downloadHandler; 
### Description
Holds a reference to a [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) object, which manages body data received from the remote server by this [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).
Setting this property to `null` indicates that this [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) does not care about the response’s body data; all received body data will be ignored and discarded. See the reference on [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) objects for more information on creating and using DownloadHandlers.  
  
This property cannot be changed after calling [Send](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Send.html).  
  
_Default value:_ `null`.
* * *
