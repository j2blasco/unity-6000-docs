* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetRequestHeader.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).GetRequestHeader
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
public string GetRequestHeader(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name of the custom request header. Case-insensitive.  
### Returns
**string** The value of the custom request header. If no custom header with a matching name has been set, returns an empty string. 
### Description
Retrieves the value of a custom request header.
This method retrieves the value of custom (i.e. user-set) request headers. These are the headers which will be transmitted _to_ the remote server as part of the HTTP request.  
  
Additional resources: [SetRequestHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SetRequestHeader.html).
* * *
