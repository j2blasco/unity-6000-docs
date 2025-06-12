* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass.html

# AndroidJavaClass
class in UnityEngine
/
Inherits from:[AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)
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
AndroidJavaClass is the Unity representation of a generic instance of java.lang.Class.
**Note** : this API can be used from custom thread, but requires that thread to be attached to JVM first, see [AndroidJNI.AttachCurrentThread](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNI.AttachCurrentThread.html).
### Constructors
Constructor | Description  
---|---  
[AndroidJavaClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass-ctor.html) | Construct an AndroidJavaClass from the class name.  
### Inherited Members
### Public Methods
Method | Description  
---|---  
[Call](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Call.html) | Calls a Java method on an object (non-static).  
[CallStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.CallStatic.html) | Call a static Java method on a class.  
[CloneReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.CloneReference.html) | Creates a clone of the C# object that references the same Java object.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Dispose.html) | IDisposable callback.  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Get.html) | Get the value of a field in an object (non-static).  
[GetRawClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.GetRawClass.html) | Retrieves the raw jclass pointer to the Java class.Note: Using raw JNI functions requires advanced knowledge of the Android Java Native Interface (JNI).  
[GetRawObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.GetRawObject.html) | Retrieves the raw jobject pointer to the Java object.Note: Using raw JNI functions requires advanced knowledge of the Android Java Native Interface (JNI).  
[GetStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.GetStatic.html) | Get the value of a static field in an object type.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Set.html) | Set the value of a field in an object (non-static).  
[SetStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.SetStatic.html) | Set the value of a static field in an object type.  
* * *
