* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-useCustomKeystore.html

#  [PlayerSettings.Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html).useCustomKeystore
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
useCustomKeystore; 
### Description
Enable application signing with a custom keystore.
When enabled, the Android application is signed with the key specified in [keyaliasName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasName.html) from the keystore specified in [keystoreName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystoreName.html). When disabled, the application is signed with a debug key.  
  
The following code example demonstrates how to enable application signing with a custom keystore and configure keystore-specific settings.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CustomKeystoreSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Custom Keystore Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html)")]
    public static void UseCustomKeystoreSample()
    {
        // Set useCustomKeystore value to true
        PlayerSettings.Android.useCustomKeystore[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-useCustomKeystore.html) = true;
        // Log the useCustomKeystore value
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"useCustomKeystore: {PlayerSettings.Android.useCustomKeystore[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-useCustomKeystore.html)}");
        
        // Sign in settings
        // Set keyaliasName
        PlayerSettings.Android.keyaliasName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasName.html) = "keyalias";
        // Log the keyalias name
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"keyaliasName: {PlayerSettings.Android.keyaliasName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasName.html)}");
        
        // Set keyaliasPass
        PlayerSettings.Android.keyaliasPass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasPass.html) = "keyAliasPass";
        // Log the keyalias password
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"keyaliasPass: {PlayerSettings.Android.keyaliasPass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasPass.html)}");
        
        // Set keystoreName
        PlayerSettings.Android.keystoreName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystoreName.html) = "keystoreName";
        // Log the keystore name
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"keystoreName: {PlayerSettings.Android.keystoreName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystoreName.html)}");
        
        // Set keystorePass
        PlayerSettings.Android.keystorePass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystorePass.html) = "keyStorePass";
        // Log the keystore password
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"keystorePass: {PlayerSettings.Android.keystorePass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystorePass.html)}");
    }
}

```

* * *
