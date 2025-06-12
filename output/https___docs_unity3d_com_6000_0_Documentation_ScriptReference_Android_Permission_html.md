* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html

# Permission
struct in UnityEngine.Android
/
Implemented in:[UnityEngine.AndroidJNIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AndroidJNIModule.html)
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
Structure describing a permission that requires user authorization.
### Static Properties
Property | Description  
---|---  
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Camera.html) | Used when requesting permission or checking if permission has been granted to use the camera.  
[CoarseLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.CoarseLocation.html) | Used when requesting permission or checking if permission has been granted to use the users location with coarse granularity.  
[ExternalStorageRead](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.ExternalStorageRead.html) | Used when requesting permission or checking if permission has been granted to read from external storage such as a SD card.  
[ExternalStorageWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.ExternalStorageWrite.html) | Used when requesting permission or checking if permission has been granted to write to external storage such as a SD card.  
[FineLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.FineLocation.html) | Used when requesting permission or checking if permission has been granted to use the users location with high precision.  
[Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Microphone.html) | Used when requesting permission or checking if permission has been granted to use the microphone.  
### Static Methods
Method | Description  
---|---  
[HasUserAuthorizedPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.HasUserAuthorizedPermission.html) | Check if the user has granted access to a device resource or information that requires authorization.  
[RequestUserPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermission.html) | Request the user to grant access to a device resource or information that requires authorization.  
[RequestUserPermissions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermissions.html) | Request the user to grant access to multiple device resources or information that requires authorization.  
[ShouldShowRequestPermissionRationale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.ShouldShowRequestPermissionRationale.html) | Check whether to display the UI explaining the reason for permission before requesting it.  
* * *
