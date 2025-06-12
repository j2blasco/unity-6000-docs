* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.html

# Result
enumeration
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
Defines codes describing the possible outcomes of a UnityWebRequest.
### Properties
Property | Description  
---|---  
[InProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.InProgress.html) | The request hasn't finished yet.  
[Success](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html) | The request succeeded.  
[ConnectionError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ConnectionError.html) | Failed to communicate with the server. For example, the request couldn't connect or it could not establish a secure channel.  
[ProtocolError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ProtocolError.html) | The server returned an error response. The request succeeded in communicating with the server, but received an error as defined by the connection protocol.  
[DataProcessingError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.DataProcessingError.html) | Error processing data. The request succeeded in communicating with the server, but encountered an error when processing the received data. For example, the data was corrupted or not in the correct format.  
* * *
