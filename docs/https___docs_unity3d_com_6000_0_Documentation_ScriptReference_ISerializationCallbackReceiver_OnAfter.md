* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnAfterDeserialize.html

#  [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html).OnAfterDeserialize
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
public void OnAfterDeserialize(); 
### Description
Implement this callback to transform data back into runtime data types after an object is deserialized.
Unity invokes the `OnAfterDeserialize` callback on an object after deserializing it. In this callback, you can transform the deserialized data back into your preferred runtime data type. For example, use key and value arrays to repopulate a C# `Dictionary` object.  
  
Refer to [Custom serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html) in the Manual for more information. 
* * *
