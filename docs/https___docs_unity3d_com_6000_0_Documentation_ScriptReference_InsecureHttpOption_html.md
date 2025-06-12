* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InsecureHttpOption.html

# InsecureHttpOption
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
Options for allowing plain text HTTP connections for [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).
Plain text HTTP connections are not secure, and can make your application vulnerable to security threats. By default, [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) uses secure HTTPS connections instead.  
  
Use this enum to configure when [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) is allowed to use HTTP plain text connections.
### Properties
Property | Description  
---|---  
[NotAllowed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InsecureHttpOption.NotAllowed.html) | Do not allow UnityWebRequest to use plain text HTTP connections.  
[DevelopmentOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InsecureHttpOption.DevelopmentOnly.html) | Allow UnityWebRequest to use plain text HTTP connections in development builds only.  
[AlwaysAllowed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InsecureHttpOption.AlwaysAllowed.html) | Allow UnityWebRequest to use plain text HTTP connections at all times.  
* * *
