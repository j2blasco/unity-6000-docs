* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.OnBeforeSerialize.html

#  [ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html).OnBeforeSerialize
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
public void OnBeforeSerialize(); 
### Description
Implement this callback to transform data into serializable data types immediately before an object is serialized.
Unity invokes the `OnBeforeSerialize` callback on an object before serializing it. In this callback, you can transform your data into something Unity understands. For example, to serialize a C# `Dictionary`, copy the data from the `Dictionary` object into an array of keys and an array of values.  
  
Refer to [Custom serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html) in the Manual for more information.  
  
**Note:** Unity calls `OnBeforeSerialize` before recompiling scripts in a domain reload, so any changes made to code in this method won't take effect until the second invocation of the callback following the change, in other words after a full serialization and domain reload cycle. For more information, refer to [Details of disabling domain and scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html) in the Manual. 
* * *
