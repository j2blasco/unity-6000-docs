* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-method.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).method
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
method; 
### Description
Defines the HTTP verb used by this [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html), such as `GET` or `POST`.
This property may be set to any non-zero-length alphabetic string, and will be used verbatim. Therefore, this property can be employed to set the UnityWebRequest to transmit any custom HTTP verb required by an application.  
  
This property cannot be changed after calling [Send](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Send.html).  
  
**Note:** This method will always return strings in UPPERCASE. When setting the verb, the input value will automatically be converted to UPPERCASE.  
  
_Default value:_ `GET`.
* * *
