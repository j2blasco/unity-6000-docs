* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity-command-line.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * [The Activity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)
  * [Extend the default Unity activity](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidUnityPlayerActivity.html)
  * Specify Android Player command-line arguments


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity.html)
Create a custom activity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
The GameActivity application entry point
# Specify Android Player command-line arguments
You can extend the custom Unity activity to pass command-line arguments when you launch the Android Player. For information on the available command-line arguments, refer to [Command-line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html).
To specify startup command-line arguments in custom activity:
  1. [Create a custom activity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity.html) and set it as the application entry point.
  2. In the custom activity, override the `String UnityPlayerActivity.updateUnityCommandLineArguments(String cmdLine)` method.
  3. In the method, concatenate the `cmdLine` argument with your own startup arguments, then return the result.
**Important** : The `cmdLine` argument can be an empty string or null. Make sure your code handles these possible values.


The following example shows how to specify startup arguments to select the graphics API based on the current device:
```
package com.company.product;
import com.unity3d.player.UnityPlayerActivity;
import android.os.Bundle;
import android.os.Build;

public class OverrideExample extends UnityPlayerActivity {
    private boolean preferVulkan() {
        // Use Vulkan on Google Pixel devices
        if (Build.MANUFACTURER.equals("Google") && Build.MODEL.startsWith("Pixel"))
            return true;
        else
            return false;
    }

    private String appendCommandLineArgument(String cmdLine, String arg) {
        if (arg == null || arg.isEmpty())
            return cmdLine;
        else if (cmdLine == null || cmdLine.isEmpty())
            return arg;
        else
            return cmdLine + " " + arg; 
    } 

    @Override protected String updateUnityCommandLineArguments(String cmdLine)
    {
        if (preferVulkan())
            return appendCommandLineArgument(cmdLine, "-force-vulkan");
        else
            return cmdLine; // let Unity pick the Graphics API based on PlayerSettings
    }

    @Override protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
    }
}

```

### Additional ways to specify command-line arguments
Apart from the custom activity, you can specify command-line arguments in the following ways:
  * **In Android Studio** : If you open your project in Android Studio, you can pass startup command-line arguments to Unity through Launch Flags in [Run/Debug Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
  * **Via Android Debug Bridge (adb)** : You can pass command-line arguments by launching an Android application via **adb** An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ADB) using the following code.

```
adb shell am start -n "<package_name>/<activity_name>" -e unity \"<command_line_arguments>\"

```

Use the following code example to pass `-systemallocator` command-line argument to your application.
```
adb shell am start -n "com.Company.MyGame/com.unity3d.player.UnityPlayerActivity" -e unity \"-systemallocator\"

```

Use the following code example to pass `-platform-android-jobworker-affinity` command-line argument with value `little` to run the Unity job worker threads on little cores. For more information, refer to [Android thread configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/android-thread-configuration.html).
```
adb shell am start -a android.intent.action.MAIN -n "com.Company.MyGame/com.unity3d.player.UnityPlayerActivity" -e unity \"-platform-android-jobworker-affinity little\"

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity.html)
Create a custom activity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
The GameActivity application entry point
