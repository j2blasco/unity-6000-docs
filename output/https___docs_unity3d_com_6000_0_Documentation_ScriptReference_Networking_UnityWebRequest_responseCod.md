* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-responseCode.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).responseCode
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
responseCode; 
### Description
The numeric HTTP response code returned by the server, such as `200`, `404` or `500`. (Read Only)
If the UnityWebRequest has received multiple responses (due to redirects), then this property will return the response code of the newest (or final) HTTP response.  
  
If the UnityWebRequest has not yet processed a response, this property will return -1.
* * *
