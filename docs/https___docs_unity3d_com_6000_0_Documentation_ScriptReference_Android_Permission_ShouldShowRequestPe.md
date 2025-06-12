* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.ShouldShowRequestPermissionRationale.html

#  [Permission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html).ShouldShowRequestPermissionRationale
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
public static bool ShouldShowRequestPermissionRationale(string permission); 
### Parameters
Parameter | Description  
---|---  
permission | A string identifier for permission. This is the value of Android constant.  
### Returns
**bool** The value returned by equivalent Android method. 
### Description
Check whether to display the UI explaining the reason for permission before requesting it.
For more information on this method, refer to [Android developer documentation](https://developer.android.com/reference/android/app/Activity#shouldShowRequestPermissionRationale\(java.lang.String\)).
```
using UnityEngine;
using UnityEngine.Android;  
  
public class RequestPermissionScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    internal void PermissionCallbacks_PermissionDeniedAndDontAskAgain(string permissionName)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{permissionName} PermissionDeniedAndDontAskAgain");
    }  
  
    internal void PermissionCallbacks_PermissionGranted(string permissionName)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{permissionName} PermissionCallbacks_PermissionGranted");
    }  
  
    internal void PermissionCallbacks_PermissionDenied(string permissionName)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{permissionName} PermissionCallbacks_PermissionDenied");
    }  
  
    void Start()
    {
        if (Permission.HasUserAuthorizedPermission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.HasUserAuthorizedPermission.html)(Permission.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Microphone.html)))
        {
            // The user authorized use of the microphone.
        }
        else
        {
            bool useCallbacks = false;
            if (!useCallbacks)
            {
                // We do not have permission to use the microphone.
                // Check whether you need to display the rationale for requesting permission
                if (Permission.ShouldShowRequestPermissionRationale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.ShouldShowRequestPermissionRationale.html)(Permission.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Microphone.html)))
                    {
                    // Show a message or inform the user in other ways why your application needs the microphone permission.
                    }
                // Ask for permission or proceed without the functionality enabled.
                Permission.RequestUserPermission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermission.html)(Permission.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Microphone.html));
            }
            else
            {
                var callbacks = new PermissionCallbacks[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.html)();
                callbacks.PermissionDenied += PermissionCallbacks_PermissionDenied;
                callbacks.PermissionGranted += PermissionCallbacks_PermissionGranted;
                callbacks.PermissionDeniedAndDontAskAgain += PermissionCallbacks_PermissionDeniedAndDontAskAgain;
                Permission.RequestUserPermission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermission.html)(Permission.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Microphone.html), callbacks);
            }
        }
    }
}

```

* * *
