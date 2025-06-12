* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * Call Java and Kotlin plug-in code from C# scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html)
Java and Kotlin source plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html)
Integrating Unity into Android applications
# Call Java and Kotlin plug-in code from C# scripts
To call Java code from C# scripts, Unity provides C# APIs that communicate with the Android [Java Native Interface](https://developer.android.com/training/articles/perf-jni) (JNI) through C++. Unity provides both a low level and a high level API that you can use to interact with Java code using JNI.
## Low-level API
The low-level [AndroidJNI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNI.html) class wraps JNI calls and provides static methods that directly map to JNI methods. The [AndroidJNIHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.html) API provides helper functionality that’s primarily used by the high-level API, but they can be useful in certain situations.
## High-level API
The high-level [AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html), [AndroidJavaClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass.html), and [AndroidJavaProxy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.html) APIs automate a lot of tasks required for JNI calls. They also use caching to make calls to Java faster. The combination of `AndroidJavaObject` and `AndroidJavaClass` is built on top of `AndroidJNI` and `AndroidJNIHelper`, but they also contain additional functionality such as static methods that you can use to access static members of Java classes.
You can use the [AndroidApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication.html) class to access instances of `currentActivity`, `currentContext`, and `currentConfiguration` for your application in a simplified way. Additionally, it also allows you to delegate code execution on the UI or main thread based on your application’s requirement.
Instances of `AndroidJavaObject` and `AndroidJavaClass` have a one-to-one mapping to an instance of [java.lang.Object](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html) and [java.lang.Class](https://docs.oracle.com/javase/7/docs/api/java/lang/Class.html) respectively. They provide three types of interactions with Java/Kotlin code:
  * [Call](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Call.html) a method.
  * [Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Get.html) the value of a field.
  * [Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Set.html) the value of a field.


Each interaction also has a static version:
  * [CallStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.CallStatic.html) to call a static method.
  * [GetStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.GetStatic.html) to get the value of a static field.
  * [SetStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.SetStatic.html) to set the value of a static field.


When you get the value of a field or call a method that returns a value, you use [generics](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics) to specify the return type. When you set the value of a field, you also use generics to specify the type of the field that you are setting. For methods that don’t return a value, there is a regular, non-generic, version of [Call](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Call.html).
**Important** : You must access any [non-primitive type](http://developer.android.com/reference/java/lang/Class.html) as an `AndroidJavaObject`. The only exception is a string which you access directly, even though they don’t represent a primitive type in Java.
The following code samples demonstrate how to use the high-level `AndroidJavaObject`, `AndroidJavaClass` APIs and Unity’s `AndroidApplication` class.
### Get the hash code for a Java string
The following code sample creates an instance of [java.lang.String](http://developer.android.com/reference/java/lang/String.html) initialized with a [string](http://developer.android.com/reference/java/lang/String.html#String\(java.lang.StringBuilder\)), and retrieves the [hash value](http://developer.android.com/reference/java/lang/String.html#hashCode\(\)) for that string.
```
using UnityEngine;
public class JavaExamples
{
    public static int GetJavaStringHashCode(string text)
    {
        using (AndroidJavaObject jo = new AndroidJavaObject("java.lang.String", text))
        {
            int hash = jo.Call<int>("hashCode");
            return hash;
        }
    }
}

```

This example:
  1. Creates an `AndroidJavaObject` that represents a [java.lang.String](http://developer.android.com/reference/java/lang/String.html). The `AndroidJavaObject` constructor takes at least one parameter, which is the name of the class to construct an instance of. Any parameters after the class name are for the constructor call on the object, in this case the `text` parameter from `GetJavaStringHashCode`.
  2. Calls [hashCode()](https://developer.android.com/reference/java/lang/String.html#hashCode\(\)) to get the hash code of the string. This call uses the `int` generic type parameter for `Call` because `hashCode()` returns the hash code as an integer.


**Note** : You can’t use dotted notation to instantiate a nested Java class. You must use the `$` separator to instantiate inner classes. For example, Use `android.view.ViewGroup$LayoutParams` or `android/view/ViewGroup$LayoutParams`, where the `LayoutParams` class is nested in the `ViewGroup` class.
### Get the cache directory
The following code sample shows how to get the cache directory for the current application in C# using the `AndroidApplication` class.
```
using UnityEngine;
using UnityEngine.Android;

public class JavaExamples
{
    public static string GetApplicationCacheDirectory()
    {
        using var javaFile = AndroidApplication.currentActivity.Call<AndroidJavaObject>("getCacheDir");
        var cacheDirectory = javaFile.Call<string>("getCanonicalPath");
        return cacheDirectory;
    }
}

```

This example:
  1. Uses `AndroidApplication.currentActivity` to access the current Android activity, without explicitly creating `AndroidJavaClass` or `AndroidJavaObject` instances.
  2. Calls [getCacheDir()](http://developer.android.com/reference/android/content/Context.html#getCacheDir\(\)) on the Activity object, which returns a [File](https://developer.android.com/reference/java/io/File.html) object that represents the cache directory.
  3. Calls [getCanonicalPath()](http://developer.android.com/reference/java/io/File.html#getCanonicalPath\(\)) on the File object can to get the cache directory as a string.


**Note** : This example is for reference purposes. Instead, to access the application’s cache and file directory use the [Application.temporaryCachePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-temporaryCachePath.html) and [Application.persistentDataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html) APIs.
### Pass data from Java to Unity
The following code sample shows how to pass data from Java to Unity using `UnitySendMessage`.
```
using UnityEngine;
using UnityEngine.Android;

public class JavaExamples : MonoBehaviour
{
    private void Start()
    {
        AndroidJNIHelper.debug = true;
        AndroidApplication.unityPlayer.CallStatic("UnitySendMessage", "My GameObject", "JavaMessage", "NewMessage");
    }

    private void JavaMessage(string message)
    {
        Debug.Log("message from java: " + message);
    }
}

```

This example:
  1. Uses `AndroidApplication.unityPlayer` to access the Java instance used by an activity without explicitly creating an `AndroidJavaClass` instance.
  2. Calls the static`UnitySendMessage` method that’s a member of `com.unity3d.player.UnityPlayer`.


Although you call `UnitySendMessage` from within Unity, it uses Java to relay the message, which then calls back to the native/Unity code to deliver it to the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) named `My GameObject` which has an attached script that contains a method called `JavaMessage`.
## Best practices
Refer to the following best practices when you call Java and Kotlin **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) code from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
### Minimize JNI calls
Using the Java Native Interface (JNI), through either the high-level or low-level C# API is resource intensive and can be slow. To improve performance, and also code clarity, it’s best practice to keep the number of JNI calls low.
To avoid unnecessary JNI calls, the high-level C# API caches the [ID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNI.GetMethodID.html) of each Java method that you call. This means that subsequent calls to the same method aren’t as resource intensive as the first call. The calls don’t need to be during the same frame or even from the same AndroidJavaObject/AndroidJavaClass instance. If you use the low-level API and want this performance benefit, you must cache method ID yourself. Otherwise, it’s best practice to use the high-level API.
**Note** : Unity maintains the cache until the application [closes](https://support.google.com/android/answer/9079646?hl=en-GB). This includes while the application is in the background.
### Garbage collection
You should wrap any instance of `AndroidJavaObject` or `AndroidJavaClass` with a `using` statement to ensure Unity destroys them as soon as possible. If you don’t use `using`, Unity’s [garbage collector](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html) should still release all created instances, but you lose control of when this will be.
The following code sample shows how to use `using` statements to get the system language in an optimal way:
```
using UnityEngine;

public class LocaleExample : MonoBehaviour
{
    void Start()
    {
        using (AndroidJavaClass cls = new AndroidJavaClass("java.util.Locale"))
        using (AndroidJavaObject locale = cls.CallStatic<AndroidJavaObject>("getDefault"))
        {
            if (locale != null)
            {
                Debug.Log("current lang = " + locale.Call<string>("getDisplayLanguage"));
            }
        }
    }
}

```

**Note** : To access a record of the garbage collector’s activity in [Android Logcat](https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@latest/index.html), set [AndroidJNIHelper.debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper-debug.html) to `true`.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html)
Java and Kotlin source plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html)
Integrating Unity into Android applications
