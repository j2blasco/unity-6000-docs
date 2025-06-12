* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).SendWebRequest
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
public [Networking.UnityWebRequestAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAsyncOperation.html) SendWebRequest(); 
### Description
Begin communicating with the remote server.
After calling this method, the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) will perform DNS resolution (if necessary), transmit an HTTP request to the remote server at the target URL and process the server’s response.  
  
This method can only be called once on any given [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) object.  
  
Once this method is called, you cannot change any of the UnityWebRequest’s properties. You cannot change [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) properties after [SendWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html) is called.  
  
This method returns a WebRequestAsyncOperation object. Yielding the WebRequestAsyncOperation inside a coroutine will cause the coroutine to pause until the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) encounters a system error or finishes communicating. 
* * *
