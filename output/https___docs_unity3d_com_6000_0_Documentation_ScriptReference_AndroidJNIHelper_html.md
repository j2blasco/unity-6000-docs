* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.html

# AndroidJNIHelper
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
Helper interface for JNI interaction; signature creation and method lookups.  
  
**Note:** Using _raw_ JNI functions requires advanced knowledge of the Android Java Native Interface (JNI). _Please take note._
### Static Properties
Property | Description  
---|---  
[debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper-debug.html) | Set debug to true to log calls through the AndroidJNIHelper.  
### Static Methods
Method | Description  
---|---  
[Box](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.Box.html) | Convert primitive to it's object counterpart.  
[ConvertFromJNIArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.ConvertFromJNIArray.html) | Creates a managed array from a Java array.  
[ConvertToJNIArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.ConvertToJNIArray.html) | Creates a Java array from a managed array.  
[CreateJavaProxy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.CreateJavaProxy.html) | Creates a java proxy object which connects to the supplied proxy implementation.  
[CreateJavaRunnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.CreateJavaRunnable.html) | Creates a UnityJavaRunnable object (implements java.lang.Runnable).  
[CreateJNIArgArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.CreateJNIArgArray.html) | Creates the parameter array to be used as argument list when invoking Java code through CallMethod() in AndroidJNI.  
[DeleteJNIArgArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.DeleteJNIArgArray.html) | Deletes any local jni references previously allocated by CreateJNIArgArray().  
[GetConstructorID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.GetConstructorID.html) | Scans a particular Java class for a constructor method matching a signature.  
[GetFieldID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.GetFieldID.html) | Scans a particular Java class for a field matching a name and a signature.  
[GetMethodID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.GetMethodID.html) | Scans a particular Java class for a method matching a name and a signature.  
[GetSignature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.GetSignature.html) | Creates the JNI signature string for particular object type.  
[Unbox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJNIHelper.Unbox.html) | Converts Java object of a boxed type to its primitive counterpart.  
* * *
