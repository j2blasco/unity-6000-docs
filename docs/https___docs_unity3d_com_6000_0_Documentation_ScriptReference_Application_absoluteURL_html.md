* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-absoluteURL.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).absoluteURL
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
absoluteURL; 
### Description
The URL of the document. For WebGL, this is a web URL. For Android, iOS, or Universal Windows Platform (UWP) this is a deep link URL (Read Only).
**WebGL** : The URL of the document as shown in a browser's address bar.  
  
**Android:** If the application has been launched or activated using an Intent Filter, a deep link (App Link) URL.  
  
**iOS:** If the application has been launched or activated using a URL Scheme or a Universal Link, a deep link (Universal Link) URL.  
  
**UWP:** If the application has been launched or activated using a custom URI scheme, a deep link URL.  
  
**Note** : If the deep link is activated while the application is running [Application.deepLinkActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-deepLinkActivated.html) delegate is called.
* * *
