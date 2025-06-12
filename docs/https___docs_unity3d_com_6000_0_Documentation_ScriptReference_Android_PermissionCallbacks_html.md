* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.html

# PermissionCallbacks
class in UnityEngine.Android
/
Inherits from:[AndroidJavaProxy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.html)
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
Contains callbacks invoked when permission request is executed using [Permission.RequestUserPermission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermission.html).
### Events
Event | Description  
---|---  
[PermissionDenied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.PermissionDenied.html) | Triggered when the user chooses Deny for a permission request.  
[PermissionDeniedAndDontAskAgain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.PermissionDeniedAndDontAskAgain.html) | Triggered when the user chooses Deny And Don't Ask Again for a permission request or denies the permission twice on newer Android versions, or the operating system determines that it should not be requested again.  
[PermissionGranted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.PermissionGranted.html) | Triggered when the user chooses Allow for a permission request.  
[PermissionRequestDismissed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.PermissionRequestDismissed.html) | Triggered when the user dismisses the permission request without explicitly choosing any option.  
### Inherited Members
### Properties
Property | Description  
---|---  
[javaInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-javaInterface.html) | Java interface implemented by the proxy.  
### Public Methods
Method | Description  
---|---  
[equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-equals.html) | The equivalent of the java.lang.Object equals() method.  
[hashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-hashCode.html) | The equivalent of the java.lang.Object hashCode() method.  
[Invoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.Invoke.html) | Called by the java vm whenever a method is invoked on the java proxy interface. You can override this to run special code on method invocation, or you can leave the implementation as is, and leave the default behavior which is to look for c# methods matching the signature of the java method.  
[toString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-toString.html) | The equivalent of the java.lang.Object toString() method.  
* * *
