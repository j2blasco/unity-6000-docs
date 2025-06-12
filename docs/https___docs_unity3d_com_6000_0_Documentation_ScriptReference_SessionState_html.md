* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.html

# SessionState
class in UnityEditor
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
SessionState is a Key-Value Store intended for storing and retrieving Editor session state that should survive assembly reloading.
The state information stored in SessionState is cleared when Unity exits. For storing state information that should be persistent across Unity Editor sessions use [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).
### Static Methods
Method | Description  
---|---  
[EraseBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseBool.html) | Erase a Boolean entry in the key-value store.  
[EraseFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseFloat.html) | Erase a Float entry in the key-value store.  
[EraseInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseInt.html) | Erase an Integer entry in the key-value store.  
[EraseIntArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseIntArray.html) | Erase an Integer array entry in the key-value store.  
[EraseString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseString.html) | Erase a String entry in the key-value store.  
[EraseVector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.EraseVector3.html) | Erase a Vector3 entry in the key-value store.  
[GetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetBool.html) | Retrieve a Boolean value.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetFloat.html) | Retrieve a Float value.  
[GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetInt.html) | Retrieve an Integer value.  
[GetIntArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetIntArray.html) | Retrieve an Integer array.  
[GetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetString.html) | Retrieve a String value.  
[GetVector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.GetVector3.html) | Retrieve a Vector3.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetBool.html) | Store a Boolean value.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetFloat.html) | Store a Float value.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetInt.html) | Store an Integer value.  
[SetIntArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetIntArray.html) | Store an Integer array.  
[SetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetString.html) | Store a String value.  
[SetVector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.SetVector3.html) | Store a Vector3.  
* * *
