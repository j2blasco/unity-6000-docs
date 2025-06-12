* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.html

# AndroidJavaProxy
class in UnityEngine
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
This class can be used to implement any java interface. Any java vm method invocation matching the interface on the proxy object will automatically be passed to the c# implementation.
**Note** : this API can be used from custom thread, but requires that thread to be attached to JVM first, see [AndroidJNI.AttachCurrentThread](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNI.AttachCurrentThread.html).
```
// Opens an android date picker dialog and grabs the result using a callback.
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static DateTime selectedDate = DateTime.Now;  
  
    class DateCallback : AndroidJavaProxy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.html)
    {
        public DateCallback() : base("android.app.DatePickerDialog$OnDateSetListener") {}
        void onDateSet(AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html) view, int year, int monthOfYear, int dayOfMonth)
        {
            selectedDate = new DateTime(year, monthOfYear + 1, dayOfMonth);
            // If you have no longer any uses for the object, it must be disposed to prevent a leak
            view.Dispose();
        }
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(15, 15, 450, 75), string.Format("{0:yyyy-MM-dd}", selectedDate)))
        {
            var activity = new AndroidJavaClass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass.html)("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)>("currentActivity");
            activity.Call("runOnUiThread", new AndroidJavaRunnable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaRunnable.html)(() =>
            {
                new AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)("android.app.DatePickerDialog", activity, new DateCallback(), selectedDate.Year, selectedDate.Month - 1, selectedDate.Day).Call("show");
            }));
        }
    }
}

```

### Properties
Property | Description  
---|---  
[javaInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-javaInterface.html) | Java interface implemented by the proxy.  
### Constructors
Constructor | Description  
---|---  
[AndroidJavaProxy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-ctor.html) |   
### Public Methods
Method | Description  
---|---  
[equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-equals.html) | The equivalent of the java.lang.Object equals() method.  
[hashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-hashCode.html) | The equivalent of the java.lang.Object hashCode() method.  
[Invoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy.Invoke.html) | Called by the java vm whenever a method is invoked on the java proxy interface. You can override this to run special code on method invocation, or you can leave the implementation as is, and leave the default behavior which is to look for c# methods matching the signature of the java method.  
[toString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaProxy-toString.html) | The equivalent of the java.lang.Object toString() method.  
* * *
