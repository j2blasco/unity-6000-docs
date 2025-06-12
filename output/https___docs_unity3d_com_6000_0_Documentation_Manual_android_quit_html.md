* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-quit.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * Quit a Unity Android application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-handle-crashes.html)
Handle Android crashes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
Building and delivering for Android
# Quit a Unity Android application
The Android operating system has a built-in user interface to hide and close applications (refer to [Close apps](https://support.google.com/android/answer/9079646?hl=en-GB#zippy=%2Cclose-apps)) so you shouldn’t add your own interface to quit your application. Users recognize Android’s interface as the way to close applications so if you create your own, users will have an inconsistent user experience between your application and other Android applications. If you must programmatically close an Android application, it’s best practice to use [Activity.moveTaskToBack](https://developer.android.com/reference/android/app/Activity#moveTaskToBack\(boolean\)) instead of [Application.Quit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Quit.html). `Activity.moveTaskToBack` pauses the application and moves it to the background, which is closer to the standard Android application lifecycle than `Application.Quit`.
The following code sample shows how to move your application to the back of the activity stack.
```
using UnityEngine;

public class QuitApplicationUtility
{
    public static void MoveAndroidApplicationToBack()
    {
        AndroidJavaObject activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject>("currentActivity");
        activity.Call<bool>("moveTaskToBack", true);
    }
}

```

## Additional resources
  * [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-handle-crashes.html)
Handle Android crashes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
Building and delivering for Android
