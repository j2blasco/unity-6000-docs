* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Toast.Create.html

#  [Toast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Toast.html).Create
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
public static [WSA.Toast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Toast.html) Create(string xml); 
## Declaration
public static [WSA.Toast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Toast.html) Create(string image, string text); 
### Parameters
Parameter | Description  
---|---  
xml | XML document with tile data.  
image | Uri to image to show on a toast, can be empty, in that case text-only notification will be shown.  
text | A text to display on a toast notification.  
### Returns
**Toast** A toast object for further work with created notification or null, if creation of toast failed. 
### Description
Create toast notification.
Toast notification is created by providing XML document with it's data. A second variant is a convenience method to show simple toast with text, optionally with image on it.
* * *
