* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.GetResponseHeader.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).GetResponseHeader
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
public string GetResponseHeader(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of the HTTP header to retrieve. Case-insensitive.  
### Returns
**string** The value of the HTTP header from the latest HTTP response. If no header with a matching name has been received, or no responses have been received, returns `null`. 
### Description
Retrieves the value of a response header from the latest HTTP response received.
In the case that this UnityWebRequest has received multiple responses (such as during redirects), only headers from the newest (or final) response are checked.
* * *
