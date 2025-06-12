* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-deepLinkActivated.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).deepLinkActivated
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
### Parameters
Parameter | Description  
---|---  
value | The deep link URL that activated the application.  
### Description
This event is raised when an application running on Android, iOS, or the Universal Windows Platform (UWP) is activated using a deep link URL.
**Note** : When this delegate is called [Application.absoluteURL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-absoluteURL.html) property is also updated.  
  
**Note** : This event never fires on the Web platform. This is because a Web browser page can't act as an application protocol handler for `unitydl://` links.
* * *
