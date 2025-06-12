* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-redirectLimit.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).redirectLimit
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
redirectLimit; 
### Description
Indicates the number of redirects that this [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) follows before halting with a `Redirect Limit Exceeded` system error.
If you want to disable redirects altogether, set this property to zero - this `UnityWebRequest` will then refuse to follow redirects. If a redirect is encountered while redirects are disabled, the request will halt with a `Redirect Limit Exceeded` system error.  
  
If you don't want to limit the number of redirects, you can set this property to any negative number. **Note:** **This is not recommended**. If the redirect limit is disabled and the `UnityWebRequest` encounters a redirect loop, the `UnityWebRequest` will consume processor time until [Abort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Abort.html) is called.  
  
**Note:** On WebGL platforms, the `UnityWebRequest` API behaves differently. It only supports a redirect limit of `0` where the request fails on a redirect, and for anything above `0`, it uses the browser-default redirect limit. This applies to Unity 2021.3 and later versions.  
  
  
  
_Default value:_ `32`.
* * *
