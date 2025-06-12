* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-uri.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).uri
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
uri; 
### Description
Defines the target URI for the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) to communicate with.
The passed Uri must be full absolute URI.  
  
This property cannot be set after calling [SendWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.SendWebRequest.html).  
  
If the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) encounters and follows redirects, this property will be updated with the URL to which the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) was redirected.  
  
Same as [url](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-url.html), but has less validation and pre-processing, so is much faster to set. Reading it's value is, however, more expensive because the new Uri instance is created, so if you want to get the URL your request ended up to, it's recommended to use [url](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-url.html), unless an Uri object is what you need.
* * *
