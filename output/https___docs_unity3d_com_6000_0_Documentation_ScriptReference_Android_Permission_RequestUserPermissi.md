* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermissions.html

#  [Permission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html).RequestUserPermissions
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
public static void RequestUserPermissions(string[] permissions, [Android.PermissionCallbacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.html) callbacks); 
## Declaration
public static void RequestUserPermissions(string[] permissions); 
### Parameters
Parameter | Description  
---|---  
callbacks | An instance of callbacks invoked when permission request is executed.  
permissions | An array of strings that describe the permissions to request.  
### Description
Request the user to grant access to multiple device resources or information that requires authorization.
* * *
